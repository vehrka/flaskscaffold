========================
Aplicación mínima Flask
========================

:titulo: Aplicación mínima Flask
:version: v1.1
:autor: pferrer
:fecha: 2015-06-25


Introducción
============

Ejemplo de aplicación mínima (scaffold) de Flask


Archivos
========

Archivos de la aplicación::


    .
    ├── app
    │   ├── __init__.py
    │   ├── main
    │   │   ├── __init__.py
    │   │   └── views.py
    │   └── templates
    │       ├── base.html
    │       └── index.html
    ├── config.py
    ├── EXPORTME_example.cfg
    ├── fabfile.py
    ├── features
    │   ├── 01_min.feature
    │   ├── environment.py
    │   └── steps
    │       └── 01_min_steps.py
    ├── manage.py
    ├── README.rst
    └── requirements
        ├── common.txt
        └── dev.txt


:app/__init__.py: Inicialización del paquete principal
:app/main/__init__.py: Inicialización del componente main
:app/main/views.py: Vistas del componente main
:app/templates/base.html: Plantilla Base
:app/templates/index.html: Plantilla del index.html
:config.py: Configuraciones de la aplicación
:EXPORTME_example.cfg: Ejemplo de configuración por archivo de variables de entorno
:fabfile.py: Archivo de comandos de Fabric
:features/01_min.feature: Definición de escenarios
:features/environment.py: Archivo de entorno de test con Behave
:features/steps/01_min_steps.py: Pasos para la definición min
:manage.py: Herramienta de gestión de la aplicación
:README.rst: Este mismo archivo
:requirements/common.txt: Archivo con los requisitos del virtualenv
:requirements/dev.txt: Archivo con los requisitos de desarrollo para el virtualenv
