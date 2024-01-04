Feature: To-Do List Management

  Scenario: Adding a task to the to-do list
    Given the user wants to add a task
    When they add a task with name "Task 1" and description "Description for Task 1"
    Then the task "Task 1" should be added to the to-do list

  Scenario: Listing all tasks in the to-do list
    Given there are tasks in the to-do list
    When the user requests to list all tasks
    Then they should see a list of tasks in the to-do list

  Scenario: Marking a task as completed
    Given there are tasks in the to-do list
    When the user marks task 1 as completed
    Then task 1 should be marked as completed

  Scenario: Finding and removing a task by name
    Given there are tasks in the to-do list
    When the user removes the task with name "Task 2"
    Then the task "Task 2" should be removed from the to-do list

  Scenario: Editing the description of a task
    Given there are tasks in the to-do list
    When the user edits the description of task "Task 3" to "Updated description for Task 3"
    Then the description of task "Task 3" should be updated

  Scenario: Clearing the entire to-do list
    Given there are tasks in the to-do list
    When the user clears all tasks
    Then the to-do list should be empty