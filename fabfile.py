from fabric.api import task
from fabric.api import cd
from fabric.api import env
from fabric.api import run

from ade25.fabfiles import project


env.use_ssh_config = True
env.forward_agent = True
env.port = '22222'
env.user = 'root'
env.hosts = ['z13']
env.webserver = '/opt/webserver/buildout.webserver'
env.code_root = '/opt/sites/agita/buildout.agita'
env.local_root = '/Users/sd/dev/agita/buildout.agita'
env.sitename = 'agita'
env.code_user = 'root'
env.prod_user = 'www'


@task
def deploy():
    """ Deploy current master to production server """
    project.site.update()
    project.site.restart()


@task
def deploy_full():
    """ Deploy current master to production and run buildout """
    project.site.update()
    project.site.build()
    project.site.restart()


@task
def rebuild():
    """ Deploy current master and run full buildout """
    project.site.update()
    project.site.build_full()
    project.site.restart()


@task
def develop(*cmd):
    """Runs arbitrary mr.developer bin/develop command."""
    with cd(env.code_root):
        run('nice bin/develop ' + ' '.join(cmd))


@task
def get_data():
    """ Copy live database for local development """
    project.db.download_data()
