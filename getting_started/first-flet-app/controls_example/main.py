import time
import flet as ft


def main(page: ft.Page):
    # page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    t = ft.Text(value="Hello, world!", color="green")
    # page.controls.append(t)
    page.add(t)

    page.add(
        # ft.Row(controles=[
        #     ft.Text("A"),
        #     ft.Text("B"),
        #     ft.Text("C")
        # ])
        ft.Row(controls=[ft.Text("A1"), ft.Text("B"), ft.Text("C")], spacing=10)
    )

    def button_clicked(e):
        t.value = "Button clicked1"
        page.update()
    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)

ft.app(main)
