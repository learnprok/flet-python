import flet
from flet import Page, ElevatedButton, Row


def main(page: Page):
    # tambien se puede con dark
    page.theme_mode = 'light'

    def change_theme_clicked(event):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()
    

    btn_change_theme = ElevatedButton('Cambiar tema', on_click=change_theme_clicked)
    page.add(
        Row([
            btn_change_theme
        ]))

flet.app(target=main)