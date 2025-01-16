import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caminho do ChromeDriver
service = Service("C:/Users/UFRN/Downloads/chromedriver-win64/chromedriver.exe")

# Configurações do navegador Brave
options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# Inicializa a instância do Brave WebDriver
driver = webdriver.Chrome(service=service, options=options)

# URL do site
url = 'https://www.livrodosonho.com/significado-dos-sonhos'
driver.get(url)

# Procura e clica no link "Sonhos A"
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sonhos A"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    print(element.text)
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Fecha o navegador após o término do script
    driver.quit()
