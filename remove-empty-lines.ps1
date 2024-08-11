# Bulunduğunuz dizindeki tüm JSON dosyalarını alır
$jsonFiles =  get-childitem -recurse .\ -exclude "*.py","launch.json" -Filter *.json #Get-ChildItem -recurse -Path .\ -Filter *.json

foreach ($file in $jsonFiles) {
    
    Get-Content $file | Where-Object { $_ -ne "" } | Set-Content $file

}
