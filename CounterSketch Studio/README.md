# CounterSketch Automated installer

This application will allow you to automagically install CounterSketch and login with provided login/serial credentials.

## Installation & Requirements
- Python3
- Pip3
- Rhinoceros 5 x64-bit -- [link](https://github.com/Signet-sd/STS-Projects-and-Innovation/tree/main/Foundry/Rhino%205)
  
---

```
invoke-webrequest -Uri "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe" -OutFile "C:\temp\python-3.9.6-amd64.exe"
Start -Wait -FilePath "C:\temp\python-3.9.6-amd64.exe"
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
py -m pip install pyautogui
py -m pip install opencv-python
```

Set User Access Control(UAC) to 0:
```
Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name ConsentPromptBehaviorAdmin -Value 0
```

---

Linux:
```
N/A
```

---

