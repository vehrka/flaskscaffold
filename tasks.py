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


@task
def version_bump(ctx, major=False, minor=False, patch=False, version=''):

    """Makes the version bump in the required files"""

    import semver

    f = open("VERSION", "r")
    fversion = f.readline().strip('\n')
    f.close()

    if version:
        nversion = version
    else:
        version = fversion

        if major:
            nversion = semver.bump_major(version)
        elif minor:
            nversion = semver.bump_minor(version)
        elif patch:
            nversion = semver.bump_patch(version)
        else:
            print("No version change")

    print("Old version {} New version {}".format(fversion, nversion))

    ctx.run("sed -i -e 's/:version: .*/:version: {}/' README.rst".format(nversion))

    f = open("VERSION", "w")
    f.write(nversion)
    f.close()
