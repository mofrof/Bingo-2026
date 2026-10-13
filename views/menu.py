import flet as ft
import views.screens as sc

def ao_mudar_aba(e :ft.Event[ft.Tabs]):
    indice = e.control.selected_index
    estrutura_pagina = e.control.data
    if indice == 0:  # Aba Inicial
        estrutura_pagina.controls[0] = sc.telaInicial()
        estrutura_pagina.update()
    elif indice == 2:  # Aba Gerenciar Cartelas
        estrutura_pagina.controls[2] = sc.telaGerenciaCartelas()
        estrutura_pagina.update()


def criarMenu():
    menu1 = ft.Tab(label="Tela Inicial", icon= ft.Icons.HOME_FILLED)
    menu2 = ft.Tab(label="Cadastrar Cartelas", icon= ft.Icons.NOTE_ADD)
    menu3 = ft.Tab(label="Gerenciar Cartelas", icon= ft.Icons.EDIT_NOTE_OUTLINED)

    estruturaMenu = ft.TabBar(tabs=[menu1,menu2,menu3])

    tela1 = sc.telaInicial()
    tela2 = sc.telaCadastroCartela()
    tela3 = sc.telaGerenciaCartelas()

    estruturaPagina = ft.TabBarView(controls=[tela1, tela2, tela3,],
                                    expand=True)

    estruturaMenuPagina = ft.Column(controls=[estruturaMenu,estruturaPagina],
                              expand=True)

    paginaComMenu = ft.Tabs(length=3,
                           expand=True,
                           content = estruturaMenuPagina,
                           on_change=ao_mudar_aba,
                           data= estruturaPagina
    )

    return paginaComMenu