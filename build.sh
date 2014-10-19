sudo apt-get install python-pip

sudo pip install virtualenvwrapper

echo "export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'" >> ~/.bashrc

echo "[[ -f /usr/local/bin/virtualenvwrapper.sh ]] && source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

source ~/.bashrc

mkvirtualenv cloudops

cd cloudops

pip install -r requirements.pip

python manage.py syncdb

python manage.py migrate


gunicorn --env DJANGO_SETTINGS_MODULE=cloudops.settings cloudops.wsgi -b :8000 -w 8


