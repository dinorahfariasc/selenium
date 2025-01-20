from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do WebDriver para Brave
# Caminho do ChromeDriver
service = Service("C:/Program Files/chromedriver-win64/chromedriver.exe") #"C:/Program Files/chromedriver-win64/chromedriver.exe" // C:/Users/UFRN/Downloads/chromedriver-win64/chromedriver.exe"

# Configurações do navegador Brave
options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" #

# Inicializa a instância do Brave WebDriver
driver = webdriver.Chrome(service=service, options=options)

# URL inicial
url = 'https://www.livrodosonho.com/significado-dos-sonhos'
driver.get(url)

# Espera carregar todos os elementos com links para sonhos
try:
    # Localiza os elementos de links de sonhos
    sonhos_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.secondary.button"))
    )
    
    # Armazena os dados coletados
    sonhos_dados = []

    # Itera sobre cada link de sonho
    for link in sonhos_links:
        # Abre o link em uma nova aba
        driver.execute_script("window.open(arguments[0].href, '_blank');", link)
        driver.switch_to.window(driver.window_handles[1])  # Muda para a nova aba

        # Aguarda o carregamento do conteúdo do sonho


    # Salva os dados em um arquivo TXT
    # with open("Sonhos_A.txt", "w", encoding="utf-8") as file:
    #     file.writelines(sonhos_dados)

except Exception as e:
    print(f"Erro geral: {e}")
finally:
    # Fecha o navegador
    driver.quit()
