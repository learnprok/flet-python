import flet
from flet import Page, Row, TextField, ElevatedButton, Text



def main(page: Page):
    page.theme_mode = 'dark'
    
    txtf_name = TextField(label='Digite su nombre')
    
    lbl_greeting = Text()
    
    def saludar(event):
        lbl_greeting.value = f'Hola ¡{txtf_name.value}!'
        page.update()
    
    row = Row(controls=[
        txtf_name,
        ElevatedButton(text='Saludar', on_click=saludar),
        lbl_greeting

    ])
    page.add(row)



flet.app(target=main)
