from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do WebDriver para Brave
service = Service("C:/Users/UFRN/Downloads/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.livrodosonho.com/significado-dos-sonhos'
driver.get(url)

try:
    letras_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.secondary.button"))
    )

    for i in range(len(letras_links)):
        # Recarrega os links das letras após cada interação
        letras_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.secondary.button"))
        )
        letra_link = letras_links[i]
        letra = letra_link.text.strip()
        print(f"Processando a letra: {letra}")

        letra_link.click()
        time.sleep(3)

        significados_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.secondary.button"))
        )

        significados_links = significados_links[::20]
        significados_dados = []

        for significado_link in significados_links:
            try:
                driver.execute_script("window.open(arguments[0].href, '_blank');", significado_link)
                WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
                driver.switch_to.window(driver.window_handles[1])

                titulo = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.post-entry p strong"))
                ).text

                conteudo = driver.find_element(By.CSS_SELECTOR, "div.post-entry").text
                significados_dados.append(f"{titulo}\n{conteudo}\n\n")

                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except Exception as e:
                print(f"Erro ao processar o link: {e}")
                if len(driver.window_handles) > 1:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

        with open(f"significados_letra_{letra}.txt", "w", encoding="utf-8") as file:
            file.writelines(significados_dados)

except Exception as e:
    print(f"Erro geral: {e}")
finally:
    driver.quit()
