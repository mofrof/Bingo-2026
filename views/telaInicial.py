import flet as ft

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
                                                                grideNumerosSorteados],
                                                      horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
                                    expand=True)

    return colunaResultados

def ladoCartelasCadastradas():
    cartelas = ft.Container(content=ft.Text("Cartelas Registradas", size=25), alignment=ft.Alignment.CENTER)
    modeloNumero = ft.Container(content=ft.Text("01",size=30),
                                alignment=ft.Alignment.CENTER,
                                border=ft.Border.all(1,ft.Colors.GREEN),
                                expand=True)

    iconSistema = ft.Container(content=ft.Icon(icon=ft.Icons.TABLE_CHART,size=30),
                                alignment=ft.Alignment.CENTER,
                                expand=True)

    letraB = ft.Container(content=ft.Text("B", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)
    letraI = ft.Container(content=ft.Text("I", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)
    letraN = ft.Container(content=ft.Text("N", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)
    letraG = ft.Container(content=ft.Text("G", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)
    letraO = ft.Container(content=ft.Text("O", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)
    
    linhaCabecalho = ft.Container(ft.Row(controls=[letraB, letraI, letraN, letraG, letraO],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),alignment=ft.Alignment.CENTER)
    linhaGrid = ft.Container(ft.Row(controls=[modeloNumero,modeloNumero,modeloNumero,modeloNumero,modeloNumero],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),alignment=ft.Alignment.CENTER)
    linhaGridEspecial = ft.Container(ft.Row(controls=[modeloNumero,modeloNumero,iconSistema,modeloNumero,modeloNumero],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),alignment=ft.Alignment.CENTER)

    gridCartela = ft.Container(ft.Column(controls=[linhaCabecalho,linhaGrid,linhaGrid,linhaGridEspecial,linhaGrid,linhaGrid],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),alignment=ft.Alignment.CENTER)

    cartelaModelo = ft.Container(content=gridCartela,
                                 border=ft.Border.all(1,ft.Colors.GREY),
                                 padding=15,
                                 margin=50,
                                 expand=True
                                 )

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


