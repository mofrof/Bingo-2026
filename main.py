import flet as ft
import views


def main(page: ft.Page):
    page.title = "Sistema BINGO"
    page.window.maximized = True
    page.theme_mode = ft.ThemeMode.DARK

    menu = views.criarMenu()

    page.add(menu)

ft.run(main=main)