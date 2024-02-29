Get-WinEvent -LogName System -StartTime (Get-Date).AddHours(-24) | Out-File -FilePath "last_24.txt" 

Get-WinEvent -LogName System -ErrorLevel 2 | Out-File -FilePath "error.txt"

Get-WinEvent -LogName System -FilterHashtable @{Id=16} | Format-Table

Get-WinEvent -LogName System -Newest 20 | Format-Table

Get-WinEvent -LogName System -Newest 500 | Select-Object -Property TimeCreated, ProviderName, Id, Message | Format-Table