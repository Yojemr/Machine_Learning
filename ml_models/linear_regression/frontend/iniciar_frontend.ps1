$ErrorActionPreference = 'Stop'
$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$python = Join-Path $raiz '.venv\Scripts\python.exe'
& $python -B (Join-Path $PSScriptRoot 'manage.py') runserver 127.0.0.1:8001
exit $LASTEXITCODE
