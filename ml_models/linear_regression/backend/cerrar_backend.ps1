$ErrorActionPreference = 'Stop'
$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$estado = Join-Path $raiz '.venv\regresion-backend.json'

if (!(Test-Path -LiteralPath $estado)) {
    Write-Output 'No hay una instancia iniciada por el script.'
    return
}

$registro = Get-Content -Raw -LiteralPath $estado | ConvertFrom-Json
$servidor = Get-Process -Id $registro.Id -ErrorAction SilentlyContinue
if ($servidor -and "$($servidor.StartTime.ToUniversalTime().Ticks)" -eq $registro.Inicio) {
    # En Windows el Python de .venv puede lanzar otro proceso para ejecutar Uvicorn.
    & taskkill.exe /PID $servidor.Id /T /F | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'No se pudo cerrar el backend.' }
}
Remove-Item -LiteralPath $estado
Write-Output 'Backend cerrado.'
