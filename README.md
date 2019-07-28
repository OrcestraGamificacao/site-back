# Backend do Projeto

Projeto base para a API do site, feita em Flask.

## Rodando o Projeto

Primeiramente vamos subir o banco de dados que vamos usar:

na pasta do projeto digite o seguinte comando:

```bash
$ docker-compose up -d db
```

Isso vai subir o banco de dados em segundo plano

Para instalar as dependências do projeto é recomendável utilizar uma virtualenv, para isolar o ambiente.

```bash
$ virtualenv .env -p python3
```
E não se esqueça de ativar a virtualenv

```bash
$ source .env/bin/activate
```

Agora vamos instalar as dependências e o projeto:

```bash
$ pip install -r requirements.txt
$ pip install -e .
```

Após isso precisamos rodar as migrações para preparar o banco

```bash
$ alembic upgrade head
```

E podemos então rodar o projeto

```bash
$ flask run
```

O projeto estará rodando na porta `5000`

Obs: Lembre-se de ao fazer alterações no código, reiniciar o servidor.

## Gerando novas migrações

A ferramenta que está sendo usada para gerenciar as migrações é o alembic.
Para gerar novas migrações bastar o rodar o comando:

`$ alembic revision --autogenerate -m "Message"`

A flag `autogenerate` diz ao alembic para gerar a migração a partir das mudanças encontradas nos arquivos de models