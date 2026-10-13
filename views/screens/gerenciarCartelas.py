import flet as ft
import views.components.cartela as ct
import models.Cartela as modelCt

def telaGerenciaCartelas():
    listElementosColunaCartela = []
    cartelas = ft.Container(content=ft.Text("Lista Cartelas", size=25), alignment=ft.Alignment.CENTER)
    listElementosColunaCartela.append(cartelas)

    butaoAlterar = ft.Button(content="Alterar", icon=ft.Icons.EDIT)
    butaoRemover = ft.Button(content="Remover",icon=ft.Icons.REMOVE)
    linhaButoes = ft.Row(controls=[butaoAlterar,butaoRemover],expand=True, alignment=ft.MainAxisAlignment.END)

    listaCartelas = modelCt.pegarListaCartelas()
    for cartela in listaCartelas:
        cartelaModelo = ct.criarCartela(cartela['codigo'],cartela['B'],cartela['I'],cartela['N'],cartela['G'],cartela['O'])
        cartelaModelo.content.content.controls.append(linhaButoes)
        listElementosColunaCartela.append(cartelaModelo)

    colunaCartelas = ft.Container(content=ft.Column(controls=listElementosColunaCartela,
                                                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                                    scroll=ft.ScrollMode.AUTO),
                                expand=True)

    return colunaCartelas