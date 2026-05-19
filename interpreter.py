import pdfplumber

arquivo = "focus.pdf"

with pdfplumber.open(arquivo) as pdf:

    for pagina in pdf.pages:
        texto = pagina.extract_text()

        if texto:
            print(texto + "\n") 
