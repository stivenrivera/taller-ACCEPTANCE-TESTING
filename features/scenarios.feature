Feature: Manage tasks in a to-do list

Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
        | Task          |
        | Buy groceries |
        | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
        """
        Tasks:
        - Buy groceries
        - Pay bills
        """

Scenario: Mark a task as completed
    Given the to-do list contains tasks:
        | Task          | Status  |
        | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
        | Task          |
        | Buy groceries |
        | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

Scenario: Remove a task from the to-do list
    Given the to-do list contains tasks:
        | Task          |
        | Buy groceries |
        | Pay bills     |
    When the user removes the task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"

Scenario: Edit a task in the to-do list
    Given the to-do list contains tasks:
        | Task          | Description      |
        | Buy groceries | Purchase items   |
    When the user edits the task "Buy groceries" with new title "Weekly Shopping" and new description "Buy items for the week"
    Then the to-do list should contain:
        | Task            | Description            |
        | Weekly Shopping | Buy items for the week |
