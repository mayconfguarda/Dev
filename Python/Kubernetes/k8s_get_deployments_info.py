import argparse
import json
from kubernetes import client, config
from prettytable import PrettyTable

def search_namespace():
    # Pergunta ao usuário se deseja filtrar por namespace
    namespace = input('\n🔍 Deseja filtrar por um namespace específico? \nDigite o nome do namespace (ou deixe em branco para buscar em todos): ')
    return namespace

def search_context():
    # Pergunta ao usuário o nome do contexto
    context = input('\n🌐 Digite o nome do contexto Kubernetes: ')

    # Carrega a configuração do contexto
    config.load_kube_config(context=context)

    return context

def main():
    # Solicita o nome do contexto
    context = search_context()

    while True:
        # Pergunta se deseja filtrar por um namespace específico
        namespace = search_namespace()

        # Cria uma instância do cliente Kubernetes
        api = client.AppsV1Api()
<<<<<<< HEAD
        autoscaling_api = client.AutoscalingV1Api()
=======
>>>>>>> 8bab8c4c6428d7b2d7398c3c278754759458a2b6

        if namespace:
            deployments = api.list_namespaced_deployment(namespace).items
        else:
            deployments = api.list_deployment_for_all_namespaces().items

        # Cria a tabela para exibir as informações
        table = PrettyTable()
        table.field_names = ['Deployment', 'Contexto', 'CPU Limit', 'Memory Limit', 'Min Pods', 'Max Pods']

        # Preenche a tabela com as informações dos deployments
        for deployment in deployments:
            name = deployment.metadata.name
            try:
                resources = deployment.spec.template.spec.containers[0].resources
                core_limit = resources.limits.get('cpu', 'N/A')
                memory_limit = resources.limits.get('memory', 'N/A')
            except AttributeError:
                core_limit = 'N/A'
                memory_limit = 'N/A'
<<<<<<< HEAD

            # Busca as informações do HPA associado ao deployment
            hpa = autoscaling_api.read_namespaced_horizontal_pod_autoscaler(name=name, namespace=namespace)
            min_replicas = hpa.spec.min_replicas
            max_replicas = hpa.spec.max_replicas

=======
            min_replicas = deployment.spec.replicas
            max_replicas = deployment.spec.replicas
>>>>>>> 8bab8c4c6428d7b2d7398c3c278754759458a2b6
            table.add_row([name, context, core_limit, memory_limit, min_replicas, max_replicas])

        # Exibe a tabela
        print('\n👀 Informações dos deployments:\n')
        print(table)

        # Pergunta ao usuário se deseja buscar um novo namespace, ou trocar de contexto, ou sair.
        user_input = input("\n🤔 Digite 'N' -> Deseja buscar um novo namespace? \n🤔 Digite 'C' -> Deseja trocar de contexto? \n🤔 Digite 'S' -> para sair. \n    Digite aqui 👉  ")
        if user_input.lower() == 'n':
            continue
        elif user_input.lower() == 'c':
            context = search_context()
            continue
        else:
            break
<<<<<<< HEAD
=======

>>>>>>> 8bab8c4c6428d7b2d7398c3c278754759458a2b6
if __name__ == '__main__':
    main()
