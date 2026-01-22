#!/usr/bin/env python3
"""
Script para descargar videos testimoniales de live.universidad.online
Usa yt-dlp para descargar videos de alta calidad con audio incluido.
"""

import argparse
import sys
import os
from datetime import datetime

try:
    import yt_dlp
except ImportError:
    print("❌ Error: yt-dlp no está instalado.")
    print("Por favor, ejecuta: pip install yt-dlp")
    sys.exit(1)


def descargar_video(url, carpeta_destino="videos_descargados"):
    """
    Descarga un video usando yt-dlp con la mejor calidad disponible.

    Args:
        url: URL del video o página a descargar
        carpeta_destino: Carpeta donde se guardarán los videos
    """
    # Crear carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f"📁 Carpeta '{carpeta_destino}' creada.")

    # Configuración de yt-dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Mejor calidad de video y audio
        'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),  # Plantilla para nombres
        'merge_output_format': 'mp4',  # Combinar en formato MP4
        'quiet': False,  # Mostrar progreso
        'no_warnings': False,
        'extract_flat': False,  # Descargar todos los videos de una página
        'ignoreerrors': True,  # Continuar si hay errores en algunos videos
        'writethumbnail': True,  # Guardar miniatura
        'writesubtitles': False,
        'writeautomaticsub': False,
    }

    try:
        print(f"\n🎬 Descargando desde: {url}")
        print(f"📂 Guardando en: {carpeta_destino}")
        print("=" * 60)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            # Mostrar información sobre lo descargado
            if info:
                if 'entries' in info:
                    # Es una playlist o página con múltiples videos
                    total = len([e for e in info['entries'] if e is not None])
                    print(f"\n✅ Se descargaron {total} videos correctamente.")
                else:
                    # Es un solo video
                    print(f"\n✅ Video descargado: {info.get('title', 'Desconocido')}")

        print(f"\n🎉 Descarga completada. Archivos guardados en: {os.path.abspath(carpeta_destino)}")
        return True

    except Exception as e:
        print(f"\n❌ Error durante la descarga: {str(e)}")
        return False


def main():
    """Función principal del script."""
    parser = argparse.ArgumentParser(
        description='Descargador de videos testimoniales de live.universidad.online',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Descargar todos los videos de la página principal
  python descargar_videos.py

  # Descargar un video específico
  python descargar_videos.py --url "https://videopress.com/embed/EOhUTbBF"

  # Descargar a una carpeta específica
  python descargar_videos.py --carpeta mis_testimoniales

  # Descargar desde un archivo MP4 directo
  python descargar_videos.py --url "https://videos.files.wordpress.com/EOhUTbBF/nani_mp4_dvd.mp4"
        """
    )

    parser.add_argument(
        '--url',
        type=str,
        default='https://live.universidad.online/',
        help='URL del video o página a descargar (por defecto: live.universidad.online)'
    )

    parser.add_argument(
        '--carpeta',
        type=str,
        default='videos_descargados',
        help='Carpeta donde guardar los videos (por defecto: videos_descargados)'
    )

    args = parser.parse_args()

    print("=" * 60)
    print("🎥 DESCARGADOR DE VIDEOS TESTIMONIALES")
    print("=" * 60)
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Descargar videos
    exito = descargar_video(args.url, args.carpeta)

    if exito:
        print("\n✨ Proceso completado exitosamente.")
        sys.exit(0)
    else:
        print("\n⚠️  El proceso terminó con errores.")
        sys.exit(1)


if __name__ == "__main__":
    main()
