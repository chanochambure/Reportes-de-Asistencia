On Error Resume Next

Dim geekside,nret

Set geekside=WScript.CreateObject("WScript.Shell")

nret=geekside.Run("C:/Python27/pythonw.exe SoftwareAdmin.py",1,TRUE)