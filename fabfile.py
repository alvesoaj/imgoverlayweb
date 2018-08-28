from fabric.api import env, run, prefix
from fabric.contrib.project import rsync_project
from fabric.contrib.files import exists

# server user
env.user = 'root'
# server ip
env.hosts = [open('./host.txt', 'rt').read()]

def deploy():
    # Create a directory on a remote server, if it doesn't already exists
    if not exists('/home/deploy/apps'):
        run('mkdir -p apps')

    if not exists('/home/deploy/apps/imgoverlayweb'):
        run('cd /home/deploy/apps && mkdir -p imgoverlayweb')

    rsync_project(local_dir='./', remote_dir='/home/deploy/apps/imgoverlayweb',
        exclude=['.git'])

    with prefix('cd /home/deploy/apps/imgoverlayweb'):
        if not exists('env'):
            run('virtualenv -p python3 env')

        with prefix('source env/bin/activate'):
            run('pip3 install fabric3')

            if not exists('/etc/supervisor/conf.d/imgoverlayweb.conf'):
                run('cp supervisor.conf /etc/supervisor/conf.d/imgoverlayweb.conf')

                run('supervisorctl reread')

            run('service supervisor restart')
