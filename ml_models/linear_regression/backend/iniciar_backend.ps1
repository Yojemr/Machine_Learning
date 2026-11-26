$ErrorActionPreference = 'Stop'
$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$entorno = Join-Path $raiz '.venv'
$python = Join-Path $entorno 'Scripts\python.exe'
$estado = Join-Path $entorno 'regresion-backend.json'

if (!(Test-Path -LiteralPath $python)) {
    throw 'No se encontro el Python del entorno .venv del proyecto.'
}
if (Test-Path -LiteralPath $estado) {
    $registro = Get-Content -Raw -LiteralPath $estado | ConvertFrom-Json
    $activo = Get-Process -Id $registro.Id -ErrorAction SilentlyContinue
    if ($activo -and "$($activo.StartTime.ToUniversalTime().Ticks)" -eq $registro.Inicio) {
        Write-Output 'El backend ya esta iniciado. Swagger: http://127.0.0.1:8000/docs'
        return
    }
}
if (Get-NetTCPConnection -State Listen -LocalPort 8000 -ErrorAction SilentlyContinue) {
    throw 'El puerto 8000 esta ocupado. Cierra la instancia anterior desde donde fue iniciada.'
}

$servidor = Start-Process -FilePath $python -ArgumentList @('-B', '-m', 'uvicorn', 'main:app', '--host', '127.0.0.1', '--port', '8000') `
    -WorkingDirectory $PSScriptRoot -WindowStyle Hidden -PassThru `
    -RedirectStandardOutput (Join-Path $entorno 'regresion-backend.log') `
    -RedirectStandardError (Join-Path $entorno 'regresion-backend-error.log')
@{Id = $servidor.Id; Inicio = "$($servidor.StartTime.ToUniversalTime().Ticks)"} |
    ConvertTo-Json | Set-Content -LiteralPath $estado

for ($intento = 0; $intento -lt 20; $intento++) {
    try {
        Invoke-RestMethod 'http://127.0.0.1:8000/modelo' -TimeoutSec 1 | Out-Null
        Write-Output 'Backend listo. Swagger: http://127.0.0.1:8000/docs'
        return
    } catch {
        if ($servidor.HasExited) { break }
        Start-Sleep -Milliseconds 500
    }
}
throw "El backend no respondio. Revisa el registro: $entorno\regresion-backend-error.log"
