#Importa a biblioteca do pytest e as classes Task e TaskManager do arquivo task.py.

import pytest
from task import Task, TaskManager

# Testa se a tarefa foi criada corretamente.
def test_add_task_and_list_tasks():
    manager = TaskManager()
    task1 = Task(1, "Task de exemplo")
    task2 = Task(2, "Task de exemplo 2")
    manager.add_task(task1)
    manager.add_task(task2)
    assert manager.list_tasks() == [task1, task2]

# Testa se a tarefa foi adicionada ao array de tarefas e foi concluida corretamente.
def test_mark_task_done():
    manager = TaskManager()
    task = Task(1, "Task de exemplo")
    manager.add_task(task)
    manager.mark_task_done(1)
    assert task.done == True

# Testa se a tarefa foi removida corretamente do array, e depois testa a lista para conferir.
def test_remove_task():
    manager = TaskManager()
    task1 = Task(1, "Task de exemplo")
    task2 = Task(2, "Task de exemplo 2")
    manager.add_task(task1)
    manager.add_task(task2)
    manager.remove_task(1)
    assert manager.tasks == [task2]