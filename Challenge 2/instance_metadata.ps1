$filter_data = $args[0]
Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -Uri "http://169.254.169.254/metadata/instance${filter_data}?api-version=2021-02-01" | ConvertTo-Json -Depth 64