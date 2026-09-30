import flet as ft
import views.components.cartela as ct

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
    cartelas = ft.Container(content=ft.Text("Cartelas Registradas", size=25), alignment=ft.Alignment.CENTER)

    listaNumerosB = [7,13,3,8,15]
    listaNumerosI = [24,30,19,16,18]
    listaNumerosN = [39,38,44,34]
    listaNumerosG = [57,58,46,52,54]
    listaNumerosO = [67,70,64,75,74]
    codigo = 2688

    cartelaModelo = ct.criarCartela(codigo,listaNumerosB,listaNumerosI,listaNumerosN,listaNumerosG,listaNumerosO)

    colunaCartelas = ft.Container(content=ft.Column(controls=[cartelas, cartelaModelo, cartelaModelo, cartelaModelo],
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


