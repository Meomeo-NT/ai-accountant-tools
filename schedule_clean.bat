@echo off
chcp 65001 >nul

:: ============================================
:: CHECK DISK - SCHEDULED CLEAN
:: File nay dung de lap lich voi Task Scheduler
:: Khong can tuong tac, chay ngam hoan toan
:: ============================================

set "GOROOT=D:\CODE\SOFT\go1.26.3.windows-amd64\go"
set REPORT_DIR=%USERPROFILE%\Desktop\clean_reports

:: Tao thu muc bao cao neu chua co
if not exist "%REPORT_DIR%" mkdir "%REPORT_DIR%"

:: Ten file bao cao: clean_YYYYMMDD_HHMMSS.txt
set REPORT_FILE=%REPORT_DIR%\clean_%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%.txt
set REPORT_FILE=%REPORT_FILE: =0%

:: Bien dich lai neu file .exe chua ton tai hoac cu hon .go
if not exist "%~dp0checkdisk.exe" (
    "%GOROOT%\bin\go" build -o "%~dp0checkdisk.exe" "%~dp0checkdisk.go" >nul 2>&1
) else (
    for %%a in ("%~dp0checkdisk.go") do set GO_FILE_DATE=%%~ta
    for %%a in ("%~dp0checkdisk.exe") do set EXE_FILE_DATE=%%~ta
    if "%GO_FILE_DATE%" GTR "%EXE_FILE_DATE%" (
        "%GOROOT%\bin\go" build -o "%~dp0checkdisk.exe" "%~dp0checkdisk.go" >nul 2>&1
    )
)

:: Chay FULL mode (quet truoc -> don -> quet sau)
"%~dp0checkdisk.exe" -mode full -top 15 -out "%REPORT_FILE%" >nul 2>&1

:: Ghi log thoi gian chay
echo [%DATE% %TIME%] Clean completed: %REPORT_FILE% >> "%~dp0clean_schedule.log"