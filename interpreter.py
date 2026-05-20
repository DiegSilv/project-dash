import pdfplumber
import pandas as pd
import re
from datetime import datetime

arquivo = "focus.pdf"

texto = ""

with pdfplumber.open(arquivo) as pdf:

    for pagina in pdf.pages:

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

data_coleta = datetime.now().strftime("%Y-%m-%d")

for linha in linhas:

    for indicador in indicadores:

        if linha.startswith(indicador):

            numeros = re.findall(r"\d+,\d+", linha)

            numeros = numeros[:12]

            for i, ano in enumerate(anos):

                inicio = i * 3

                if inicio + 2 < len(numeros):

                    periodos = {
                        "Há 4 semanas": numeros[inicio],
                        "Há 1 semana": numeros[inicio + 1],
                        "Hoje": numeros[inicio + 2]
                    }

                    for periodo, valor in periodos.items():

                        dados.append({
                            "Data_Coleta": data_coleta,
                            "Indicador": indicador,
                            "Ano": ano,
                            "Periodo": periodo,
                            "Valor": float(valor.replace(",", "."))
                        })

df = pd.DataFrame(dados)

print(df)

df.to_csv(
    "focus.csv",
    index=False,
    sep=";"
)
print("CSV gerado com sucesso.")