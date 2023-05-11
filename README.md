<h1 align="center"> Token Manager </h1>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#gear-funcionamento">Funcionamento</a>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</p>

<br>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- Python

## 💻 Projeto

Um script de automação que auxilia na gestão de tokens e senhas

## :gear: Funcionamento

Para que o projeto funcione são necessários os seguintes requisitos:

- Ter o Python instalado e adicionado ao PATH
- Instalar as bibliotecas utilizando o comando "pip install -r requirements.txt", em  ambiente Windows, ou "pip3 install -r requirements.txt" em ambiente Linux
- Substituir o diretório de tokens na constante "TOKEN_FOLDER_PATH"
- No caso de um ambiente Linux, instalar xclip com o comando "sudo apt install xclip"

Feito isso, basta rodar o comando

- "python main.py -{nome-token}", em ambiente Windows
- "python3 main.py -{nome-token}" em ambiente Linux

O script lerá o conteúdo e o deixará disponível na área de transferência

---
