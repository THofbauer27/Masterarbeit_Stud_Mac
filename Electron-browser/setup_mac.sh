{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww29740\viewh15980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #!/bin/bash\
\
echo "\uc0\u55356 \u57166  Setup-Skript f\'fcr macOS gestartet..."\
\
# Pr\'fcfe, ob pip3 installiert ist\
if ! command -v pip3 &> /dev/null\
then\
    echo "\uc0\u10060  pip3 ist nicht installiert. Bitte installiere es zuerst mit: brew install python3"\
    exit 1\
fi\
\
# Erstelle virtual environment (optional, empfehlenswert)\
if [ ! -d "venv" ]; then\
    echo "\uc0\u55357 \u56333  Erstelle Python Virtual Environment..."\
    python3 -m venv venv\
fi\
\
# Aktiviere virtual environment\
source venv/bin/activate\
\
# Installiere Python-Abh\'e4ngigkeiten\
echo "\uc0\u55357 \u56550  Installiere Python-Dependencies (pyobjc, pynput)..."\
pip3 install --upgrade pip\
pip3 install pyobjc pynput\
\
# Optional: requirements.txt schreiben\
echo "pyobjc" > requirements.txt\
echo "pynput" >> requirements.txt\
\
# Installiere Node.js-Dependencies\
if [ -f "package.json" ]; then\
    echo "\uc0\u55357 \u56550  Installiere Node.js-Dependencies..."\
    npm install\
else\
    echo "\uc0\u9888 \u65039  Keine package.json gefunden, \'fcberspringe npm install."\
fi\
\
echo "\uc0\u9989  Setup abgeschlossen! Du kannst jetzt starten mit:"\
echo "   ./start_all.sh"\
\
# Deaktiviere virtual environment\
deactivate\
}