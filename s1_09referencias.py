import flet
from flet import Page, Text, TextField, ElevatedButton, Column

def main(page: Page):
    page.theme_mode = 'dark'

    def add_product_clicked(event):
        col_controls.controls.append(Text(f'El producto es {txt_product.value}'))
        txt_product.value = ''
        page.update()
        txt_product.focus()


    txt_product = TextField(hint_text='Producto')
    btn_add_product = ElevatedButton('Añadir producto', on_click=add_product_clicked)

    col_controls = Column([
        txt_product,
        btn_add_product
    ])

    page.add(col_controls)

    


flet.app(target=main, assets_dir='assets', view=flet.FLET_APP)