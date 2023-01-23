import flet
from flet import Page, Text, Row

def main(page: Page):
    langs = ['Python', 'Flet', 'Flutter']
    tags = []

    for lang in langs:
        tags.append(Text(lang))

    # Row es un contenedor que añade otros contenedores
    row_data = Row(
        controls=tags
    )
    page.add(row_data)

flet.app(target=main)

