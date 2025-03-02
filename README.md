# GLOBAL_PULSE

**GLOBAL_PULSE** es un proyecto diseñado para ofrecer de forma sencilla e intuitiva la información y los datos relevantes de todo lo que se necesita saber para aprovechar el funcionamiento de infoproductos y PLRs. Este monorepositorio alberga múltiples aplicaciones y paquetes que trabajan en conjunto para Vender rápido y sin tener que contar con suerte, porque ya tienes todo validado de la mano: Anuncios, Creativos, Segmentación, Páginas y Videos de Venta.

## 📌 Tabla de Contenidos

1. [📂 Estructura del Proyecto](#-estructura-del-proyecto)
2. [⚙️ Instalación](#️-instalación)
   - [📥 Clonar el repositorio](#clonar-el-repositorio)
   - [🔧 Configurar el entorno](#configurar-el-entorno)
   - [🚀 Construir y levantar los servicios](#construir-y-levantar-los-servicios)
3. [🚀 Uso](#-uso)
4. [🛠️ Contribución](#️-contribución)
5. [📜 Licencia](#-licencia)

---

## 📂 Estructura del Proyecto

La estructura del monorepositorio es la siguiente:

```bash
GLOBAL_PULSE/
├── apps/
│   ├── backend/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   ├── frontend/
│   │   ├── package.json
│   │   ├── pnpm-lock.yaml
│   │   └── Dockerfile
├── docker-compose.yml
└── README.md
```

- apps/backend/: Contiene la aplicación backend desarrollada con Flask.
- apps/frontend/: Contiene la aplicación frontend desarrollada con Next.js.
- docker-compose.yml: Archivo para orquestar los servicios Docker del proyecto.
- README.md: Este archivo de documentación.

# ⚙️ Instalación

Para poner en marcha el proyecto en un entorno local, sigue estos pasos:

## Clonar el repositorio

```bash
git clone https://github.com/MiguelT18/GLOBAL_PULSE.git
cd GLOBAL_PULSE
```

## Configurar el entorno

Asegúrate de tener Docker y Docker Compose instalados en tu sistema. Puedes verificar las instalaciones con:

```bash
docker --version
docker-compose --version
```

## Construir y levantar los servicios

Utiliza Docker Compose para construir y levantar los servicios:

```bash
sudo docker compose up --build -d
```

sudo docker compose up --build -d

---

# 🚀 Uso

Una vez que los servicios estén en funcionamiento:

- **Frontend:** Accede a la aplicación frontend en http://localhost:3000.
- **Backend:** Backend: La API del backend estará disponible en http://localhost:5000.

---

# 🛠️ Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir al proyecto, sigue estos pasos:

1. **Fork** el repositorio.
2. Crea una nueva rama para tu funcionalidad o corrección de errores:

```bash
sudo docker compose up --build -d
```

3. Realiza tus cambios y haz commits descriptivos.
4. Envía un Pull Request detallando los cambios realizados.

# 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más información.
