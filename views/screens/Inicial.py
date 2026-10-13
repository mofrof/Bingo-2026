import flet as ft
import views.components.cartela as ct
import models.Cartela as modelCt

def criarListaBotoes():
    listaModuloNumero = []
    for i in range(1,76):
        bordaEstilo = ft.BorderSide(width=1, color=ft.Colors.WHITE,)
        estilo = ft.ButtonStyle(color=ft.Colors.WHITE,
                                side=bordaEstilo,
                                shape=ft.CircleBorder(),
                                padding=0
                                )
        
        botao = ft.Button(content=f"{i}", style = estilo)
        listaModuloNumero.append(botao)
    return listaModuloNumero

def ladoRegistroNumero():
    numerosSorteados = ft.Container(ft.Text("Numero sorteado", size=25), alignment=ft.Alignment.CENTER)

    listaNumeros = criarListaBotoes()

    grideNumerosSorteados = ft.GridView(
                expand=True,
                padding=5,
                max_extent=60,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
                runs_count=10,
                controls=listaNumeros
                )

    colunaResultados = ft.Container(content=ft.Column(controls=[numerosSorteados,
                                                                grideNumerosSorteados]
                                                    ),
                                    expand=True)

    return colunaResultados

def ladoCartelasCadastradas():
    listElementosColunaCartela = []
    cartelas = ft.Container(content=ft.Text("Cartelas Registradas", size=25), alignment=ft.Alignment.CENTER)
    listElementosColunaCartela.append(cartelas)

    listaCartelas = modelCt.pegarListaCartelas()
    for cartela in listaCartelas:
        cartelaModelo = ct.criarCartela(cartela['codigo'],cartela['B'],cartela['I'],cartela['N'],cartela['G'],cartela['O'])
        listElementosColunaCartela.append(cartelaModelo)
    
    colunaCartelas = ft.Container(content=ft.Column(controls=listElementosColunaCartela,
                                                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                                    scroll=ft.ScrollMode.AUTO),
                                expand=True)

    return colunaCartelas

def telaInicial():
    telaLadoRegistroNumero = ladoRegistroNumero()
    telaLadoCartelasCadastradas = ladoCartelasCadastradas()

    divisoriaVertical = ft.VerticalDivider(1,color=ft.Colors.GREY)

    divisaoTela = ft.Row(controls=[telaLadoRegistroNumero,divisoriaVertical,telaLadoCartelasCadastradas], expand=True, margin=0)
    tela = ft.Container(content=divisaoTela, expand=True, align=ft.Alignment.CENTER)

    return tela


