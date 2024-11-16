from selenium import webdriver # para abrir o navegador
from selenium.webdriver.common.by import By # pegar o caminho dos elementos
from selenium.webdriver.common.keys import Keys # interagir com elementos
import datetime
import pandas as pd

#opcoes = webdriver.ChromeOptions()
#opcoes.add_experimental_option("detach", True)


class Navegador:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.campo_busca = self.driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        self.campo_busca.send_keys("clima são paulo")
        self.campo_busca.send_keys(Keys.ENTER)
        self.temperatura = self.driver.find_element(By.XPATH, '//*[@id="wob_tm"]').get_attribute("textContent")
        self.umidade = self.driver.find_element(By.XPATH, '//*[@id="wob_hm"]').get_attribute("textContent")
        self.hora = datetime.datetime.now()
        self.data = self.hora.strftime("%d/%m/%Y")
        self.hora_atual = self.hora.strftime("%H:%M:%S")
        self.dados = pd.DataFrame({self.temperatura: [], self.umidade: [], self.data: [], self.hora_atual: []})
        self.dados.to_csv("historico.csv", mode="a")
        #print(f"Temperatura: {self.temperatura}ºC\nUmidade: {self.umidade}\nData: {self.data}\nHora: {self.#hora_atual}")
        #self.driver.quit()

Navegador()