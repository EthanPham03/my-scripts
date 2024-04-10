Import-Module ActiveDirectory

$firstName = "Franz"
$lastName = "Ferdinand"
$username = "Ferdi"
$password = "GlobeX123"
$email = "ferdi@GlobeXpower.com"
$ou = "OU=Users,OU=Springfield,OU=Oregon"

$splat = @{
    GivenName = $firstName
    Surname = $lastName
    SamAccountName = $username
    AccountPassword = $password
    Enable = $true
    EmailAddress = $email
    Path = $ou
}

New-ADUser @splat

Add-ADGroupMember -Identity "TPS Department" -Members $username