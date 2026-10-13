import flet as ft
import models.bancoDados 

def verificarNumeroPorLetra(numero:int, coordenada:str):
    coluna = coordenada.split(":")[0]
    if(coluna == "0" and numero >= 1 and numero <= 15):
        return False
    elif(coluna == "1" and numero >= 16 and numero <= 30):
        return False
    elif(coluna == "2" and numero >= 31 and numero <= 45):
        return False
    elif(coluna == "3" and numero >= 46 and numero <= 60):
        return False
    elif(coluna == "4" and numero >= 61 and numero <= 75):
        return False
    return True

def mensagemErro(coordenada:str):
    coluna = coordenada.split(":")[0]
    if(coluna == "0"):
        return "Número aceitos: 1-15"
    elif(coluna == "1"):
        return "Número aceitos: 16-30"
    elif(coluna == "2"):
        return "Número aceitos: 31-45"
    elif(coluna == "3"):
        return "Número aceitos: 46-60"
    elif(coluna == "4"):
        return "Número aceitos: 61-75"

# Função do pacote
def verificarValorDigitado(e: ft.Event[ft.TextField]):
    try:
        valor = int(e.control.value)
        coordenada= e.control.data
        if(verificarNumeroPorLetra(valor,coordenada)):
            e.control.label = mensagemErro(coordenada)
            e.control.border_color = ft.Colors.RED
        else:
            e.control.label = None
            e.control.border_color = ft.Colors.GREEN
    except:
        e.control.label = "Somente números"
        e.control.border_color = ft.Colors.RED

    e.page.update()

def verificarValorValido(valor, coordenada):
    try:
        valor = int(valor)
        if(verificarNumeroPorLetra(valor,coordenada)):
            return False
        else:
            return True
    except:
        return False

def verificaEAlertaSeTemCamposComValoresDuplicados(listaColunas):
    possuiValoresDuplicados = False
    for coluna in listaColunas:
            tamanhoLista = len(coluna.controls)
            contador = 0
            while contador < tamanhoLista:
                contadorComparador = contador + 1
                while contadorComparador < tamanhoLista:
                    if isinstance(coluna.controls[contador], ft.TextField) and isinstance(coluna.controls[contadorComparador], ft.TextField) and coluna.controls[contador].value != "":
                        if(coluna.controls[contador].value == coluna.controls[contadorComparador].value):
                            coluna.controls[contadorComparador].border_color = ft.Colors.RED
                            coluna.controls[contadorComparador].label = "Valor Duplicado"
                            possuiValoresDuplicados = True
                    contadorComparador+=1
                contador+=1
    return possuiValoresDuplicados

def verificaEAlertaSeTemCamposVazios(listaColunas):
        possuiVazios = False
        for coluna in listaColunas:
            for item in coluna.controls:
                if(isinstance(item, ft.TextField)):
                    if(item.value == None or item.value == ""):
                        possuiVazios = True
                        item.border_color = ft.Colors.YELLOW
                        item.label = "Não pode ficar vazio"
        return possuiVazios

# Função do pacote
def cadastrarCartela(e: ft.Event[ft.Button]):
    listaColunas = e.control.data[0]
    codigo = e.control.data[1].content.value
    codigoValido = codigo != ""
    textoMensagem = e.control.data[2]

    listaB = []
    listaI = []
    listaN = []
    listaG = []
    listaO = []

    contadorCorretos = 0
    contadorColunas = 0

    for coluna in listaColunas:
        for item in coluna.controls:
            if(item.data != None and verificarValorValido(item.value, item.data)):
                if(contadorColunas == 0):
                    listaB.append(item.value)
                elif(contadorColunas == 1):
                    listaI.append(item.value)
                elif(contadorColunas == 2):
                    listaN.append(item.value)
                elif(contadorColunas == 3):
                    listaG.append(item.value)
                elif(contadorColunas == 4):
                    listaO.append(item.value)
                contadorCorretos += 1
        contadorColunas += 1

    possuiValoresDuplicados = verificaEAlertaSeTemCamposComValoresDuplicados(listaColunas)
    possuiCamposVazios = verificaEAlertaSeTemCamposVazios(listaColunas)

    if(not codigoValido):
        e.control.data[1].content.border_color = ft.Colors.YELLOW
        e.control.data[1].content.label = "Não pode ficar vazio"
    else:
        e.control.data[1].content.border_color = ft.Colors.GREEN
        e.control.data[1].content.label = ""

    #criar Verificação se o código ja esta cadastrado
    if(contadorCorretos == 24 and codigoValido and not possuiValoresDuplicados and not possuiCamposVazios):
        models.bancoDados.adicionarCartela(codigo,listaB,listaI,listaN,listaG,listaO)
        textoMensagem.color = ft.Colors.GREEN
        textoMensagem.value = f"Cartela {codigo} cadastrado com suscesso"
        #limpar campos

    e.page.update()

def pegarListaCartelas():
    return models.bancoDados.pegarListaCartelas()

