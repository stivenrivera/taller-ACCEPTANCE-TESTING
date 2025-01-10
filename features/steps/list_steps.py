from behave import given, when, then
from main import ToDoListManager

@given('the to-do list is empty')
def step_given_empty_list(context):
    context.manager = ToDoListManager()
    context.manager.clear_tasks()

@given('the to-do list contains tasks')
def step_given_list_contains_tasks(context):
    context.manager = ToDoListManager()
    for row in context.table:
        context.manager.add_task(row['Task'], "Description", "2024-09-10", "Medium")

@when('the user adds a task "{task}"')
def step_when_add_task(context, task):
    context.manager.add_task(task, "Description", "2024-09-10", "Medium")

@when('the user lists all tasks')
def step_when_list_tasks(context):
    context.list_output = context.manager.list_tasks_formatted()

@when('the user marks task "{task}" as completed')
def step_when_mark_completed(context, task):
    context.manager.mark_completed(task)

@when('the user clears the to-do list')
def step_when_clear_list(context):
    context.manager.clear_tasks()

@when('the user removes the task "{task}"')
def step_when_remove_task(context, task):
    context.manager.remove_task(task)

@when('the user edits the task "{task}" with new title "{new_title}" and new description "{new_description}"')
def step_when_edit_task(context, task, new_title, new_description):
    context.manager.edit_task(task, new_title=new_title, new_description=new_description)

@then('the to-do list should contain')
def step_then_list_contains_updated_task(context):
    # Verifica que la lista de tareas se actualice correctamente según la tabla del escenario
    tasks = [
        {"task": row['Task'], "description": row['Description']}
        for row in context.table
    ]
    
    # Verifica que las tareas en el contexto coincidan con las esperadas
    actual_tasks = context.manager.list_tasks()
    for task in tasks:
        found = False
        for actual_task in actual_tasks:
            if actual_task['title'] == task['task'] and actual_task['description'] == task['description']:
                found = True
                break
        assert found, f"Task '{task['task']}' with description '{task['description']}' not found in the list"


@then('the to-do list should contain "{task}"')
def step_then_list_should_contain(context, task):
    titles = [task['title'] for task in context.manager.list_tasks()]
    assert task in titles

@then('the to-do list should show task "{task}" as completed')
def step_then_task_completed(context, task):
    for t in context.manager.list_tasks():
        if t['title'] == task:
            assert t['completed'] is True

@then('the output should contain')
def step_then_output_should_contain(context):
    expected_tasks = [line.strip('- ') for line in context.text.strip().splitlines()[1:]]
    actual_tasks = [task['title'] for task in context.manager.list_tasks()]
    assert expected_tasks == actual_tasks, f"Expected: {expected_tasks}, but got: {actual_tasks}"


@then('the to-do list should be empty')
def step_then_list_empty(context):
    assert len(context.manager.list_tasks()) == 0

@then('the to-do list should not contain "{task}"')
def step_then_list_should_not_contain(context, task):
    titles = [task['title'] for task in context.manager.list_tasks()]
    assert task not in titles
