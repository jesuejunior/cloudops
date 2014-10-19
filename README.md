
### Como executar o cloudOps

* _Testado no Ubuntu 12.04/14.04 caso use outra distribuição faça as devidas alterações._

Se já utiliza virtualenv ou não quer usar pode pular essa parte

#### Passo 1 - Instalar e configurar virtualenv

``` $ sudo apt-get install python-pip ```

```$ sudo pip install virtualenvwrapper ```

```$ echo "export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'" >> ~/.bashrc ou ~/.zshrc ```

```$ echo "[[ -f /usr/local/bin/virtualenvwrapper.sh ]] && source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc ou ~/.zshrc ```

```$ source ~/.bashrc ```

ou para quem usa ZSH

```$ source ~/.zshrc ```

```$ mkvirtualenv cloudops ```

#### Passo 2 - Fazer o clone do repositório e instalar dependências

```$ git clone git@github.com:jesuejunior/cloudops.git ```

``` cd cloudops ```

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

#### Documentação completa de todos os endpoints

* Abra o seguinte endereço http://127.0.0.1:8000/docs

### Exemplos de uso

#### Efetuando login

* Request

```$ curl -H "Content-Type: application/json"  -X POST --data '{"username": "admin", "password": "admin"}' http://127.0.0.1:8000/auth ```

* Response

```$ {"token": "c7feffe7728cce3384bcce0b1d34bb81d9ad9a51"} ```

#### Fazendo request na API

* Request no endpoint para listar servidores /servers

```$ curl -H "Content-Type: application/json" -H "Authorization: Token c7feffe7728cce3384bcce0b1d34bb81d9ad9a51" -X GET http://127.0.0.1:8000/servers ```

* Response

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "cloudops",
            "ipaddress": "192.18.121.23",
            "system_operational": "Ubuntu",
            "applications": []
        },
        {
            "id": 2,
            "name": "cloudops",
            "ipaddress": "192.18.121.213",
            "system_operational": "Ubuntu",
            "applications": []
        }
    ]
}
```



###TO-DO

- [ ] - Implementar API para registro de usuários
- [ ] - Implementar permissionamento com grupos/usuários
- [ ] - Corrigir bug de cadastrar applicações que ainda não existem para servidores


# Duvidas??? Mail me!

jesuesousa@gmail.com
