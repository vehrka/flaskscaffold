#!/usr/bin/env python
# −*− coding: UTF−8 −*−

from fabric.api import local, prefix, task
import os

DIR = os.path.abspath(os.path.dirname(__file__))


@task
def test():
    """Runs the unittests"""
    local('python manage.py test')


@task
def rundev():
    """Sets the dev environment and launches the app"""
    exportcfg = os.path.join(DIR, 'EXPORTME.cfg')
    with prefix('export APP_CONFIG={}'.format(exportcfg)):
        apprun()


@task
def shelldev():
    """Sets the dev environment and launches the shell"""
    exportcfg = os.path.join(DIR, 'EXPORTME.cfg')
    with prefix('export APP_CONFIG={}'.format(exportcfg)):
        shellrun()


def apprun():
    local('python manage.py runserver')


def shellrun():
    local('python manage.py shell')
