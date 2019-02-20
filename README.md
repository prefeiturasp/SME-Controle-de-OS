# SME-Controle-de-OS

[![Maintainability](https://api.codeclimate.com/v1/badges/7d34f4c49b56a7c38466/maintainability)](https://codeclimate.com/github/prefeiturasp/SME-Controle-de-OS)



## Conteúdo

1. [Sobre o Sistema de Gerenciamento de Ordem de Serviço](#sobre-o-sistema-de-gerenciamento-de-ordem-de-serviço)
2. [Comunicação](#Comunicação)
3. [Como contribuir](#como-contribuir)
4. [Requesitos](#requesitos)
5. [Como criar e executar a máquina virtual](#como-criar-e-executar-a-máquina-virtual)
6. [Organização do projeto](#organização-do-projeto)
7. [Instalação](#instalação)


## Sobre o Sistema de Gerenciamento de Ordem de Serviço


## Comunicação

| Canal de comunicação | Objetivos |
|----------------------|-----------|
| [Issues do Github](https://github.com/prefeiturasp/SME-Controle-de-OS/issues) | - Sugestão de novas funcionalidades<br> - Reportar bugs<br> - Discussões técnicas |


## Como Contribuir

Contribuições são **super bem vindas**! Se você tem vontade de construir o
Fila da creche conosco, veja o nosso [guia de contribuição](./CONTRIBUTING.md)
onde explicamos detalhadamente como trabalhamos e de que formas você pode nos
ajudar a alcançar nossos objetivos. Lembrando que todos devem seguir 
nosso [código de conduta](./CODEOFCONDUCT.md).


## Requesitos
 
1. Python 3.6
2. Máquina virtual 
 
## Como criar e executar a Máquina Virtual

Crie a máquina com o nome controlevenv apartir dos comandos:</br>
No Windowns: `python -m venv controlevenv`</br>
No linux ou Mac OS: `python3 -m venv controlevenv`</br>

Para executar a máquina use os comados:</br>
No windows: `controlevenv\Scripts\activate`</br>
No linux ou Mac OS: `source controlevenv/bin/activate` ou `. controlevenv/bin/activate`</br>


## Organização do projeto

Baixar dependências via requirements.txt


## Instalação

1. `pip install`
2. `pip install -r requirements.txt`
3.  Executar maquina virtual: consulte o comando para o seu sistema operacional aqui na documentação
4. `cd django`
5. `python3 manage.py runserver`


