import flet as ft

def criarModeloNumero(numero):
        modeloNumero = ft.Container(content=ft.Text(numero,size=30),
                                alignment=ft.Alignment.CENTER,
                                border=ft.Border.all(1,ft.Colors.GREEN),
                                expand=True)
        return modeloNumero

def criarCartela(codigo,listaNumerosB, listaNumerosI, listaNumerosN,
                  listaNumerosG, listaNumerosO, linhasButao = None):
    iconSistema = ft.Container(content=ft.Icon(icon=ft.Icons.TABLE_CHART,size=30),
                                alignment=ft.Alignment.CENTER,
                                expand=True)

    codigoTexto = ft.Container(content=ft.Text(f"Código: {codigo}", size=15, weight=ft.FontWeight.BOLD), expand=True)
    
    letraB = ft.Container(content=ft.Text("B", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)
    letraI = ft.Container(content=ft.Text("I", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)
    letraN = ft.Container(content=ft.Text("N", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)
    letraG = ft.Container(content=ft.Text("G", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)
    letraO = ft.Container(content=ft.Text("O", size=25, weight=ft.FontWeight.BOLD),alignment=ft.Alignment.CENTER, expand=True)

    linhaCodigo = ft.Container(ft.Row(controls=[codigoTexto],alignment=ft.MainAxisAlignment.START, expand=True),expand=True)
    linhaCabecalho = ft.Container(ft.Row(controls=[letraB, letraI, letraN, letraG, letraO],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),alignment=ft.Alignment.CENTER)
    listaLinhasGrid = [linhaCodigo,linhaCabecalho]

    for numLinha in range(5):
        if(numLinha < 2):
            linhaGrid = ft.Container(ft.Row(controls=[criarModeloNumero(listaNumerosB[numLinha]),
                                                      criarModeloNumero(listaNumerosI[numLinha]),
                                                      criarModeloNumero(listaNumerosN[numLinha]),
                                                      criarModeloNumero(listaNumerosG[numLinha]),
                                                      criarModeloNumero(listaNumerosO[numLinha])],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN),alignment=ft.Alignment.CENTER)
        elif(numLinha == 2):
            linhaGrid = ft.Container(ft.Row(controls=[criarModeloNumero(listaNumerosB[numLinha]),
                                                              criarModeloNumero(listaNumerosI[numLinha]),
                                                              iconSistema,
                                                              criarModeloNumero(listaNumerosG[numLinha]),
                                                              criarModeloNumero(listaNumerosO[numLinha])],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),alignment=ft.Alignment.CENTER)
        else:
            linhaGrid = ft.Container(ft.Row(controls=[criarModeloNumero(listaNumerosB[numLinha]),
                                                      criarModeloNumero(listaNumerosI[numLinha]),
                                                      criarModeloNumero(listaNumerosN[numLinha-1]),
                                                      criarModeloNumero(listaNumerosG[numLinha]),
                                                      criarModeloNumero(listaNumerosO[numLinha])],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN),alignment=ft.Alignment.CENTER)
        listaLinhasGrid.append(linhaGrid)

    if linhasButao != None:
         listaLinhasGrid.append(linhasButao)

    gridCartela = ft.Container(ft.Column(controls=listaLinhasGrid, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),alignment=ft.Alignment.CENTER)

    cartelaModelo = ft.Container(content=gridCartela,
                                 border=ft.Border.all(1,ft.Colors.GREY),
                                 padding=15,
                                 margin=50,
                                 expand=True
                                 )

    return cartelaModelo