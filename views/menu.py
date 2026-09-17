import flet as ft
import views

def criarMenu():
    menu1 = ft.Tab(label="Tela Inicial", icon= ft.Icons.HOME_FILLED)
    menu2 = ft.Tab(label="Cadastrar Cartelas", icon= ft.Icons.NOTE_ADD)
    menu3 = ft.Tab(label="Alterar Cartelas", icon= ft.Icons.EDIT_NOTE_OUTLINED)
    menu4 = ft.Tab(label="Deletar Cartelas", icon= ft.Icons.DELETE)

    estruturaMenu = ft.TabBar(tabs=[menu1,menu2,menu3, menu4])

    tela1 = views.telaInicial()
    tela2 = views.telaCadastroCartela()
    tela3 = ft.Text("Alterar Cartelas")
    tela4 = ft.Text("Deletar Cartelas")

    estruturaPagina = ft.TabBarView(controls=[tela1, tela2, tela3, tela4],
                                    expand=True)

    estruturaMenuPagina = ft.Column(controls=[estruturaMenu,estruturaPagina],
                              expand=True)

    paginaComMenu = ft.Tabs(length=3,
                           expand=True,
                           content = estruturaMenuPagina
                           
    )

    return paginaComMenu