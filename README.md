# Desafio Zapay

API para consumo de informações sobre lançamentos da SpaceX

## Rodando o projeto na sua máquina

Pré-requisitos para rodar localmente

 - Git
 - Python 3
 
1. Clone o repositório
2. Crie um virtualenv com Python 3
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute o makemigrations
7. Execute o migrate
8. Execute os testes
9. Coloque o projeto em execução

```console
git clone https://github.com/carlos-moreno/zapay_challenge.git api
cd api
python -m venv .api
source .api/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
```

## Rodando o projeto usando Docker e Docker-Compose

Pré-requisitos:

 - Docker
 - Docker-Compose
 
1. docker-compose up

```console
docker-compose up
```

###### Os Passos listados acima foram testados em máquina linux

