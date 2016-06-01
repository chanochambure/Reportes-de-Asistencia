Option Explicit
Dim objShell, objDesktop, objLinkuno, objLinkdos
Dim strAppPathuno,strAppPathdos, strWorkDir, strIconPath, dirPath

dirPath = Replace(WScript.ScriptFullName, WScript.ScriptName, "")
strWorkDir = dirPath
strAppPathuno = dirPath+"exeAdmin.vbs"
strAppPathdos = dirPath+"exeReportes.vbs"
strIconPath = dirPath+"Software.ico"

Set objShell = CreateObject("WScript.Shell")
objDesktop = objShell.SpecialFolders("Desktop")
Set objLinkuno = objShell.CreateShortcut(objDesktop & "\RdA - Administrador.lnk")
Set objLinkdos = objShell.CreateShortcut(objDesktop & "\RdA - Reportes.lnk")

objLinkuno.IconLocation = strIconPath
objLinkuno.TargetPath = strAppPathuno
objLinkuno.WindowStyle = 3
objLinkuno.WorkingDirectory = strWorkDir
objLinkuno.Save

objLinkdos.IconLocation = strIconPath
objLinkdos.TargetPath = strAppPathdos
objLinkdos.WindowStyle = 3
objLinkdos.WorkingDirectory = strWorkDir
objLinkdos.Save

WScript.Quit