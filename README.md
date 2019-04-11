# Analise de logs
Projeto do curso Nanodegree FullStack.

## Objetivos do projeto
Gerar um relatório em cima da base de dados que responda as seguintes perguntas:
- Quais são os três artigos mais populares de todos os tempos?
- Quem são os autores de artigos mais populares de todos os tempos?
- Em quais dias mais de 1% das requisições resultaram em erros?

## Desevolvimento
Este projeto usa o código Python com o DB-API. O código não tem erros e segue as recomendações de estilo do PEP8. O projeto é executado na configuração da máquina virtual (VM) baseada em Linux da Udacity no Vagrant.

## Executando o projeto.
- Baixe o [Vagrant](https://www.vagrantup.com/downloads.html) e instale.
- Faz o fork e clona ou faz o download da configuração de [máquina virtual baseada em Linux do Udacity](https://github.com/udacity/fullstack-nanodegree-vm)
- Baixe o [Virtual Box 5.1.x](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) e instale.
- Faça o download do newsdata.sql da página do curso e extraia o diretório do seu vagrant na sua VM.
- Para começar a trabalhar no projeto, execute os seguintes comandos do terminal na pasta onde seu vagrant está instalado:
    - ```vagrant up``` para iniciar a VM.
    - ```vagrant ssh``` para entrar na VM.
    - ```cd /vagrant``` para mudar para o seu diretório vagrant.
    - ```psql -d news -f newsdata.sql``` para carregar os dados e criar as tabelas.
    - ```python newsdata.py``` para executar a ferramenta de relatório.

**Para visualizar o schema das tabelas do banco. [Acesse](./info_tables.md)