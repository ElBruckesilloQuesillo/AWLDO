# GENERALES
    1. Carpeta views: Esta carpeta contiene todas las vistas html del sitio.
        Asegurarse colocar la siguiente nomenclatura para un mejor entendimiento:
        "VistaView", ejemplo: 
            ComprasView, NosotrosView, ContactoView, ...

        1.1. Carpeta Components: Esta carpeta aloja 3 archivos html:
            1. Index: Este archivo contendrá el contenido de cualquier vista.
            2. Footer: Footer del sitio
            3. NavBar: NavBar del sitio
            Estos 3 archivos nos ayudan a reciclar código, son los componentes que
            más se repiten en cada vista y sólo hace falta un llamado para evitar redundancia.
            Esto ya se hace de manera automática.
    
    2. Archivo settings.py: Incluye la configuración del proyecto. Es recomendable que los cambios
        que se realicen en este archivo sean sólo de manera local.

    3. Archivo urls.py: Incluye un directorio de las url del sitio.

    4. Archivo views.py: Incluye sólo métodos para la carga y renderizado de vistas html.

# SOLUCIONAR ERROR DE CARGA DE VISTAS
    1. Abrir archivo settings.py
    2. Buscar variable 'TEMPLATES'
    3. En el parámetro 'DIRS' colocar la URL de alojamiento de la carpeta views.
    
        Ejemplo: 'DIRS': ['C:/xampp/htdocs/django/LineaDeOro/lineaDeOro/views']

    Es importante no actualizar este archivo en git porque puede generar errores al ser
    rutas diferentes.

# COMANDOS QUE CREO QUE MÁS USAREMOS

# //Iniciar servidor
py manage.py runserver

# //Inicia un repositorio vacio
git init

# //Clona un repositorio de github
git clone

# //Añade archivos al area de preparación
git add nombrearchivo.extension

# //Añade archivos a la base de git
git commit -m "Se hizo tal cambio"

# //Envia los cambios a GitHub
git push

# //Trae los cambios a Git local
git pull




