import flet as ft
import views.components.cartela as ct

def telaGerenciaCartelas():
    cartelas = ft.Container(content=ft.Text("Lista Cartelas", size=25), alignment=ft.Alignment.CENTER)

    butaoAlterar = ft.Button(content="Alterar", icon=ft.Icons.EDIT)
    butaoRemover = ft.Button(content="Remover",icon=ft.Icons.REMOVE)
    linhaButoes = ft.Row(controls=[butaoAlterar,butaoRemover],expand=True, alignment=ft.MainAxisAlignment.END)
    # container = ft.Container(content=linhaButoes, expand=True, bgcolor="RED")

    listaNumerosB = [7,13,3,8,15]
    listaNumerosI = [24,30,19,16,18]
    listaNumerosN = [39,38,44,34]
    listaNumerosG = [57,58,46,52,54]
    listaNumerosO = [67,70,64,75,74]

    cartelaModelo = ct.criarCartela(listaNumerosB,listaNumerosI,listaNumerosN,listaNumerosG,listaNumerosO)

    cartelaModelo.content.content.controls.append(linhaButoes)

    colunaCartelas = ft.Container(content=ft.Column(controls=[cartelas, cartelaModelo, cartelaModelo, cartelaModelo],
                                                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                                    scroll=ft.ScrollMode.AUTO),
                                expand=True)

    return colunaCartelas