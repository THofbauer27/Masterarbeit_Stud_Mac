# Masterarbeit_Stud_Mac

📦 MIBP Electron Browser – Masterarbeitsprojekt  
Dieses Projekt enthält einen logging-fähigen Browser zur Untersuchung des Informationssuchverhaltens. Studierende nutzen diesen Browser zur Bearbeitung von Programmieraufgaben. Dabei werden besuchte Webseiten sowie Tastatur- und Mauseingaben anonymisiert erfasst.

✅ Voraussetzungen  
1. **macOS (ab Catalina empfohlen)**

2. **Python ab Version 3.10**

   → Muss als System-App installiert sein (`python3` im Terminal ausführbar)

3. **Node.js (mind. Version 18)**

   → Muss im PATH verfügbar sein (`node -v` und `npm -v` im Terminal ausführbar)

📥 Installation (nur beim ersten Start erforderlich)  
1. **Projekt herunterladen**

   Lade das gesamte Projekt (z. B. ZIP-Datei) herunter und entpacke es an einen beliebigen Ort (z. B. Schreibtisch).

2. **Setup starten**

   Öffne das Terminal, wechsle in den entpackten Projektordner und führe den folgenden Befehl aus:

   ```bash
   chmod +x setup_mac.sh
   ./setup_mac.sh
   ```

   Das Skript installiert automatisch:

   - Alle npm-Abhängigkeiten (Electron etc.)  
     → über `npm install`
   - Alle pip-Abhängigkeiten (für den Keylogger)  
     → über `pip3 install pynput pyobjc`
  

🚀 Nutzung  
- **Starte den Browser mit Keylogger:**

  Im Terminal:

  ```bash
  chmod +x start_all.sh
  ./start_all.sh
  ```

🔒 Die Tastatur- und Mauseingaben werden lokal gespeichert und am Ende der Sitzung zur Überprüfung angezeigt. Erst nach manueller Bestätigung werden die Daten anonym an den zentralen Server übertragen.

📄 Hinweise  
- **Fenster für Keylogger und Prozesse werden automatisch minimiert.**

- **Beim Schließen des Browsers** wird der Keylogger automatisch beendet.

- **Es werden keine persönlichen Daten gespeichert.**

❓ Häufige Probleme  

| Problem                          | Lösung                                                                 |
|----------------------------------|------------------------------------------------------------------------|
| `python3` wird nicht erkannt     | Stelle sicher, dass Python installiert ist und im PATH verfügbar ist   |
| `node` oder `npm` fehlen         | Installiere Node.js z. B. mit `brew install node`                      |
| Fenster bleiben offen            | Stelle sicher, dass nur diese Version des Browsers verwendet wird.    |
| Keylogger wird nicht beendet     | Starte `start_all.sh` nicht mehrfach. Nur ein Fenster gleichzeitig nutzen |
