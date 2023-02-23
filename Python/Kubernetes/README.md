## Consulta de Deployments no Kubernetes
Este é um script Python que permite consultar informações sobre os deployments no Kubernetes.

## Requisitos
Python 3.x
Bibliotecas: argparse, json, kubernetes, prettytable

## Como utilizar

1. Clone o repositório para o seu computador.
2. Instale as bibliotecas necessárias executando o comando pip install argparse json kubernetes prettytable

3. No terminal, navegue até o diretório onde o script está salvo.
4. Execute o comando python3 k8s_get_deployments_info.py para iniciar o script.
    4.1 Quando solicitado, digite o nome do contexto Kubernetes que você deseja utilizar. 
        O script irá carregar a configuração do contexto selecionado.

    4.2 Quando solicitado, digite o nome do namespace que você deseja filtrar. Se não quiser filtrar por namespace, deixe o campo em branco.
        O script irá exibir uma tabela com informações sobre os deployments. 
        As informações exibidas incluem nome do deployment, contexto Kubernetes, limites de CPU e memória, e número mínimo e máximo de réplicas.
        Você pode buscar por um novo namespace, trocar de contexto ou sair do script quando solicitado.

## Autor
Maycon Felix Guarda
