from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests

def baixa_pdf():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://www.bcb.gov.br/publicacoes/focus")

    botao = driver.find_element(By.XPATH,'//download//a')

    pdf_url = botao.get_attribute("href")

    driver.quit()

    response = requests.get(pdf_url)

    with open("focus.pdf", "wb") as f:
        f.write(response.content)

    print("Relatório Focus baixado com sucesso.")