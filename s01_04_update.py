import time
import flet
from flet import Page, Text

def main(page: Page):
    lbl_text = Text()
    page.add(lbl_text)

    for i in range(1, 10+1):
        lbl_text.value = f'Step: {i}'
        page.update()
        time.sleep(1)

flet.app(target=main, view=flet.WEB_BROWSER)
