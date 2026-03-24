import sys
import os

from app import tasks

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

def test_add_task():
    tasks.add_task("Learn Docker")
    assert "Learn Docker" in tasks.get_tasks()

def test_multiple_tasks():
    tasks.add_task("Learn CI")
    tasks.add_task("Learn Devops")

    tasks1=tasks.get_tasks()

    assert "Learn CI" in tasks1
    assert "Learn Devops" in tasks1
#please work
# wifi attempts sabotage