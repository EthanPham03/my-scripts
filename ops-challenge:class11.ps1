Enable-NetFirewallRule -DisplayGroup "File and Printer Sharing"

New-NetFirewallRule -DisplayName "Allow ICMPv4-In" -Protocol ICMPv4 -ImcpType 8 -Enabled True

Enable-PSRemoting -Force 

Get-AppxPackage -AllUsers | Where-Object { $_.bloatware -like "bloatware" } | Remove-AppxPackage

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
Set-SmbClientConfiguration -EnableSMB1Protocol $false -Force
