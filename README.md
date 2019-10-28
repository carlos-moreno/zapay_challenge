# Desafio Zapay

API para consumo de informações sobre lançamentos da SpaceX

[![Build Status](https://travis-ci.org/carlos-moreno/zapay_challenge.svg?branch=master)](https://travis-ci.org/carlos-moreno/zapay_challenge)
[![Maintainability](https://api.codeclimate.com/v1/badges/44bd056d8e5e5a99b310/maintainability)](https://codeclimate.com/github/carlos-moreno/zapay_challenge/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/44bd056d8e5e5a99b310/test_coverage)](https://codeclimate.com/github/carlos-moreno/zapay_challenge/test_coverage)

O projeto foi desenvolvido utilizando a linguagem de programação Python e o Django Rest Framework para construção da API.

Foram criados 4 endpoints para apresentar os dados solicitados, sendo eles:
 - /v1/next ***(endpoint responsável por trazer informação referente ao próximo lançamento)***
 - /v1/latest ***(endpoint responsável por trazer infromação referente ao último lançamento)***
 - /v1/upcoming ***(endpoint responsável por trazer informações referentes aos próximos lançamentos)***
 - /v1/past ***(endpoint responsável por trazer informações referentes aos últimos lançamentos)***
 
Caso nenhum endpoint acima seja informado, a API irá utilizar o endpoint / para trazer informações de todos os lançamentos da SpaceX, tanto efetuados quanto os que estão agendados para acontecer.

O projeto busca seguir algumas recomendações da metodologia [doze-fatores](https://12factor.net/pt_br/), como por exemplo:
 - Base de código
 - Declaração de dependêcias
 - Configurações 
 
Para integração contínua é utilizado o travis-ci, onde o mesmo roda os testes da aplicação, envia o relatório de cobertura de testes e qualidade do código para o code climate e por fim realiza o deploy no heroku. 
 
Para ver o projeto em execução, [clique aqui!](https://carlos-moreno-spacex-api.herokuapp.com/)  

## Rodando o projeto na sua máquina

***Pré-requisitos:***

 - Git
 - Python 3
 
***Passos a serem executados:***
 
1. Clone o repositório
2. Crie um virtualenv com Python 3
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute o migrate
7. Execute o collectstatic
8. Execute os testes
9. Coloque o projeto em execução

```console
git clone https://github.com/carlos-moreno/zapay_challenge.git api
cd api
python -m venv .api
source .api/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py migrate
python manage.py collectstatic
python manage.py test
python manage.py runserver
```

## Rodando o projeto usando Docker e Docker-Compose

***Pré-requisitos:***

 - Docker
 - Docker-Compose
 
***Passo a ser executado:***
 
1. docker-compose up

```console
docker-compose up
```

###### Os Passos listados acima foram testados em uma máquina com o sistema Linux Mint

#### ***Pontos a serem concluídos:***
 - / ***(Falta realizar o tratamento das querystrings)***
 - /v1/upcoming ***(Falta realizar o tratamento das querystrings)***
 - /v1/past ***(Falta realizar o tratamento das querystrings)***
 - Front-End (Foi solicitado a criação de um front-end feito em React para consumo da API, devido a inexperiência com o mesmo não foi possível atender esse ponto)

#### ***Para a instalação dos pré-requisitos veja:***

 - [Instalação do Git](https://git-scm.com/book/pt-br/v1/Primeiros-passos-Instalando-Git)
 - [Instalação do Python no Linux](https://docs.python.org/3.7/using/unix.html)
 - [Instalação do Python no Windows](https://docs.python.org/3.7/using/windows.html)
 - [Instalação do Docker](https://docs.docker.com/install/)
 - [Instalação do Docker-Compose](https://docs.docker.com/compose/install/)
 


