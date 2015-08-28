import contextlib

from fabric.api import *


env.hosts = ['cyl',]
env.use_ssh_config = True


server_project_dirs = {
    'prod': '/home/cyl/alley',
}

server_virtualenvs = {
    'prod': 'alley',
}

supervisord_programs = {
    'prod': 'alley',
}

supervisord_conf = '/etc/supervisor/supervisord.conf'


@contextlib.contextmanager
def cdversion(version, subdir=''):
    """cd to the version indicated"""
    with prefix('cd %s' % '/'.join([server_project_dirs[version], subdir])):
        yield


@contextlib.contextmanager
def workon(version):
    """workon the version of indicated"""
    with prefix('workon %s' % server_virtualenvs[version]):
        yield


@task
def pull(version='prod'):
    with cdversion(version):
        run('git pull --no-edit')


@task
def install_requirements(version='prod'):
    with workon(version):
        with cdversion(version):
            run('pip install -r requirements/base.txt')
            run('pip install -r requirements/production.txt')


@task
def build_static(version='prod'):
    with workon(version):
        run('django-admin collectstatic --noinput')


@task
def syncdb(version='prod'):
    with workon(version):
        run('django-admin syncdb')


@task
def restart_django(version='prod'):
    with workon(version):
        sudo('supervisorctl -c %s restart %s' % (
            supervisord_conf,
            supervisord_programs[version]
        ))


@task
def deploy():
    pull()
    install_requirements()
    syncdb()
    build_static()
    restart_django()
