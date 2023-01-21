import flet
from flet import Page, Checkbox, TextField, Row, ElevatedButton, Text


def main(page: Page):
    
    def add_task_clicked(event):
        if txt_new_task.value == '':
            lbl_message.value = 'Por favor llene el camo'
            page.update()
        else:
            lbl_message.value = ''
            page.add(Checkbox(
                label=txt_new_task.value
            ))

    lbl_message = Text(color='red')
    txt_new_task = TextField(hint_text='¿Cual tarea desea agregar?', width=300)
    btn_add_task = ElevatedButton('Agregar', on_click=add_task_clicked)


    page.add(Row([
        txt_new_task,
        btn_add_task,
        lbl_message
    ])
    )

flet.app(target=main)