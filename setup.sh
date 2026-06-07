#!/bin/bash

# WalrOS Crypter - Setup Script
# By: Alpha / Zo

echo "═══════════════════════════════════════════════════════════════"
echo "  🦭 WalrOS Crypter v6.0 - Installation Script"
echo "═══════════════════════════════════════════════════════════════"

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
   echo "[!] Don't run as root, use sudo for specific commands"
fi

echo ""
echo "[1/4] Updating package list..."
sudo apt update

echo ""
echo "[2/4] Installing dependencies..."
sudo apt install -y mono-complete openssl osslsigncode python3 python3-pip

echo ""
echo "[3/4] Installing Python packages..."
pip3 install --upgrade pip
pip3 install cryptography pycryptodome

echo ""
echo "[4/4] Verifying installations..."

# Check mono
if command -v mcs &> /dev/null; then
    echo "    ✅ Mono: $(mcs --version | head -1)"
else
    echo "    ❌ Mono: Not found"
fi

# Check openssl
if command -v openssl &> /dev/null; then
    echo "    ✅ OpenSSL: $(openssl version)"
else
    echo "    ❌ OpenSSL: Not found"
fi

# Check Python
if command -v python3 &> /dev/null; then
    echo "    ✅ Python: $(python3 --version)"
else
    echo "    ❌ Python: Not found"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  ✅ Installation complete!"
echo "  🚀 Run: python3 walros_crypter.py"
echo "═══════════════════════════════════════════════════════════════"