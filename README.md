# 🎥 Descargador de Videos Testimoniales

Script Python para descargar videos testimoniales de https://live.universidad.online/ usando `yt-dlp`.

## 📋 Requisitos Previos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

### 1. Clonar o descargar este repositorio

```bash
git clone <url-del-repositorio>
cd claudecode
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

O instalar directamente:

```bash
pip install yt-dlp
```

## 💻 Uso

### Opción 1: Descargar TODOS los videos de la página (Recomendado)

```bash
python descargar_videos.py
```

Esto descargará todos los videos encontrados en https://live.universidad.online/ y los guardará en la carpeta `videos_descargados/`.

### Opción 2: Descargar un video específico

```bash
# Desde un embed de VideoPress
python descargar_videos.py --url "https://videopress.com/embed/EOhUTbBF"

# Desde un archivo MP4 directo
python descargar_videos.py --url "https://videos.files.wordpress.com/EOhUTbBF/nani_mp4_dvd.mp4"
```

### Opción 3: Guardar en una carpeta personalizada

```bash
python descargar_videos.py --carpeta mis_testimoniales
```

### Opción 4: URL personalizada + carpeta personalizada

```bash
python descargar_videos.py --url "https://videopress.com/embed/EOhUTbBF" --carpeta videos_juan
```

## 📁 Estructura de Archivos

```
claudecode/
├── descargar_videos.py      # Script principal
├── requirements.txt          # Dependencias
├── README.md                 # Este archivo
└── videos_descargados/       # Carpeta con los videos (se crea automáticamente)
    ├── video1.mp4
    ├── video2.mp4
    └── ...
```

## 🎯 Características

- ✅ Descarga automática de la mejor calidad disponible
- ✅ Combina audio y video automáticamente en formato MP4
- ✅ Descarga múltiples videos de una página
- ✅ Guarda miniaturas de los videos
- ✅ Nombres de archivo basados en el título del video
- ✅ Manejo de errores y continuación en caso de fallos
- ✅ Interfaz de línea de comandos fácil de usar

## 📖 Ejemplos de Uso Avanzado

### Descargar solo usando yt-dlp directamente

Si prefieres usar `yt-dlp` directamente desde la terminal:

```bash
# Descargar un video específico
yt-dlp "https://videopress.com/embed/EOhUTbBF"

# Descargar todos los videos de la página
yt-dlp "https://live.universidad.online/"

# Descargar con formato específico
yt-dlp -f "bestvideo+bestaudio" "https://videopress.com/embed/EOhUTbBF"
```

## 🔧 Solución de Problemas

### Error: "yt-dlp no está instalado"

```bash
pip install --upgrade yt-dlp
```

### Error: "Permission denied"

En Linux/Mac, dale permisos de ejecución al script:

```bash
chmod +x descargar_videos.py
./descargar_videos.py
```

### Los videos no se descargan

1. Verifica tu conexión a internet
2. Asegúrate de que la URL sea correcta
3. Intenta actualizar yt-dlp: `pip install --upgrade yt-dlp`

## 📝 Notas

- Los videos se descargan en la mejor calidad disponible
- El formato de salida por defecto es MP4
- El script crea automáticamente la carpeta de destino si no existe
- Se incluyen las miniaturas de los videos

## 🤝 Contribuciones

Si encuentras algún problema o tienes sugerencias, no dudes en crear un issue o pull request.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y comercial.

## 🌟 Créditos

- Utiliza [yt-dlp](https://github.com/yt-dlp/yt-dlp) como motor de descarga
- Desarrollado para facilitar la descarga de videos testimoniales de live.universidad.online

---

**¡Feliz descarga! 🎬**
