# STARKBANK CHALLENGE
## _Produzido por Marco Aurélio Menezes, versão 1.6_

[![N|Solid](https://starkbank.com/images/logo.svg)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


## The Challenge


1. Emite de 8 a 12 faturas a cada 3 horas para pessoas aleatórias por 24 horas

2. Recebe o retorno de chamada do webhook do crédito da fatura e envia o valor recebido

## Additional

1. consome uma API, para gerar os CPFs, e Possui base de dados para os nomes, 
. 

## requirements
- requests~=2.27.1
- starkbank~=2.15.0


## Features

- Criar novo projeto e instale os requerimentos ( pip install requirements.txt )
- Crie seu par de chaves : Publica e privada que pode ser obtidas em https://starkbank.com/faq/how-to-create-ecdsa-keys. (o arquivo authentication.py possui maiores informações)
- Executar apenas o arquivo main.pya
- existem modulos adicionais prontos, que nao fazem parte do desafio, como de saldo, consultas, baixar pdf da transação.
os mesmo foram retirados para nao atrapalhar a visualização no github.
- Foi mantindo o webhook.py pois faz parte demandas.
- 



> “Um dos meus dias mais produtivos foi quando eu joguei fora 1000 linhas de código.” – Ken Thompson
> “Há apenas uma maneira de evitar críticas: não fazer, não falar e não ser nada.” – Aristóteles

## ARQUIVOS

| PASTA | :D |
| ------ | ------ |
| MAIN | [COMEÇE POR AQUI] |
| INVOICES | [CRIA DE 8 A 12 INVOICES A CADA 3 HORAS] |
| AUTHENTICATION | [CUIDA DA AUTENTICAÇÃO NO SISTEMA ( CHAVES)] |
| TRANSFER | [VERIFICA AS INVOICES DO SISTEMA E GERA UMA TRANSFERENCIA DO MESMO VALOR] |
| WEBHOOK | {[FAZ USO DE SERVIÇOS ONLINE COMO POSTMAN, PARA RECEBER E ENVIAR INFORMAÇOS ( AINDA EM CONTRUÇÃO)] |
|  |  |


#### Building for source



**Free Software, Hell Yeah!**

   
   [![Build Status](https://discourse-cloud-file-uploads.s3.dualstack.us-west-2.amazonaws.com/business6/uploads/python1/original/1X/fe459ce92996895410438d8efee327d394e419a0.png)](https://travis-ci.org/joemccann/dillinger)
