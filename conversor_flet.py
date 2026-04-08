import flet as ft

def main(page: ft.Page):
    def add_task(e):
        print(resposta.value)
        page.add(ft.Checkbox(label= resposta.value))
        resposta.value = ''
        page.update()
    
    titulo = ft.Text(value="Aqui é na onde comeca porraaaaa")
    resposta = ft.TextField(hint_text="Insira alguma coisa...", expand=True)
    resp2 = ft.TextField(hint_text="Digite tbm...", expand=True)
    botao = ft.FloatingActionButton(icon=ft.Icons.ADD,on_click=add_task)
    
    card = ft.Column(
                controls=[
                ft.Row(
                    controls=[
                        titulo,
                        resposta,
                        resp2,
                        botao
                    ]
                )
            ]
        )
    page.add(card)

ft.app(target=main)