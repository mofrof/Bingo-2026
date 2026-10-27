import flet as ft
import views.components.cartela as ct
import models.Cartela as modelCt
import views.menu as menu

def voltarListaPaginas(e: ft.Event[ft.Button]):
    estruturaPagina = e.control.data[0]
    menu.ao_mudar_aba(estruturaPagina, 2)

def criarCampo(codigo):
    textFild = ft.TextField(value=codigo,
                            border_color=ft.Colors.WHITE,
                            on_change=modelCt.verificarValorDigitado)
    return textFild

def telaAlterarCartelas(estruturaPagina, codigoCartela):
    dadosCartelaParaAlterar = modelCt.pegarCartelaDadosCartelaPeloCodigo(codigoCartela)

    titulo = ft.Container(content=ft.Text("Alterar Cartela", size=35, weight=ft.FontWeight.BOLD), alignment=ft.Alignment.CENTER)

    codCartelaTextFild = ft.Container(content= ft.TextField(label="Código Cartela", value=dadosCartelaParaAlterar["codigo"], border_color=ft.Colors.WHITE), alignment=ft.Alignment.CENTER_LEFT)

    letraB = ft.Container(content=ft.Text("B", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)
    letraI = ft.Container(content=ft.Text("I", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)
    letraN = ft.Container(content=ft.Text("N", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)
    letraG = ft.Container(content=ft.Text("G", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)
    letraO = ft.Container(content=ft.Text("O", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)

    listaLetras = [letraB, letraI, letraN, letraG, letraO]
    listaLinha = []
    listaColuna = []

    for index, value in enumerate(["B","I", "N" , "G", "O"]):
        listaColuna.append(listaLetras[index])
        for j in range(5):
            textFild = None
            if index== 2 and j == 2:
                textFild = ft.Container(content=ft.Icon(icon=ft.Icons.TABLE_CHART,size=50),
                                alignment=ft.Alignment.CENTER)
            else:
                if(index == 2 and j > 1):
                    textFild = ft.TextField(label=f"{index}:{j}", data=f"{index}:{j}",
                                        border_color=ft.Colors.WHITE,
                                        value=dadosCartelaParaAlterar[value][j-1],
                                        on_change=modelCt.verificarValorDigitado
                                        )
                else:
                    textFild = ft.TextField(label=f"{index}:{j}", data=f"{index}:{j}",
                                        border_color=ft.Colors.WHITE,
                                        value=dadosCartelaParaAlterar[value][j],
                                        on_change=modelCt.verificarValorDigitado
                                        )
            listaColuna.append(textFild)
        coluna = ft.Column(controls=listaColuna, expand=True, alignment=ft.Alignment.CENTER)
        listaLinha.append(coluna)
        listaColuna = []

    cartelaBingo = ft.Row(controls=listaLinha, expand=True, alignment=ft.MainAxisAlignment.CENTER)

    textoMensagens = ft.Text("", size=25)

    butaoAlterar = ft.Button(content=ft.Text("Alterar", size=25, weight=ft.FontWeight.BOLD),
                       align=ft.Alignment.BOTTOM_RIGHT,
                       height=50,
                       on_click=modelCt.atualizarCartela,
                       data=[listaLinha, codCartelaTextFild, dadosCartelaParaAlterar["codigo"], textoMensagens, estruturaPagina])

    butaoCancelar = ft.Button(content=ft.Text("Cancelar", size=25, weight=ft.FontWeight.BOLD),
                       align=ft.Alignment.BOTTOM_RIGHT,
                       height=50,
                       on_click=voltarListaPaginas,
                       data=[estruturaPagina])

    linhaButoes = ft.Row(controls=[butaoCancelar, butaoAlterar])

    linhaButao = ft.Row(controls=[textoMensagens, linhaButoes], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, margin=0)

    conteudo = ft.Column(controls=[titulo, codCartelaTextFild ,cartelaBingo, linhaButao], horizontal_alignment=ft.CrossAxisAlignment.STRETCH, margin=0)

    container = ft.Container(content=conteudo, expand=True)

    return container