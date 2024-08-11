# Bulunduğunuz dizindeki tüm JSON dosyalarını alır
$jsonFiles =  get-childitem -recurse .\ -exclude "*.py","launch.json" -Filter *.json #Get-ChildItem -recurse -Path .\ -Filter *.json

foreach ($file in $jsonFiles) {
    
    # JSON dosyasının içeriğini okur
    $content = Get-Content -Path $file.FullName -Raw
    # "\n" stringini siler
    $updatedContent = $content -replace '\[\d+\]',''
    # Güncellenmiş içeriği tekrar dosyaya yazar
    Set-Content -Path $file.FullName -Value $updatedContent -NoNewLine
}
