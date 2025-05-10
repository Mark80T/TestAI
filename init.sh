#!/bin/bash

echo "[INFO] Installazione ODBC..."
apt-get update
apt-get install -y unixodbc unixodbc-dev libodbc1

echo "[INFO] Creazione symlink libodbc.so.2..."
ln -sf /usr/lib/x86_64-linux-gnu/libodbc.so.2 /usr/lib/libodbc.so.2

echo "[INFO] Aggiornamento linker..."
ldconfig

echo "[INFO] Avvio backend Python..."
exec python main.py
