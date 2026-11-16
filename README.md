# Aventuras del Sur: sistema de reservas del ecoparque

Aplicación web en **Django** para el Ecoparque y Reserva Natural "Aventuras del Sur".
Sirve para administrar el catálogo de experiencias (trekking, canopy, kayak, arriendo de equipos), las inscripciones de los visitantes y el acceso según el rol del usuario.

Evaluación Sumativa N°3, Programación Back End.

## Tecnologías

| Parte | Herramienta |
|---|---|
| Backend | Python 3 + Django (vistas basadas en funciones, ORM, ModelForm) |
| Base de datos | MySQL 8 conectado con **PyMySQL** |
| Panel privado | Plantilla **SB Admin 2** (Bootstrap 4 + Font Awesome) |
| Listados | **DataTables** (búsqueda en tiempo real, paginación y orden) en español |
| Sesiones | `django.contrib.sessions` + `django.contrib.auth` (`login`, `logout`, `request.session`) |

## Estructura del proyecto

```
inventarioAventura/          <- carpeta raíz (repositorio)
├── manage.py
├── requirements.txt
├── inventarioAventura/      <- proyecto principal (settings.py, urls.py)
├── core/                    <- landing pública y panel de control
├── cuentas/                 <- Perfil (rol), login/logout, registro, CRUD de usuarios
│   └── management/commands/poblar_datos.py   <- carga los datos de prueba
├── experiencias/            <- Categoria, Experiencia, Inscripcion (reservas)
├── templates/               <- plantillas HTML (base.html = layout SB Admin 2)
├── static/                  <- CSS/JS de SB Admin 2, DataTables, jQuery
└── respaldo_bd/inventarioAventura.sql   <- respaldo MySQL (estructura + datos)
```

## Modelos (models.py)

- **Perfil** (`cuentas`): relación `OneToOneField` con el `User` de Django. Guarda el `rol` (ADMIN, GUIA o TURISTA) y el teléfono.
- **Categoria**: nombre, descripción y estado `activo`.
- **Experiencia**: título, descripción, precio, cupo máximo, fecha/hora, `activa`, categoría (`ForeignKey`) y creador (`ForeignKey` a `User`).
- **Inscripcion**: tabla intermedia entre `User` y `Experiencia`. Guarda la fecha de inscripción y el estado de pago (Pendiente o Confirmado). Tiene una restricción única (usuario + experiencia) para no reservar dos veces lo mismo.

## Roles y permisos

Al iniciar sesión, el rol se guarda en `request.session['rol']`. Cada vista revisa ese rol antes de ejecutarse (y `@login_required` exige sesión iniciada).

| Funcionalidad | Administrador | Guía / Operador | Turista |
|---|---|---|---|
| Usuarios (CRUD) | ✅ Completo | ❌ | ❌ |
| Categorías (CRUD) | ✅ Completo | ❌ | ❌ |
| Experiencias | ✅ CRUD de todas | Crear, ver y editar **solo las suyas** (`filter(creador=request.user)`), sin eliminar | Solo ve el catálogo de experiencias activas |
| Inscritos de una experiencia | ✅ Todas | ✅ Solo de sus experiencias | ❌ |
| Reservas | ✅ Ve todas, cambia estado y elimina | ❌ | Reserva, paga y cancela **sus** reservas |
| Django Admin (`/admin/`) | ✅ | ❌ | ❌ |

## Instalación

```bash
# 1. Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate          # Windows: .\venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Crear la base de datos en MySQL (Workbench o consola)
#    CREATE DATABASE inventarioAventura CHARACTER SET utf8mb4;
#    Ajustar USER y PASSWORD en inventarioAventura/settings.py

# 4. Opción A: crear las tablas y cargar los datos de prueba
python manage.py migrate
python manage.py poblar_datos

#    Opción B: restaurar el respaldo incluido
mysql -u root -p < respaldo_bd/inventarioAventura.sql

# 5. Levantar el servidor
python manage.py runserver
```

Luego abre <http://127.0.0.1:8000/>.

## Credenciales de prueba

Todos los usuarios de prueba usan la misma contraseña: **`Aventura2026`**

| Rol | Usuario | Nombre | Datos asociados |
|---|---|---|---|
| Administrador | `admin` | Ana Administradora | Superusuario, también entra a `/admin/` |
| Guía | `guia1` | Camila Rojas | 4 experiencias |
| Guía | `guia2` | Matías Fuentes | 4 experiencias |
| Turista | `turista1` | Sofía Pérez | 3 reservas |
| Turista | `turista2` | Benjamín Soto | 3 reservas |

Las cuentas nuevas creadas desde "Crear cuenta" quedan siempre con rol **Turista**.

## Rutas principales

| URL | Qué hace | Quién entra |
|---|---|---|
| `/` | Landing pública | Todos |
| `/cuentas/login/`, `/cuentas/registro/` | Iniciar sesión y crear cuenta | Todos |
| `/panel/` | Panel de control (cambia según el rol) | Con sesión |
| `/cuentas/usuarios/` | CRUD de usuarios | Admin |
| `/experiencias/categorias/` | CRUD de categorías | Admin |
| `/experiencias/gestion/` | Gestión de experiencias | Admin y guía |
| `/experiencias/catalogo/` | Catálogo de actividades | Con sesión |
| `/experiencias/mis-reservas/` | Reservas propias | Turista |
| `/experiencias/reservas/` | Todas las reservas | Admin |
| `/admin/` | Django Admin | Admin |
