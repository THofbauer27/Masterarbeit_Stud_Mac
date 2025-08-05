#!/bin/bash

echo "🍎 Setup-Skript für macOS gestartet..."

# Prüfe, ob pip3 installiert ist
if ! command -v pip3 &> /dev/null
then
    echo "❌ pip3 ist nicht installiert. Bitte installiere es zuerst mit: brew install python3"
    exit 1
fi

# Erstelle virtual environment (optional, empfehlenswert)
if [ ! -d "venv" ]; then
    echo "🐍 Erstelle Python Virtual Environment..."
    python3 -m venv venv
fi

# Aktiviere virtual environment
source venv/bin/activate

# Installiere Python-Abhängigkeiten
echo "📦 Installiere Python-Dependencies (pyobjc, pynput)..."
pip3 install --upgrade pip
pip3 install pyobjc pynput

# Optional: requirements.txt schreiben
echo "pyobjc" > requirements.txt
echo "pynput" >> requirements.txt

# Installiere Node.js-Dependencies
if [ -f "package.json" ]; then
    echo "📦 Installiere Node.js-Dependencies..."
    npm install
else
    echo "⚠️ Keine package.json gefunden, überspringe npm install."
fi

echo "✅ Setup abgeschlossen! Du kannst jetzt starten mit:"
echo "   ./start_all.sh"

# Deaktiviere virtual environment
deactivate
