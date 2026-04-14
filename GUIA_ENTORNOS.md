# 🖥️ Guía de Entornos de Claude Code

Claude Code te permite trabajar desde diferentes entornos según dónde se encuentre tu código y cómo quieras ejecutarlo. Esta guía explica cada una de las opciones que aparecen en el selector de entornos.

## 📋 Resumen rápido

| Entorno | Ideal para | Dónde corre Claude |
|---|---|---|
| **Local** | Desarrollo en tu propia máquina | Tu computadora |
| **Agregar conexión SSH** | Servidores remotos propios | Servidor remoto vía SSH |
| **Control remoto** | Controlar otra máquina desde la web | Máquina remota registrada |
| **Entornos en la nube** | Trabajo sin configuración local | Sandbox en la nube de Anthropic |

---

## 💻 1. Local

Ejecuta Claude Code directamente en tu máquina, usando los archivos de la carpeta que selecciones.

### Cuándo usarlo
- Ya tienes el proyecto clonado en tu computadora.
- Necesitas acceso a tus herramientas locales (Docker, bases de datos, variables de entorno, etc.).
- Quieres latencia mínima al editar archivos.

### Cómo usarlo
1. Haz clic en **Seleccionar carpeta** y elige el directorio del proyecto.
2. Asegúrate de que el selector de entorno (abajo a la derecha) muestre **Local**.
3. Escribe tu petición (por ejemplo: *"Find a small todo in the codebase and do it"*) y envíala.

### Requisitos
- Tener Claude Code instalado localmente (`npm install -g @anthropic-ai/claude-code` o la app de escritorio).
- Permisos de lectura/escritura sobre la carpeta elegida.

---

## 🔐 2. Agregar conexión SSH

Conecta Claude Code a un servidor remoto al que accedas por SSH. El código vive en el servidor; Claude ejecuta comandos allí.

### Cuándo usarlo
- El proyecto está en un servidor de desarrollo, VM o workstation remota.
- Necesitas más recursos (CPU, GPU, RAM) de los que tienes en tu máquina.
- Quieres mantener el entorno de desarrollo centralizado.

### Cómo configurarlo
1. En el selector de entorno, elige **+ Agregar conexión SSH**.
2. Introduce los datos de conexión:
   - **Host** (p. ej. `dev.miempresa.com` o `192.168.1.50`)
   - **Usuario** (p. ej. `juan`)
   - **Puerto** (por defecto `22`)
   - **Clave SSH** o contraseña
3. Selecciona la carpeta del proyecto *dentro* del servidor remoto.

### Requisitos
- Acceso SSH funcional desde tu equipo al servidor (prueba primero con `ssh usuario@host`).
- Claude Code instalado en el servidor remoto, o permitir que el cliente lo instale.

### Consejos
- Usa claves SSH en lugar de contraseñas para mayor seguridad.
- Si usas un *jump host*, configúralo en tu `~/.ssh/config` antes de añadirlo aquí.

---

## 📡 3. Control remoto — "Agregar control remoto"

Permite que Claude Code (por ejemplo desde la web o desde otro dispositivo) controle una máquina tuya donde ya corre un agente de Claude Code.

### Cuándo usarlo
- Quieres iniciar tareas desde el móvil o el navegador mientras tu computadora principal hace el trabajo pesado.
- Necesitas retomar una sesión desde otro dispositivo.
- Trabajas en equipo y quieres compartir acceso a un entorno concreto.

### Cómo configurarlo
1. En la máquina que actuará como "host", inicia Claude Code y habilita el modo de control remoto (Settings → Remote control).
2. Copia el código o token de emparejamiento que aparece.
3. En el cliente, elige **+ Agregar control remoto** y pega el token.
4. La máquina registrada aparecerá en el desplegable y podrás seleccionarla.

### Requisitos
- Claude Code corriendo y autenticado en la máquina host.
- Red accesible (no requiere abrir puertos; usa el servicio de relay de Anthropic).

---

## ☁️ 4. Entornos en la nube (Default)

Entornos sandbox alojados por Anthropic. Claude clona tu repositorio de GitHub dentro de un contenedor temporal y trabaja allí.

### Cuándo usarlos
- No quieres instalar nada localmente.
- Quieres aislar tareas en entornos efímeros (útil para experimentos, refactors, PRs automáticas).
- Trabajas desde la versión web de Claude Code (`claude.ai/code`).

### Cómo usarlos
1. En el selector de entorno, elige uno de los **Default** bajo *Entornos en la nube*.
2. Vincula tu cuenta de GitHub si es la primera vez.
3. Selecciona el repositorio y la rama sobre los que trabajar.
4. Envía tu petición. Claude creará una rama, hará los cambios y podrá abrir un PR.

### Requisitos
- Repositorio accesible desde la integración de GitHub de Claude.
- Opcional: un archivo de configuración de SessionStart hook para preparar el entorno (instalar dependencias, compilar, etc.).

### Notas
- Cada entorno *Default* corresponde a una plantilla preconfigurada (Node, Python, etc.). Si necesitas herramientas específicas, añade un hook de inicio al repositorio.
- Los entornos en la nube son efímeros: no guardes datos sensibles sin commitearlos o exportarlos.

---

## ❓ ¿Cuál elegir?

- **Solo quiero probar algo rápido sin instalar nada** → *Entornos en la nube*.
- **Estoy trabajando en mi laptop con mi IDE** → *Local*.
- **Mi proyecto está en un servidor remoto potente** → *Conexión SSH*.
- **Quiero lanzar tareas desde el móvil mientras mi PC trabaja** → *Control remoto*.

---

## 🔧 Solución de problemas

### "No se puede conectar por SSH"
- Verifica con `ssh usuario@host` desde tu terminal.
- Revisa que la clave privada esté cargada (`ssh-add -l`).

### "El entorno en la nube no ve mi repo"
- Autoriza la app de GitHub de Claude para la organización o repo.
- Confirma que la rama existe y no está protegida contra cambios de bots.

### "El control remoto no aparece"
- Asegúrate de que la máquina host esté encendida y con Claude Code abierto.
- Vuelve a generar el token si ha caducado.

---

**Consejo final:** puedes cambiar de entorno en cualquier momento usando el desplegable inferior derecho (**Local ▾** en la captura). El prompt que escribas se ejecutará en el entorno seleccionado en ese momento.
