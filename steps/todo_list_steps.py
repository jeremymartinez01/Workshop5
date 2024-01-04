from behave import given, when, then
from todo_list import ToDoList

todo_list = ToDoList()

@given('the user wants to add a task')
def step_add_task(context):
    pass

@when('they add a task with name "{name}" and description "{description}"')
def step_add_task_with_name_and_description(context, name, description):
    todo_list.add_task(name, description)

@then('the task "{name}" should be added to the to-do list')
def step_task_should_be_added_to_todo_list(context, name):
    task = todo_list.get_task_by_name(name)
    assert task is not None, f"Task '{name}' was not added to the to-do list"

@given('there are tasks in the to-do list')
def step_tasks_exist_in_todo_list(context):
    todo_list.add_task("Task 1", "Description for Task 1")
    todo_list.add_task("Task 2", "Description for Task 2")
    todo_list.add_task("Task 3", "Description for Task 3")

@when('the user requests to list all tasks')
def step_user_requests_list_all_tasks(context):
    context.list_output = todo_list.list_tasks()

@then('they should see a list of tasks in the to-do list')
def step_should_see_list_of_tasks(context):
    assert context.list_output is not None, f"No tasks were listed"

@when('the user marks task {task_number:d} as completed')
def step_user_marks_task_completed(context, task_number):
    todo_list.mark_task_completed(task_number)

@then('task {task_number:d} should be marked as completed')
def step_task_should_be_marked_completed(context, task_number):
    task = todo_list.tasks[task_number - 1]
    assert task.status == 'Completed', f"Task {task_number} was not marked as completed"


@when('the user removes the task with name "{name}"')
def step_user_removes_task_by_name(context,name):
    todo_list.remove_task_by_name(name)


@then('the task "{name}" should be removed from the to-do list')
def step_task_should_be_removed(context, name):
    task =  todo_list.get_task_by_name(name)
    assert task is not None, f"Task '{name}' was not removed from the to-do list"

@when('the user edits the description of task "{name}" to "{new_description}"')
def step_user_edits_task_description(context, name, new_description):
    context.task_name = name
    context.new_description = new_description
    todo_list.edit_task_description(name, new_description)

@then('the description of task "{name}" should be updated')
def step_task_description_should_be_updated(context, name):
    task = todo_list.get_task_by_name(name)
    assert task.description == context.new_description, f"Description of task '{name}' was not updated as expected to '{context.new_description}'"

@when('the user clears all tasks')
def step_user_clears_all_tasks(context):
    todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_todo_list_should_be_empty(context):
    assert len(todo_list.tasks) == 0, "The to-do list is not empty after clearing"
