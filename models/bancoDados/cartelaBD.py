listaCartelas = [
{
    "codigo": 2600,
    "B":[7,13,3,8,15],
    "I":[24,30,19,16,18],
    "N":[39,38,44,34],
    "G":[57,58,46,52,54],
    "O":[67,70,64,75,74],
},
{
    "codigo": 2601,
    "B":[3,8,11,12,2],
    "I":[23,26,27,20,18],
    "N":[36,41,35,44],
    "G":[57,47,48,53,56],
    "O":[62,63,68,71,72],
},
{
    "codigo": 2602,
    "B":[7,14,4,9,6],
    "I":[26,22,24,20,28],
    "N":[40,34,36,35],
    "G":[58,55,46,52,49],
    "O":[73,68,72,74,64],
},
]

def encontrar_cartela(codigo):
    indice = 0
    for item in listaCartelas:
        if item["codigo"] == codigo:
            return indice
        indice += 1

    return None

def pegarListaCartelas():
    return listaCartelas

def adicionarCartela(codigo,B,I,N,G,O):
    cartela = {"codigo": codigo,
                  "B":B,
                  "I":I,
                  "N":N,
                  "G":G,
                  "O":O
                  }
    listaCartelas.append(cartela)

def removerCartela(indiceExcluir):
    listaCartelas.pop(indiceExcluir)

def alterarCartela(codigo,B,I,N,G,O):
    indiceAlterar = encontrar_cartela(codigo)
    cartelaAlterada = {"codigo": codigo,
                  "B":B,
                  "I":I,
                  "N":N,
                  "G":G,
                  "O":O
                  }
    listaCartelas[indiceAlterar] = cartelaAlterada


if(__name__ == "__main__"):
    adicionarCartela(2603,[0,0,0,0,0], [1,1,1,1,1], [2,2,2,2], [3,3,3,3,3], [4,4,4,4,4])
    print(pegarListaCartelas())
    removerCartela(2600)
    print(pegarListaCartelas())
    alterarCartela(2601,[5,5,5,5,5], [6,6,6,6,6], [7,7,7,7], [8,8,8,8,8], [9,9,9,9,9])
    print(pegarListaCartelas())
