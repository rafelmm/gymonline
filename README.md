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
	$ source devenv/bin/activate
	$ (devenv) pip install -r requirements/dev.txt
	$ deactivate
	
	$ source testenv/bin/activate
	$ (devenv) pip install -r requirements/test.txt
	$ deactivate

	$ source prodenv/bin/activate
	$ (devenv) pip install -r requirements/prod.txt
	$ deactivate

Para desarrollar activaremos el entorno de desarrollo: 
	$ source devenv/bin/activate


