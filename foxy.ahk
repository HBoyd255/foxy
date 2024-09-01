; Local paths to the python executable and the script.
PythonPath := "pythonw.exe"
ScripePath := "main.py"

; Get the directory of the this script.
DirectoryLocation = %A_ScriptDir%\

; Get the full path of the script.
FullScriptPath := DirectoryLocation . ScriptPath

args := ""
Loop, %0% ; For each parameter,
{
    ; Append the parameter to the list.
    param := %A_Index%
    args .= param . " "
}

command := PythonPath . " " . FullScriptPath . " " . args

run %command%

