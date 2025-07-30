import os
import json
from datetime import datetime
from pynput import keyboard, mouse
from AppKit import NSWorkspace  # macOS-spezifisch

def read_user_id():
    try:
        with open("user_id.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        print(f"⚠️ Fehler beim Lesen der user_id.txt: {e}")
        return "UnknownUser"

USER_ID = read_user_id()
KEYLOG_FILE = "keylog.jsonl"
MOUSELOG_FILE = "mouselog.jsonl"
ACTIVE_APP_NAME = "Electron"  # ← korrekt laut Debug-Ausgabe
CURRENT_URL_FILE = "current_url.txt"

def get_current_url():
    try:
        with open(CURRENT_URL_FILE, "r", encoding="utf-8") as f:
            url = f.read().strip()
            if url.startswith("http"):
                return url
    except Exception:
        pass
    return ""

def is_custom_browser_active():
    try:
        active_app = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
        return ACTIVE_APP_NAME in active_app
    except Exception as e:
        print(f"⚠️ Fehler bei App-Check: {e}")
        return False

current_word = ""
pressed_keys = set()
logged_special_keys = set()

def log_word(word):
    log_entry = {
        "user_id": USER_ID,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "word": word,
        "url": get_current_url()
    }
    try:
        with open(KEYLOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        print(f"💾 Gespeichert (Word): {word}")
    except Exception as e:
        print(f"⚠️ Fehler beim Schreiben in {KEYLOG_FILE}: {e}")

def on_press(key):
    global current_word

    if not is_custom_browser_active():
        return

    if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r] and "ctrl" not in logged_special_keys:
        log_word("ctrl")
        logged_special_keys.add("ctrl")
    elif key in [keyboard.Key.alt_l, keyboard.Key.alt_r] and "alt" not in logged_special_keys:
        log_word("alt")
        logged_special_keys.add("alt")
    elif key == keyboard.Key.cmd and "cmd" not in logged_special_keys:
        log_word("cmd")
        logged_special_keys.add("cmd")

    pressed_keys.add(key)

def on_release(key):
    global current_word

    if not is_custom_browser_active():
        if key in pressed_keys:
            pressed_keys.remove(key)
        return

    ctrl_pressed = keyboard.Key.ctrl_l in pressed_keys or keyboard.Key.ctrl_r in pressed_keys
    cmd_pressed = keyboard.Key.cmd in pressed_keys

    try:
        if hasattr(key, 'char') and key.char is not None:
            if (ctrl_pressed and key.char.lower() == 'c'):
                log_word("ctrl+c")
            elif (ctrl_pressed and key.char.lower() == 'v'):
                log_word("ctrl+v")
            elif (cmd_pressed and key.char.lower() == 'c'):
                log_word("cmd+c")
            elif (cmd_pressed and key.char.lower() == 'v'):
                log_word("cmd+v")
            else:
                current_word += key.char
        elif key == keyboard.Key.space or key == keyboard.Key.enter:
            word = current_word.strip()
            if word:
                log_word(word)
            current_word = ""
        elif key == keyboard.Key.backspace:
            current_word = current_word[:-1]
            log_word("BACKSPACE")
    except Exception as e:
        print(f"⚠️ Fehler beim Verarbeiten der Taste: {e}")

    if key in pressed_keys:
        pressed_keys.remove(key)

    if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
        logged_special_keys.discard("ctrl")
    elif key in [keyboard.Key.alt_l, keyboard.Key.alt_r]:
        logged_special_keys.discard("alt")
    elif key == keyboard.Key.cmd:
        logged_special_keys.discard("cmd")

def on_click(x, y, button, pressed):
    if not is_custom_browser_active():
        return

    log_entry = {
        "user_id": USER_ID,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": "click" if pressed else "release",
        "x": x,
        "y": y,
        "button": str(button),
        "url": get_current_url()
    }
    try:
        with open(MOUSELOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
        print(f"💾 Gespeichert (Mouse): {button} at ({x},{y})")
    except Exception as e:
        print(f"⚠️ Fehler beim Schreiben in {MOUSELOG_FILE}: {e}")

def on_scroll(x, y, dx, dy):
    if not is_custom_browser_active():
        return

    log_entry = {
        "user_id": USER_ID,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": "scroll",
        "x": x,
        "y": y,
        "dx": dx,
        "dy": dy,
        "url": get_current_url()
    }
    try:
        with open(MOUSELOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
        print(f"💾 Gespeichert (Scroll): {dx},{dy}")
    except Exception as e:
        print(f"⚠️ Fehler beim Schreiben in {MOUSELOG_FILE}: {e}")

def start_logger():
    print("🖱️ Maus- und ⌨️ Tastatur-Logger gestartet – nur aktiv, wenn Electron im Vordergrund ist.")
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)

    keyboard_listener.start()
    mouse_listener.start()

    keyboard_listener.join()
    mouse_listener.join()

if __name__ == "__main__":
    start_logger()



















