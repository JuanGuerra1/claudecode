#!/bin/bash
# Script super simple para descargar videos

echo "🎬 DESCARGADOR DE VIDEOS - UNIVERSIDAD ONLINE"
echo "=============================================="
echo ""

# Verificar si yt-dlp está instalado
if ! command -v yt-dlp &> /dev/null
then
    echo "📦 Instalando yt-dlp..."
    pip install yt-dlp
    echo "✅ yt-dlp instalado"
else
    echo "✅ yt-dlp ya está instalado"
fi

echo ""
echo "📥 Descargando videos de live.universidad.online..."
echo ""

# Crear carpeta para videos
mkdir -p videos_descargados

# Descargar videos
yt-dlp "https://live.universidad.online/" -o "videos_descargados/%(title)s.%(ext)s"

echo ""
echo "✅ ¡Descarga completada!"
echo "📁 Los videos están en: videos_descargados/"
