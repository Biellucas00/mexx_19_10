from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pytest
from selenium.webdriver.support.ui import Select



class Chamados:
    def __init__(self, driver):
        self.driver = driver

    def botao_criar_chamados(self):
        # Espera até que o modal obscuring desapareça (substitua 'seletor_do_modal' pelo seletor apropriado)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, 'seletor_do_modal'))
            )
        except TimeoutException:
            pytest.fail("Modal ainda visível após o tempo limite estendido.")

        # Agora você pode clicar no botão de chamados
        elemento_chamados = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/main/div/div[1]/div[1]/a'))
        )
        self.driver.execute_script("arguments[0].click();", elemento_chamados)  # Use JavaScript para clicar no botão
        time.sleep(4)

    def preencher_organizacao(self):
        # Clique no campo combo-box
        combo_box = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/main/div/form/div/div[1]/div/div/div")
        combo_box.click()

        # Clique na opção esperada (combo-box-option-1)
        combo_box_option = self.driver.find_element(By.ID, "combo-box-option-1") ##selecione aqui o id da categoria (Recomendo utilizar o SELENIUM IDE)
        combo_box_option.click()
        time.sleep(4)

    def preencher_categoria(self):
        # ================================= #
        # CAMPO CATEGORIA #

        # Clique no campo combo-box
        combo_boxD = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/main/main/div/form/div/div[3]/div/div/div/input")
        combo_boxD.click()

        combo_box_option2 = self.driver.find_element(By.ID, "combo-box-option-1") ##selecione aqui o id da categoria (Recomendo utilizar o SELENIUM IDE)
        combo_box_option2.click()
        time.sleep(4)

    def preencher_titulo(self):
        self.driver.find_element(By.ID, 'title').send_keys("Monitor não liga 3 - aut")



    def preencher_descricao(self):
        self.driver.find_element(By.CLASS_NAME,'ql-editor').send_keys("monitor Não liga 3 - aut")

    def botao_enviar(self):
        # Esperar até que o botão de envio esteja visível e clicável
        elemento_enviar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.MuiButton-contained'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento_enviar)
        elemento_enviar.click()
        time.sleep(5)

    def retornar_menu_chamadas(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/header/div/button[1]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/nav/a[1]/div[2]/span').click()
        time.sleep(5)