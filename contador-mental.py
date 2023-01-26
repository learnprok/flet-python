import flet
from flet import Page, TextField, IconButton, Row, icons

color_blue = '#2589BD'

def main(page: Page):
    page.title = 'Contador'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'


    page.add(Row([
        IconButton(icons.REMOVE),
        TextField(value='0', width=100, border_color=color_blue),
        IconButton(icons.ADD)
    ]))


flet.app(target=main)
