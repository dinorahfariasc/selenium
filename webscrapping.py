import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

# iniciando uma sessão do webdriver
service = Service()

# webdriver.chromeoption é usado para definir a preferencia para o browser do chrome
options = webdriver.ChromeOptions()

# inicia a instancia do chrome webdriver 
driver = webdriver.Chrome(service=service, options=options)

url = 'https://books.toscrape.com/'

driver.get(url)

todosLivros = driver.find_elements(By.TAG_NAME,'a')[54:94:2]

# pegando apenas o titulo das tags a (livros)
titlesLivros = [title.get_attribute('title') for title in todosLivros]

print(titlesLivros)

# entrando em um link
todosLivros[0].click()
driver.back()

qntEstoque = driver.find_element(By.CLASS_NAME,'instock').text #nome original da classe = instock availabillity, passamos apenas oque está antes do espaço
print(qntEstoque)