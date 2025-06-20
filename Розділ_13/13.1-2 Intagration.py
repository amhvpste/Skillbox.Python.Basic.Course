class Stack:
    def __init__(self):
        self.__st = []

    def __str__(self):
        return str(self.__st)

    def push(self, elem):
        """Додає елемент на вершину стеку."""
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f"Пріоритет {i_priority}: {self.task[i_priority]}")
        return "\n".join(display)  # додано повернення рядка

    def new_task(self, task, prioryty):
        if prioryty not in self.task:
            self.task[prioryty] = Stack()
        self.task[prioryty].push(task)


manager = TaskManager()
manager.new_task("Завдання 1", 1)
manager.new_task("Завдання 2", 2)
manager.new_task("Завдання 3", 4)
manager.new_task("Завдання 4", 4)
print(manager)
