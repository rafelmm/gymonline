# gymonline

Para empezar a desarrollar hay que crear el entorno siguiendo los siguientes pasos:

1. Instalar python3

2. Instalar virtualenv: 

	$ [sudo] pip install virtualenv
	
3. Crear los entornos de desarrollo, test y producción:

	$ virtualenv devenv
	$ virtualenv testenv
	$ virtualenv prodenv
	
4. Instalar los paquetes necesarios en cada entorno:
	NOTA: Si se produce un error al instalar psycopg2 ejecutar el siguiente comando:
	$ sudo apt-get install libpq-dev python3-dev

	$ source devenv/bin/activate
	$ (devenv) pip install -r requirements/common.txt
	$ (devenv) pip install -r requirements/dev.txt
	$ deactivate
	
	$ source testenv/bin/activate
	$ (devenv) pip install -r requirements/common.txt
	$ (devenv) pip install -r requirements/test.txt
	$ deactivate

	$ source prodenv/bin/activate
	$ (devenv) pip install -r requirements/common.txt
	$ (devenv) pip install -r requirements/prod.txt
	$ deactivate
	
5. Modificar el fichero devenv/bin/activate y añadir las siguientes líneas. Hacer lo mismo para el entorno de test:

	DJANGO_SETTINGS_MODULE="gymonline.development_settings"
	export DJANGO_SETTINGS_MODULE


Para desarrollar activaremos el entorno de desarrollo: 

	$ source devenv/bin/activate

Podemos usar Eclipse para desarrollar. Para ello deberemos seguir los siguientes pasos:

1. Instalar Eclipse y el paquete PyDev
2. Configurar el interprete de Python en Window->Preferences. Debemos seleccionar el interprete ubicado en devenv/bin/
3. Importar el proyecto


BASE DE DATOS

	Usuario: root
	Password: root

Crear una base de datos llamada gymonline, otra gymonlinedev y otra gymonlinetest
Para ello abrir una consola:

	$ mysql -u root -p
	[introducir password: root]

	mysql> create database gymonline character set utf8;
	mysql> create database gymonlinedev character set utf8;
	mysql> create database gymonlinetest character set utf8;
	mysql> exit;


CREAR TABLAS PARA LA APLICACIÓN
Abrimos consola y vamos al directorio del proyecto donde esta el fichero manage.py

	$ python manage.py check
	$ python manage.py makemigrations
	$ python manage.py migrate

Con esto se crearan las tablas en la base de datos


INICIAR SERVIDOR
Abrimos consola y vamos al directorio del proyecto donde esta el fichero manage.py

	$ python manage.py runserver


TRADUCIR TEXTOS
1. Crear ficheros de textos

	$ python manage.py makemessages -l ca
	$ python manage.py makemessages -l es

2. Traducir todos los textos del fichero locale/ca/LC_MESSAGES/django.po

3. Compilar los ficheros de textos

	$ python manage.py compilemessages -l ca
	$ python manage.py compilemessages -l es
	
	
	
