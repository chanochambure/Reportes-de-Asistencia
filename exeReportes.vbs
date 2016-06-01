On Error Resume Next

Dim geekside,nret

Set geekside=WScript.CreateObject("WScript.Shell")

nret=geekside.Run("pythondw.exe SoftwareReportes.pywc",1,TRUE)