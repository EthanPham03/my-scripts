Get-Process | Sort-Object -Property CPU -Descending | Format-Table -Property ProcessName, CPU -AutoSize

Get-Process | Sort-Object -Property Id -Descending | Format-Table -Property ProcessName, Id

Get-Process | Sort-Object - Property WorkingSet -Descending | Select-Object -First 5 | Format-Table -Property ProcessName, WorkingSet -AutoSize

Start-Process "msedge.exe" -ArgumentList "https://owasp.org/www-project-top-ten/"

for ($i = 1; $i -le 10; $i++) {
    Start-Process "notepad.exe"
}

$notepadProcesses = Get-Process -Name "notepad"
foreach ($process in $notepadProcesses) {
    Stop-Process -Id $process.Id -Force
}

Stop-Process -Id (Get-Process -Name "msedge").Id -Force
