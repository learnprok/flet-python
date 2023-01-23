import flet
from flet import Page, Row, TextField, Column

def main(page: Page):
    txt_name = TextField(hint_text='nombre')
    txt_lastname = TextField(hint_text='apellido')
    txt_lastname.disabled = True
    
    row_controls = Column([
        txt_name,
        txt_lastname
    ])

    row_controls.disabled = True

    page.add(row_controls)


flet.app(target=main)
