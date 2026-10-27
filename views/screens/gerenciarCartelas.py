import flet as ft
import views.components.cartela as ct
import models.Cartela as modelCt
import views.menu as menu

def abrirTelaAlterar(e: ft.Event[ft.Button]):
    codigoCartela = e.control.data[0]
    estruturaPagina = e.control.data[1]

    menu.ao_mudar_aba(estruturaPagina, 3, codigoCartela)

def telaGerenciaCartelas(estruturaPagina=None):
    listElementosColunaCartela = []
    cartelas = ft.Container(content=ft.Text("Lista Cartelas", size=25), alignment=ft.Alignment.CENTER)
    listElementosColunaCartela.append(cartelas)

    dialogo = ft.AlertDialog(   modal=False,
                                title=ft.Text("Aviso Importante"),
                                content=ft.Text(""),
                                actions_alignment=ft.MainAxisAlignment.END)

    listaCartelas = modelCt.pegarListaCartelas()
    for cartela in listaCartelas:
        butaoAlterar = ft.Button(content="Alterar", icon=ft.Icons.EDIT,
                                 on_click=abrirTelaAlterar,
                                 data=[cartela['codigo'], estruturaPagina])
        butaoRemover = ft.Button(content="Remover",icon=ft.Icons.REMOVE,
                                 on_click=modelCt.verificarCondicoesDeExclusao,
                                 data=[cartela['codigo'],dialogo, estruturaPagina])
        linhaButoes = ft.Row(controls=[butaoAlterar,butaoRemover],expand=True, alignment=ft.MainAxisAlignment.END)

        cartelaModelo = ct.criarCartela(cartela['codigo'],cartela['B'],cartela['I'],
                                        cartela['N'],cartela['G'],cartela['O'],
                                          linhaButoes)
        listElementosColunaCartela.append(cartelaModelo)

    colunaCartelas = ft.Container(content=ft.Column(controls=listElementosColunaCartela,
                                                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                                    scroll=ft.ScrollMode.AUTO),
                                expand=True)

    return colunaCartelas