# Controle de OS

# Pátio Digital

_“Recurso público retorna ao público”._

Nós somos o **pátio digital**, uma iniciativa da Secretaria Municipal de Educação de São Paulo que, por meio do fortalecimento da transparência, da participação social e do desenvolvimento de novas tecnologias, aproxima diferentes grupos da sociedade civil por um objetivo maior: a melhoria da educação na cidade de São Paulo. 

## Conteúdo

1. [Sobre o Controle de OS](#sobre-o-controle-de-os)
2. [Comunicação](#comunicação)
3. [Roadmap de tecnologia](#roadmap-de-tecnologia)
4. [Como contribuir](#como-contribuir)
5. [Instalação](#instalação)

## Sobre o Controle de OS
  O controle de OS é um sistema interno da SME que otimiza o gerenciamento e acompanhamento das Ordens de Serviços geradas pelas Coordenadorias educacionais Municipais de São Paulo. (Sistema em desenvolvimento)
  
  
  ## Comunicação
  | Canal de comunicação | Objetivos |
|----------------------|-----------|
| [Issues do Github](https://github.com/prefeiturasp/SME-Controle-de-OS/issues) | - Sugestão de novas funcionalidades<br> - Reportar bugs<br> - Discussões técnicas |
  | [Telegram](https://t.me/patiodigital ) | - Comunicar novidades sobre os projetos<br> - Movimentar a comunidade<br>  - Falar tópicos que **não** demandem discussões profundas |

Qualquer outro grupo de discussão não é reconhecido oficialmente.


## Roadmap de tecnologia

### Passos iniciais
- Melhorar a qualidade de código
- Iniciar a escrita de testes unitários
- Iniciar escrita de testes funcionais
- Melhorar documentação de maneira enxuta


## Como contribuir

Contribuições são **super bem vindas**! Se você tem vontade de construir o com
Controle de OS conosco, veja o nosso [guia de contribuição](./CONTRIBUTING.md)
onde explicamos detalhadamente como trabalhamos e de que formas você pode nos
ajudar a alcançar nossos objetivos. Lembrando que todos devem seguir 
nosso [código de conduta](./CODEOFCONDUCT.md).

## Instalação

## Dependências
* [Python3] (https://docs.python.org/3/)
* [Django 2.0] (https://docs.djangoproject.com/en/2.1/)

Gerenciador de Pacotes
* Pip

Banco de Dados
* Postgress(configure-o em sua maquina)


### Subir ambiente de desenvolvimento
1. Iniciar ambiente virtual:
  Windons:  myvenv\Scripts\activate
  Linux e OSX: source myvenv/bin/activate ou . myvenv/bin/activate

2. Instalar Django: `python3 -m pip install --upgrade pip`

3. Rodar uma versão do servidor de desenvolvimento: `python manage.py runserver`

4. Endereço de desenvolvimento: http://127.0.0.1:8000/

Baseado no Readme do [i-educar](https://github.com/portabilis/i-educar)
