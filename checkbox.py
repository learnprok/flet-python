import flet
from flet import Page, Checkbox, Text

def main(page: Page):

    

    def clicked_checkbox(event):
        lbl_message.value = f'Hola,vas aprende a programas {chk_task.value}'
        page.update()

    lbl_message = Text()
    chk_task = Checkbox(label='Aprender flet', on_change=clicked_checkbox)

    page.add(
        chk_task,
        lbl_message
    )
    


flet.app(target=main)