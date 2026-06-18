from datetime import datetime

def validate_task_title(title):
    if len(title) == 0:
        print("Title cannot be empty.")
        return False

    if len(title.strip()) == 0:
        print("Title cannot be empty.")
        return False

    return True


def validate_task_description(description):
    if len(description) == 0:
        print("Description cannot be empty.")
        return False

    if len(description.strip()) == 0:
        print("Description cannot be empty.")
        return False

    return True


def validate_due_date(due_date):
    try:
        if len(due_date) == 0:
            print("Invalid date format. Use YYYY-MM-DD.")
            return False

        datetime.strptime(due_date, "%Y-%m-%d")
        return True

    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return False