import flet as ft
import models

def telaCadastroCartela():

    titulo = ft.Container(content=ft.Text("Cadastro Cartela", size=35, weight=ft.FontWeight.BOLD), alignment=ft.Alignment.CENTER)

    codCartelaTextFild = ft.Container(content= ft.TextField(label="Código Cartela", border_color=ft.Colors.WHITE), alignment=ft.Alignment.CENTER_LEFT)

    letraB = ft.Container(content=ft.Text("B", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)
    letraI = ft.Container(content=ft.Text("I", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)
    letraN = ft.Container(content=ft.Text("N", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)
    letraG = ft.Container(content=ft.Text("G", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)
    letraO = ft.Container(content=ft.Text("O", size=25, weight=ft.FontWeight.BOLD), align=ft.Alignment.CENTER)
    
    listaLetras = [letraB, letraI, letraN, letraG, letraO]
    listaLinha = []
    listaColuna = []

    for i in range(5):
        listaColuna.append(listaLetras[i])
        for j in range(5):
            textFild = None
            if i== 2 and j == 2:
                textFild = ft.Container(content=ft.Icon(icon=ft.Icons.TABLE_CHART,size=50),
                                alignment=ft.Alignment.CENTER)
            else:
                textFild = ft.TextField(label=f"{i}:{j}", data=f"{i}:{j}",
                                        border_color=ft.Colors.WHITE,
                                        on_change=models.verificarValorDigitado
                                        )
            listaColuna.append(textFild)
        coluna = ft.Column(controls=listaColuna, expand=True, alignment=ft.Alignment.CENTER)
        listaLinha.append(coluna)
        listaColuna = []

    cartelaBingo = ft.Row(controls=listaLinha, expand=True, alignment=ft.MainAxisAlignment.CENTER)

    textoErro = ft.Text("", size=25, color=ft.Colors.RED)

    button = ft.Button(content=ft.Text("Cadastrar Cartela", size=25, weight=ft.FontWeight.BOLD),
                       align=ft.Alignment.BOTTOM_RIGHT,
                       height=50,
                       on_click=models.cadastrarCartela,
                       data=[listaLinha,codCartelaTextFild,textoErro])

    linhaButao = ft.Row(controls=[textoErro, button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, margin=0)

    conteudo = ft.Column(controls=[titulo, codCartelaTextFild ,cartelaBingo, linhaButao], horizontal_alignment=ft.CrossAxisAlignment.STRETCH, margin=0)

    container = ft.Container(content=conteudo, expand=True)

    return container