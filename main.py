from extractor import baixa_pdf
from interpreter import monta_csv

def main():

    try:

        print("Baixando relatório Focus...")
        baixa_pdf()

        print("Gerando CSV...")
        monta_csv()

        print("Concluído com sucesso.")

    except Exception as erro:

        print(f"ERRO: {erro}")

if __name__ == "__main__":
    main()