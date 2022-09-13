# Avaliacao_Tecnica_Diagnes

Criar um sistema de agendamento de consultas simples realizando um cadastro de médicos, cadastro de agendamentos depois apresentar a agenda com as marcações de consultas

1) Utilizar o admin do Django para realizar o cadastro de médicos. Deve conter as seguintes
informações:
* Nome
* Telefone
* Email
* Especialidade (Ecocardiografista | Clínico Geral | Obstetra)
* Endereço: cep, logradouro, número, bairro, cidade, estado

2) Criar uma página pública, “Realizar Agendamento” (fora do admin), para o paciente realizar o
agendamento. Deve contar as seguintes informações:
* Nome do paciente
* Telefone
* Data e hora da consulta;
* Especialidade (que deseja realizar a consulta - Ecocardiografista | Clínico Geral | Obstetra)

3) Criar uma página pública, "Listagem de Agendamentos” (fora do admin), com uma lista
ordenada por data e hora de todos os próximos agendamentos realizados a partir da data e
hora atual, com as seguintes informações:
* Data e Hora
* Nome do paciente
* Nome do médico
* Especialidade

## Validações
* Ao selecionar a especialidade será apresentada uma lista de médicos de acordo com a especialidade selecionada.
* Verificar se a data é no futuro
* Verificar se o médico selecionado já tem um agendamento no mesmo dia e hora.

### 📋 Pré-requisitos

* [VSCode](https://code.visualstudio.com/Download)
* [Python](https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe)
* [Django](https://www.djangoproject.com/download/)
* [Bootstrap](https://getbootstrap.com.br/docs/4.1/getting-started/introduction/)
* [JQuery ](https://api.jquery.com/)

## 🚀 Começando

O objetivo é verificar noções de desenvolvimento de
sistemas com foco em desenvolvimento web utilizando o framework Django e a linguagem de
programação Python.


## 🚀 Como rodar o projeto

* 1 - Clonar o repositório do [git](https://github.com/carlosrjhoe/Avaliacao_Tecnica_Diagnes.git)
* 2 - Dentro do seu diretório, abrir o CMD e digitar: git clone + CTRL+V
* 3 - Instalar e Abrir [VSCode](https://code.visualstudio.com/Download)
* 4 - Selecionar projeto clonado do [git](https://github.com/carlosrjhoe/Avaliacao_Tecnica_Diagnes.git) para seu repositório.
* 5 - Abrir terminal do [VSCode](https://code.visualstudio.com/Download) e digitar cd .\venv\ (precionar - ENTER)
* 6 - Digitar .\Scripts\activate (precionar - ENTER)
* 7 - Digitar python .\manage.py runserver (precionar - ENTER)
* 8 - Clicar em CTRL + http://127.0.0.1:8000/(que vai aparecer no terminal)
* 9 - Digitar os campos disponiveis com dados solicitados e clicar em (cadastrar)

## 🚀 Para acessar o admin do banco de dados

Obs: Com o servidor online

* 1 - Digitar na barra de pesquisa http://127.0.0.1:8000/admin/
* 2 - Login: admin
* 3 - Senha: Admin

## 🛠️ Projéto em Construção com

* [Python](https://docs.python.org/3/library/index.html) - linguagem
* [Django](https://docs.djangoproject.com/en/4.1/) - Framework web
* [Bootstrap](https://getbootstrap.com.br/docs/4.1/getting-started/introduction/) - Para gerar HTML, CSS e JS
* [JQuery ](https://api.jquery.com/) - Biblioteca

## ✒️ Autor

* [Carlos Roberto](https://www.linkedin.com/in/carlos-roberto-conceicao/)

## 🎁 Expressões de gratidão

* Obrigado pela oportunidade de uma oportunidade 📢;
* Podem me convidar para uma cerveja 🍺;
* Um agradecimento para 🫂; [Valdenia Andrade](https://github.com/valdenia), [Átila Bezerra](https://www.linkedin.com/in/atilabezerra/), [Anderson Bispo](https://www.linkedin.com/in/anderson-bispo/)


---
⌨️ com ❤️ por [Carlos Roberto](https://github.com/carlosrjhoe) 😊
