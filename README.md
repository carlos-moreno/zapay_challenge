# Desafio Zapay

API para consumo de informações sobre lançamentos da SpaceX

## Rodando o projeto na sua máquina

1. Clone o repositório
2. Crie um virtualenv com Python 3
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute o makemigrations para verificar alterações no model (técnicamente não é para ter modificação)
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

