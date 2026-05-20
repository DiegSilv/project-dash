import pdfplumber
import pandas as pd
import re

arquivo = "focus.pdf"

texto = ""

with pdfplumber.open(arquivo) as pdf:

    for pagina in pdf.pages:

        #if pra pegar só os dados anuais, n queria os mensais

        if pagina.page_number == 1:

            conteudo = pagina.extract_text()

            if conteudo:
                texto += conteudo + "\n"

linhas = texto.split("\n")

dados = []

indicadores = [
    "IPCA (variação %)",
    "PIB Total",
    "Câmbio (R$/US$)",
    "Selic",
    "IGP-M"
]

anos = [2026, 2027, 2028, 2029]

for linha in linhas:

    for indicador in indicadores:

        if linha.startswith(indicador):

            numeros = re.findall(r"\d+,\d+", linha)

            # pega somente os 12 primeiros números
            numeros = numeros[:12]

            for i, ano in enumerate(anos):

                inicio = i * 3

                if inicio + 2 < len(numeros):

                    dados.append({
                        "Indicador": indicador,
                        "Ano": ano,
                        "Há 4 semanas": numeros[inicio],
                        "Há 1 semana": numeros[inicio + 1],
                        "Hoje": numeros[inicio + 2]
                    })

df = pd.DataFrame(dados)

print(df)

df.to_csv("focus.csv", index=False, sep=";")