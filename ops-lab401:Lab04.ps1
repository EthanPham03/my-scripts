secedit.exe /export /cfg "$env:TEMP\temp.cfg"
((Get-Content "$env:TEMP\temp.cfg") -replace "PasswordComplexity = 0", "PasswordComplexity = 1") | Set-Content "$env:TEMP\temp.cfg"
secedit.exe /configure /db %windir%\securitynew.sdb /cfg "$env:TEMP\temp.cfg" /areas SECURITYPOLICY
gpupdate /force
Remove-Item "$env:TEMP\temp.cfg"

Set-SmbClientConfiguration -EnableSMB1Protocol $false -Force
