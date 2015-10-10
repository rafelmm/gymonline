Quick Start Guide
=================
 
Secret Django Key
-----------------
 
This boilerplate has the **DJANGO_KEY** setting variable hidden. 
 
You can generate your DJANGO_KEY |django_key|.
 
.. |django_key| raw:: html
    
    <a href="http://www.miniwebtool.com/django-secret-key-generator"
    target="_blank">here</a>
 
  
Virtual environments and Settings Files
---------------------------------------

First, you must check that libqp-dev, python3-dev and libmysqlclient-dev are installed::
	
	$ sudo apt-get install libpq-dev python3-dev libmysqlclient-dev

First, you must install virtualenv for python3::
 
    $ pip3 install virtualenv
 
Next, create a Development virtual environment with Python 3 installed::
 
    $ virtualenv tb_dev
 
Go to the virtual enviornment folder with::
 
    $ cd $VIRTUAL_ENV/bin
 
and edit the activate file.:
 
    $ vi activate
 
You must add the lines: ::
 
    export DJANGO_SETTINGS_MODULE="gymonline.development_settings"
 
 
Repeat the last steps for your testing environment::
 
    $ virtualenv tb_test
    $ cd $VIRTUAL_ENV/bin
    $ vi activate
 
where you have to add the lines::
 
    export DJANGO_SETTINGS_MODULE="gymonline.test_settings"
 
Next, install the packages in each environment::
 
    $ source tb_dev/bin/activate
    $ (tb_dev) pip install -r requirements/dev.txt
    $ source tb_test/bin/activate
    $ pip install -r requirements/test.txt
 

Base de datos
-------------

Instalación
***********

Tenemos que instalar mysql::
	
	$ sudo apt-get install mysql-server

Cración de la base de datos
***************************

Crear una base de datos llamada gymonline, otra gymonlinedev y otra gymonlinetest
Para ello abrir una consola y introducir el siguiente comando::

	$ mysql -u root -p
	
Nos preguntará la contraseña del usuario, la introducimos. A continuación ejecutamos los siguientes comandos::

	mysql> create database gymonline character set utf8;
	mysql> create database gymonlinedev character set utf8;
	mysql> create database gymonlinetest character set utf8;
	mysql> exit;


Crear tablas para la aplicación
*******************************

Abrimos consola y vamos al directorio del proyecto donde esta el fichero manage.py::

	$ python manage.py check
	$ python manage.py migrate


Con esto se crearan las tablas en la base de datos

 
Internationalization and Localization
-------------------------------------
 
Settings
********
 
The default language for this Project is **English**, and we use internatinalization to translate the text into Spanish and Catalan.
 
If you want to change the translation language, or include a new one, you just need to modify the **LANGUAGES** variable in the file *settings.py*. The language codes that define each language can be found |codes_link|.
 
.. |codes_link| raw:: html
 
    <a href="http://msdn.microsoft.com/en-us/library/ms533052(v=vs.85).aspx" target="_blank">here</a>
 
For example, if you want to use German you should include::
 
    LANGUAGES = (
        ...
        'de', _("German"),
        ...
    )
 
You can also specify a dialect, like Luxembourg's German with::
 
    LANGUAGES = (
        ...
        'de-lu', _("Luxemburg's German"),
        ...
    )
 
Note: the name inside the translation function _("") is the language name in the default language (English).
 
More information on the |internationalization_post|. 
 
.. |internationalization_post| raw:: html
 
    <a href="http://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones" target="_blank">TaskBuster post</a>
 
 
Translation
***********
 
Go to the terminal, inside the gymonline_project folder and create the files to translate with::
 
    $ python manage.py makemessages -l ca
 
change the language "ca" for your selected language.
 
Next, go to the locale folder of your language::
 
    $ cd taskbuster/locale/ca/LC_MESSAGES
 
where taskbuster is your project folder. You have to edit the file *django.po* and translate the strings. You can find more information about how to translate the strings |translation_strings_post|.
 
.. |translation_strings_post| raw:: html
 
    <a href="http://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones#inter-translation" target="_blank">here</a>
 
Once the translation is done, compile your messages with::
 
    $ python manage.py compilemessages -l ca
 
 
 
Tests
*****
 
We need to update the languages in our Tests to make sure the translation works correclty. Open the file *functional_tests/test_all_users.py*:
 
- in **test_internationalization**, update your languages with the translation of title text, here "Welcome to TuGymOnline!"
- in **test_localization**, update your languages.
 

Apache
------

First we need to install the Apache Web Server::
	
	$ sudo apt-get install apache2 apache2-threaded-dev
	
Then we have to install mod_wsgi and setuptools::

	$ sudo apt-get install python-setuptools libapache2-mod-wsgi-py3
 
Next restart the apache server::

	$ sudo service apache2 restart
	

Useful commands
---------------
 
A list of all the commands used to run this template::
 
    $ activate tb_dev
 
    $ python manage.py makemessages -l ca
    $ python manage.py compilemessages -l ca
    
    $ python manage.py runserver
    
Useful links
------------

https://www.digitalocean.com/community/tutorials/how-to-set-up-an-apache-mysql-and-python-lamp-server-without-frameworks-on-ubuntu-14-04
