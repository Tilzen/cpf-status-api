# API Situação Cadastral CPF
CPFs para testes:
- 40442820135
- 63017285995
- 91708635203
- 58136053391
- 40532176871
- 47123586964
- 07691852312
- 10975384600
- 01648527949
- 47893062592
- 98302514705


## Instruções


Status possíveis:

  - Regular: Quando o CPF não apresenta nenhuma irregularidade ou pendência. Devemos zelar para que nosso CPF esteja sempre assim.

  - Nula: Um CPF apresenta situação nula quando a Receita Federal, órgão responsável pela emissão do documento, detecta alguma fraude na inscrição, gerando, certamente, a anulação do documento.

  - Suspensa: Um CPF Suspenso. Nesse caso, o cadastramento ou inscrição do contribuinte não está completo ou não está correto, resultando nessa situação.

  - Cancelada: Já o cancelamento de um CPF pode ser causado pelo falecimento de seu titular.  Ou ainda, através de uma decisão judicial ou administrativa.

  - Pendente de Regularização: Talvez a situação mais simples de ser resolvida. O CPF que esteja Pendente de Regularização está nessa situação por não ter entregue Declaração do Imposto de Renda da Pessoa Física (DIRPF). E, portanto, tinha obrigação, pelo menos uma vez, nos últimos cinco anos, como nos informa o site Brasil Consultas.



## API Endpoints
`GET /` ou `GET /docs` ou `GET /documentation`
- Apresenta a documentação da API


`POST /register`
#### Responses
body:

```json
  "username": "<seu-nome-de-usuario>",
  "password": "<uma-senha>"
```

e retorna:
```json
  "username": "<seu-nome-de-usuario>",
  "user_token": "<seu-token>"
```

`POST /login`
#### Responses
body:

```json
  "username": "<seu-nome-de-usuario>",
  "password": "<sua-senha>"
```

e retorna:
```json
  "access_token": "<seu-token-de-acesso>",
  "refresh_token": "<refresh-token>",
  "message": "success"
```

`GET /consult/<cpf>`
#### Responses
 - `200 OK` em caso de requisição bem sucedida

 Respostas bem sucedidas terão o seguinte formato:

 ```json
   {
     "status": "<situation>"
   }
 ```

 Exemplo:

 ```json
   {
     "status": "Regular"
   }
 ```

 - `404 Not Found` se o CPF não for encontrado

 Respostas com erros terão o seguinte formato:

 ```json
   {
     "erro": {
         "reason": "error description"
     }
   }
 ```

## Como Executar esse Projeto
```bash
  ~$ docker-compose build
  ~$ docker run -p 5000:5000 cpf-status-api
```

## Gerar as Migrações
```bash
  ~$ flask db init
  ~$ flask db migrate
  ~$ flask db upgrade
```

## Como Executar os Testes e Obter a Cobertura
```bash

  ~$ coverage run --source=app -m unittest discover -s . -v

  # mostra um resumo da cobertura no shell
  ~$ coverage report

  # gera o path '/htmlcov' com htmls estáticos da cobertura
  ~$ coverage html
```
