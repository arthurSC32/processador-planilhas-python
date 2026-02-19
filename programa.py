import pandas as pd
caminho_arquivo="data/entrada.xlsx"
quantidade_minima=50

def lerArquivo(caminho_arquivo):
   DF = pd.read_excel(caminho_arquivo)
   return DF


df=lerArquivo(caminho_arquivo)


def calcular_total(DF):
    DF["total"]=DF["preco"]*DF["quantidade"]
    print(DF)
    return DF

def verificar_quantidade_baixa(DF):
  produtos_baixo=DF.loc[DF["quantidade"]<=quantidade_minima,["produtos"]]
  print("produtos com quantidade baixa",produtos_baixo)
  resposta=input("que gerar um relatorio dos produtos com quantidade abaixo do ideal s para sim")
  if (resposta == "s"):
      produtos_baixo.to_excel("data/produtos_baixo.xlsx", index=False)
  return produtos_baixo




df =calcular_total(df)
lista_itens_quantidade_baixa=verificar_quantidade_baixa(df)













