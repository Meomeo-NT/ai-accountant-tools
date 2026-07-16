@echo off
chcp 65001 >nul
title CHECK DISK - Dọn dẹp toàn diện
color 0A

echo ============================================
echo   CHECK DISK - DON DEP TOAN DIEN
echo   (c) 2026 - Chay 1 lan la xong
echo ============================================
echo.
echo 📋 Chuong trinh se:
echo   1. Quet 5 thu muc lon nhat o C:\
echo   2. Quet 5 thu muc lon nhat trong %USERPROFILE%
echo   3. Quet 5 thu muc lon nhat o E:\
echo   4. Xoa cac cache an toan (Temp, npm, pip, Rust, ...)
echo   5. Quet lai de so sanh ket qua
echo   6. Xuat bao cao ra file results_YYYYMMDD.txt
echo.
echo ⚠️  DONG VS CODE TRUOC KHI CHAY!
echo.
pause
echo.

:: Tao ten file bao cao
set REPORT_FILE=%USERPROFILE%\Desktop\clean_report_%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%.txt
echo Bao cao don dep > "%REPORT_FILE%"

:: Hien thi log ra man hinh va ghi vao file cung luc
set "GOROOT=D:\CODE\SOFT\go1.26.3.windows-amd64\go"

echo ⏳ Dang biet dich chuong trinh...
"%GOROOT%\bin\go" build -o checkdisk.exe checkdisk.go 2>nul

echo ⏳ Dang quet va don dep... (co the mat vai phut)
echo.
echo ============================================ >> "%REPORT_FILE%"
echo CHECK DISK - BAO CAO DON DEP >> "%REPORT_FILE%"
echo Ngay: %DATE% %TIME% >> "%REPORT_FILE%"
echo ============================================ >> "%REPORT_FILE%"
echo. >> "%REPORT_FILE%"

:: Chay FULL mode - quet truoc, don, quet sau
checkdisk.exe -mode full -top 15 -out "%REPORT_FILE%"

echo.
echo ============================================
echo   ✅ DON DEP HOAN TAT!
echo   Bao cao duoc luu tai:
echo   %REPORT_FILE%
echo ============================================
echo.
pause