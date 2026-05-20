from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import requests

def baixa_pdf():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://www.bcb.gov.br/publicacoes/focus")

    wait = WebDriverWait(driver, 20)

    botao = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="publicacao"]//download//a'
            )
        )
    )

    pdf_url = botao.get_attribute("href")

    print(f"URL PDF: {pdf_url}")

    driver.quit()

    response = requests.get(pdf_url)

    with open("focus.pdf", "wb") as f:
        f.write(response.content)

    print("Relatório Focus baixado com sucesso.")