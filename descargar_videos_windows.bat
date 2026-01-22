@echo off
chcp 65001 >nul
echo ============================================
echo   DESCARGADOR DE VIDEOS - UNIVERSIDAD ONLINE
echo ============================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python no está instalado
    echo.
    echo Por favor instala Python desde: https://www.python.org/downloads/
    echo Asegúrate de marcar "Add Python to PATH" durante la instalación
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

REM Instalar yt-dlp
echo 📦 Instalando yt-dlp...
pip install yt-dlp
echo.

REM Crear carpeta para videos
if not exist "videos_descargados" mkdir videos_descargados
echo 📁 Carpeta 'videos_descargados' lista
echo.

REM Descargar videos
echo 📥 Descargando videos de live.universidad.online...
echo.
yt-dlp "https://live.universidad.online/" -o "videos_descargados/%%(title)s.%%(ext)s"

echo.
echo ============================================
echo ✅ ¡Descarga completada!
echo 📁 Los videos están en: videos_descargados\
echo ============================================
echo.
pause
