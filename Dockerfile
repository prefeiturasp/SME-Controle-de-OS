# Configuração do python para ser utilizada no conteiner
FROM python:3.6

# Permite criar as variaveis de ambiente com o env
ENV PYTHONUNBUFFERED 1

# Cria o diretorio que guardara os arquivos do projeto
#RUN mkdir /app


# Instrui em qual diretorio os comandos vao ser executados
WORKDIR /code

# Copia o arquivo do host para o container
COPY requirements.txt /code/

# Executa o comando dentro do container
RUN pip install -r requirements.txt

# Copia o arquivo do host para o container
COPY . /code

# Mapeia uma porta do container para o host  
EXPOSE 8000

