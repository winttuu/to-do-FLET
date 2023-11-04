import flet
from flet import CrossAxisAlignment
from todo import TodoApp

def main(page: flet.Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()
    page.add(todo)

flet.app(target=main)