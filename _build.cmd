@echo off
set PATH=D:\TUANNA01\SOFT\node-v24.13.0-win-x64;%SystemRoot%\system32
set NODE_OPTIONS=--max-old-space-size=768
cd /d D:\Code\ai-accountant-tools
node node_modules\next\dist\bin\next build