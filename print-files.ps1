# Bulunduğunuz dizindeki tüm JSON dosyalarını alır
$jsonFiles = Get-ChildItem -recurse .\ -exclude *.py -Filter *.json

foreach ($file in $jsonFiles) {
    # Dosya içeriğini okur
    $content = Get-Content -Path $file.FullName -Raw
    
    # Eğer içerikte \n stringi varsa, dosya adını konsola yazdırır
    if ($content -match "\\n") {
        Write-Host $file.FullName
    }
}
