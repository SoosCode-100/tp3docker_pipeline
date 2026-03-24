import sys
import os

from app.tasks import add_task, get_tasks 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

def test_add_task():
    add_task("Learn Docker")
    assert "Learn Docker" in add_task.tasks

def test_multiple_tasks():
    add_task("Lean CI")
    add_task("Learn Devops")
    tasks=get_tasks()
    assert "Learn CI" in tasks
    assert "Learn Devops" in tasks

    