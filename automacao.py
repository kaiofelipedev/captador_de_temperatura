from selenium import webdriver # para abrir o navegador
from selenium.webdriver.common.by import By # pegar o caminho dos elementos
from selenium.webdriver.common.keys import Keys # interagir com elementos
import datetime
import pandas as pd


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
        self.dados = pd.DataFrame({"Temperatura": [self.temperatura + ' ºC'],
                                    "Umidade": [self.umidade],
                                    "Data": [self.data],
                                    "Hora": [self.hora_atual]})
        self.dados.to_csv("historico.csv", index=False, mode="a", header=None)
        self.driver.quit()


#Navegador()
