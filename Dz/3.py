from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        status = "Виконано" if self.is_done else "Не виконано"
        return f"{self.title} - {self.description}\nДедлайн: {self.deadline.strftime('%Y-%m-%d')} | Стан: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_as_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_done()
                return True
        return False

    def list_tasks(self):
        if not self.tasks:
            return "Список завдань порожній."
        return "\n\n".join(str(task) for task in self.tasks)


if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Купити продукти", "Молоко, хліб, масло", "2024-11-24")
    manager.add_task("Завершити проект", "Підготувати фінальний звіт", "2024-11-30")

    print("Список завдань:")
    print(manager.list_tasks())

    print("\nВідмічаємо завдання 'Купити продукти' як виконане...")
    manager.mark_task_as_done("Купити продукти")

    print("\nОновлений список завдань:")
    print(manager.list_tasks())

    print("\nВидаляємо завдання 'Завершити проект'...")
    manager.remove_task("Завершити проект")

    print("\nОновлений список завдань:")
    print(manager.list_tasks())
