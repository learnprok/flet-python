import flet
from flet import Page, Text

def main(page: Page):
    lbl_text = Text(value='Hola mundo', color='green')
    page.controls.append(lbl_text)
    page.update()

flet.app(target=main)