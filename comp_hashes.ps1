param(
    [Parameter(Mandatory=$true)]
    [string]$fichero1,

    [Parameter(Mandatory=$true)]
    [string]$fichero2,
 
    [string]$algoritmo
)

if (!$algoritmo) {
    $algoritmo = Read-Host "Introduce el algoritmo (MD5, SHA1, SHA256, SHA512) [SHA256]"
}

if (!$algoritmo) {
    $algoritmo = "SHA256"
}


if (!(Test-Path -LiteralPath $fichero1 -PathType Leaf) -or
    !(Test-Path -LiteralPath $fichero2 -PathType Leaf)) {
    Write-Host "Error: uno o ambos ficheros no existen."
    exit 1
}

if ($algoritmo -notin @("MD5", "SHA1", "SHA256", "SHA512")) {
    Write-Host "Error: algoritmo no valido."
    exit 1
}

Write-Host "Calculando hashes usando el algoritmo $algoritmo..."

try {
    $hash1 = (Get-FileHash -LiteralPath $fichero1 -Algorithm $algoritmo -ErrorAction Stop).Hash.ToLower()
    $hash2 = (Get-FileHash -LiteralPath $fichero2 -Algorithm $algoritmo -ErrorAction Stop).Hash.ToLower()
}
catch {
    Write-Host "Error al calcular los hashes: $_"
    exit 1
}

Write-Host "${fichero1}: $hash1"
Write-Host "${fichero2}: $hash2"

if ($hash1 -eq $hash2) {
    Write-Host "Los hashes son IGUALES."
} else {
    Write-Host "Los hashes son DIFERENTES."
}
