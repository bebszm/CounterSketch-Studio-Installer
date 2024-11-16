$CounterSketchExec = "C:\temp\CounterSketch\src\exe\CounterSketch.exe"
$CounterSketchPath = "C:\Program Files\CounterSketch Studio\CounterSketch Studio.exe"

# Install CounterSketch
Start-Process -Wait -FilePath $CounterSketchExec -Argument "/silent" -PassThru

# Start CounterSketch
start-process -filepath $CounterSketchPath

Start-Sleep -Seconds 10

# Start python script
py C:\temp\CounterSketch\src\Countersketch_login.py
