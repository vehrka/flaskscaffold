========================
Aplicación mínima Flask
========================

:titulo: Aplicación mínima Flask
:version: v0.0
:autor: pferrer
:fecha: 2015-06-03

Introducción
============

Ejemplo de aplicación mínima (scaffold) de Flask

Archivos
========

Archivos de la aplicación::

    ├── app
    │   ├── __init__.py
    │   ├── main
    │   │   ├── __init__.py
    │   │   └── views.py
    │   └── templates
    │       ├── base.html
    │       └── index.html
    ├── config.py
    ├── features
    │   ├── environment.py
    │   ├── min.feature
    │   └── steps
    │       └── min_steps.py
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
:features/environment.py: Archivo de entorno de test con Behave
:features/min.feature: Definición de escenarios
:features/steps/min_steps.py: Pasos para la definición min
:manage.py: Herramienta de gestión de la aplicación
:README.rst: Este mismo archivo
:requirements/common.txt: Archivo con los requisitos del virtualenv
:requirements/dev.txt: Archivo con los requisitos de desarrollo para el virtualenv
