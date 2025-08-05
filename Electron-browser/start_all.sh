#!/bin/bash

echo "🐍 Prüfe Python3-Pfad..."
PYTHON_PATH=$(which python3)
echo "✅ Gefundener Python3-Pfad: $PYTHON_PATH"

if [ -z "$PYTHON_PATH" ]; then
    echo "❌ python3 wurde nicht gefunden! Bitte installiere es zuerst (z. B. mit brew install python3)."
    exit 1
fi

echo "🐍 Starte Python-Keylogger im Hintergrund (Logs: keylogger.log)..."
$PYTHON_PATH keylogger.py > keylogger.log 2>&1 &
KEYLOGGER_PID=$1
echo "✅ Keylogger PID: $KEYLOGGER_PID"

echo "⚡ Starte Electron-App..."
npm start

echo "❌ Electron wurde beendet. Stoppe Keylogger ..."

if ps -p $KEYLOGGER_PID > /dev/null; then
    echo "✅ Keylogger-Prozess läuft noch, beende jetzt..."
    kill $KEYLOGGER_PID
    echo "✅ Keylogger wurde gestoppt."
else
    echo "⚠️ Keylogger-Prozess lief nicht mehr."
fi

echo "✅ Alles gestoppt. Fertig!"

