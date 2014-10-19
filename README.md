
### Como executar o cloudOps

Se já utiliza virtualenv ou não quer usar pode pular essa parte

#### Passo 1 - Instalar e configurar virtualenv

``` $ sudo apt-get install python-pip ```

sudo pip install virtualenvwrapper

```$ echo "export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'" >> ~/.bashrc ou ~/.zshrc ```

```$ echo "[[ -f /usr/local/bin/virtualenvwrapper.sh ]] && source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc ou ~/.zshrc ```

```$ source ~/.bashrc ```

ou para quem usa ZSH

```$ source ~/.zshrc ```

```$ mkvirtualenv cloudops ```

#### Passo 2 - Instalar dependencias

```$ git clone git@github.com:jesuejunior/cloudops.git ```

cd cloudops

```$ pip install -r requirements.pip ```

#### Passo 3 - Fazendo sync do banco de dados e criando seu super usuário

```$ python manage.py syncdb ```

```$ python manage.py migrate ```

#### Passo 4 - Executando a aplicação com gunicorn ou servidor de desenvolvimento do django

###### Primeira opção

```$ gunicorn --env DJANGO_SETTINGS_MODULE=cloudops.settings cloudops.wsgi -b :8000 -w 8 ```

###### Segunda opção

```$ python manage.py runserver ```

#### Para executar os testes

```$ py.test ```

#### Opção rapida?

* Clone o repositório, entre no diretório e execute ```$ bash build.sh```