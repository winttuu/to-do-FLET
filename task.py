import flet
from flet import Checkbox, TextField, MainAxisAlignment, CrossAxisAlignment, IconButton, Row, IconButton, Column, icons, colors

class Task(flet.UserControl):
    def __init__(self, task_name, task_delete, task_status_change):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        self.completed = False
        self.task_status_change = task_status_change

    def build(self):
        self.display_task = Checkbox(
            value=False, 
            label=self.task_name, 
            on_change=self._status_changed
        )
        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self._edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self._delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self._save_clicked,
                ),
            ],
        )

        return Column(controls=[self.display_view, self.edit_view])

    def _edit_clicked(self, evt):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def _save_clicked(self, evt):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def _delete_clicked(self, evt):
        self.task_delete(self)

    def _status_changed(self, evt):
        self.completed = self.display_task.value
        self.task_status_change(self)