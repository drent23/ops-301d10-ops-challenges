# Import AD 'library'
Import-Module ActiveDirectory

# Create new AD user 'Franz Ferdinand'
New-ADUser -SamAccountName "fferdinand" -Name "FranzFerdinand" -OtherAttributes @{'city'="Springfield";'department'="TPS";'mail'+"ferdi@GlobeXpower.com";'state'="OR";'title'="TPS Reporting Lead"}

# Create new Group
New-ADGroup -SamAccountName ReportingLeads =Name "Reporting Leads" -Description "Reporting Leads for TPS Department" -DisplayName "Reporting Leads" -GroupCategory 1 -GroupScope 1 -DisplayName "TPS Reporting Leads"

# Create new OU
New-ADOrganizationalUnit -Name "TPS" -Description "TPS Department" -DisplayName "TPS Department" -Path "DC=GLOBEXPOWER,DC=COM" -ProtectedFromAccidentalDeletion 1