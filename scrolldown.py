# coding=utf-8

import time
from selenium.webdriver.common.by import By

class ScrollDown():

    def __init__(self, driver, px_desplazamiento, tiempo_final):
        self.driver = driver
        self.px_desplazamiento = px_desplazamiento
        self.tiempo_minutos = tiempo_final

    def desplazar_web(self):
        while (time.time() < self.tiempo_minutos):
            # Evento para pulsar el botón 'Mostrar más productos'
            try:
                if len(self.driver.find_elements(By.XPATH, './/*[@id="btn-load-more"]/button')) > 0:
                    self.driver.find_element(By.XPATH, './/*[@id="btn-load-more"]/button').click()
            except Exception:
                time.sleep(2)
                return self.desplazar_web()

            # Eveto para desplazar la web
            self.px_desplazamiento += 800
            self.driver.execute_script('window.scrollTo(0, {})'.format(self.px_desplazamiento))
            time.sleep(1)
                