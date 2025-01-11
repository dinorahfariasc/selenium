import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# iniciando uma sessão do webdriver
service = Service()

# webdriver.chromeoption é usado para definir a preferencia para o browser do chrome
options = webdriver.ChromeOptions()

# inicia a instancia do chrome webdriver 
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.livrodosonho.com/significado-dos-sonhos'

driver.get(url)

# procure pelo titulo do elemento, clicando no link

element = driver.find_element(By.LINK_TEXT, "Sonhos A")
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
print(element.text)

# # pegando apenas o titulo das tags a (livros)
# titlesLivros = [title.get_attribute('title') for title in todosLivros]

# print(titlesLivros)

# # entrando em um link
# todosLivros[2].click()
# driver.back()

# qntEstoque = driver.find_element(By.CLASS_NAME,'instock').text #nome original da classe = instock availabillity, passamos apenas oque está antes do espaço
# print(qntEstoque)