import pytest
from task import Task, TaskManager

# Testa se a tarefa foi criada corretamente.
def test_create_task():
    task = Task(1, "Task de exemplo")
    assert task.task_id == 1
    assert task.description == "Task de exemplo"
    assert not task.done

# Testa se a tarefa foi adicionada ao array de tarefas.
def test_add_task():
    manager = TaskManager()
    task = Task(1, "Task de exemplo")
    manager.add_task(task)
    assert manager.tasks == [task]

# Adiciona duas tarefas e testa se a tarefa foi removida do array de tarefas.
def test_list_tasks():
    manager = TaskManager()
    task1 = Task(1, "Task de exemplo")
    task2 = Task(2, "Task de exemplo 2")
    manager.add_task(task1)
    manager.add_task(task2)
    assert manager.list_tasks() == [task1, task2]

# Adiciona duas tarefas e testa se a tarefa foi removida do array de tarefas.
def test_mark_task_done():
    manager = TaskManager()
    task1 = Task(1, "Task de exemplo")
    manager.add_task(task1)
    manager.mark_task_done(1)
    assert task1.done == True

# Adiciona duas tarefas e testa se a tarefa foi removida corretamente do array de tarefas.
def test_remove_task():
    manager = TaskManager()
    task1 = Task(1, "Task de exemplo")
    task2 = Task(2, "Task de exemplo 2")
    manager.add_task(task1)
    manager.add_task(task2)
    manager.remove_task(1)
    assert manager.tasks == [task2]

