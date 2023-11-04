import flet
from flet import TextField, Column, FloatingActionButton, icons, Checkbox, Row, Tabs, Tab, OutlinedButton, Text
from task import Task

class TodoApp(flet.UserControl):
    def build(self):
        self.new_task = TextField(hint_text="Whats needs to be done?", expand=True)
        self.tasks = Column()

        self.filter = Tabs(
            selected_index = 0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="all"), Tab(text="active"), Tab(text="completed")],
        )

        return Column(
            width=600,
            controls=[
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self._add_clicked),
                    ]
                ),
                self.filter,
                self.tasks
            ]
        )

    def tabs_changed(self, evt):
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text

        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )

        super().update()

    def _add_clicked(self, evt):
        task = Task(self.new_task.value, self.task_delete, self.tabs_changed)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()