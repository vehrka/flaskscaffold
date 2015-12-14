#!/usr/bin/env python
# −*− coding: UTF−8 −*−

from invoke import ctask as task
import os

DIR = os.path.abspath(os.path.dirname(__file__))


@task
def test(ctx):
    """Runs the unittests"""
    ctx.run('python manage.py test')


@task
def rundev(ctx):
    """Sets the dev environment and launches the app"""
    exportcfg = os.path.join(DIR, 'EXPORTME.cfg')
    appconf = {'APP_CONFIG': exportcfg, 'FLASK_CONFIG': 'development'}
    os.environ.update(appconf)
    apprun(ctx)


@task
def shelldev(ctx):
    """Sets the dev environment and launches the shell"""
    exportcfg = os.path.join(DIR, 'EXPORTME.cfg')
    appconf = {'APP_CONFIG': exportcfg, 'FLASK_CONFIG': 'development'}
    os.environ.update(appconf)
    shellrun(ctx)


def apprun(ctx):
    ctx.run('python manage.py runserver')


def shellrun(ctx):
    ctx.run('python manage.py shell')
