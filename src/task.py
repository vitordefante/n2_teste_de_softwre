# Iniciando a classe Task

class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.done = False

# Iniciando a classe task manager

class TaskManager:

    #Inicia um array vazio de tarefas
    def __init__(self):
        self.tasks = []
    #Adiciona uma nova tarefa ao array de tarefas
    def add_task(self, task):
        self.tasks.append(task)

    #Mostra a lista de tarefas.
    def list_tasks(self):
        return self.tasks

    #bota o valor de done como True
    def mark_task_done(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.done = True
                break

    #Cria um novo array de tarefas, NÃO contendo apenas a tarefa que o ID foi fornecido para ser removido. Meio mal otimizado mas funciona.
    def remove_task(self, task_id):
        new_tasks = []
        for task in self.tasks:
            if task.task_id != task_id:
                new_tasks.append(task)
            self.tasks = new_tasks

        