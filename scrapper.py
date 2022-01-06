# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import time
import json
from colores import bcolors
import datetime

class Scrapper():
    
    def __init__(self, URL):
        self.URL = URL
        #self.options = Options()
        # self.options.add_argument("--headless")
        # self.options.add_argument("--disable-gpu")
        # self.options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.maximize_window()
        self.driver.get(self.URL)
        
    # Hace click en el boton de políticas de privacidad, en caso de dar una excepcion lo realiza hasta un maximo de 3 veces.
    def aceptar_politicas_privacidad(self, numero_intentos=3) -> None:
        if (numero_intentos > 0):
            try:
                self.driver.find_element(By.ID, 'didomi-notice-agree-button').click()
            except NoSuchElementException:
                time.sleep(2)
                return self.aceptar_politicas_privacidad(numero_intentos - 1)
    
    
    # Obtiene una lista con los productos de Wallapop.
    def get_fichero_datos(self, tiempo_final: int) -> list:
        
        lista_enlaces = []
        lista_productos = []

        # Evento para añadir los productos a la lista:
        while (time.time() < tiempo_final):
            try:                    
                productos = self.driver.find_elements(By.CLASS_NAME, 'ItemCardList__item')
                for producto in productos:
                    nombre  = (producto.find_element(By.CLASS_NAME, 'ItemCard__title').text)
                    precio  = (producto.find_element(By.CLASS_NAME, 'ItemCard__price').text)[:len(producto.find_element(By.CLASS_NAME, 'ItemCard__price').text) - 1]
                    desc    = (producto.find_element(By.CLASS_NAME, 'ItemCard__description').text)
                    enlace  = (producto.get_attribute('href'))
                    
                    if (enlace not in lista_enlaces):
                        if (',' not in precio) and ('.' not in precio):     
                            lista_enlaces.append(enlace)
                            lista_productos.append({
                                'NOMBRE':   nombre,
                                'PRECIO':   precio,
                                'DESC':     desc,
                                'ENLACE':   enlace
                            })
                            print(f'Numero Productos: [{bcolors.OKGREEN} {len(lista_productos)} {bcolors.ENDC}]')

            except Exception as e:
                print(f'{bcolors.WARNING}{e}{bcolors.ENDC}')
                time.sleep(2)

        return (self.crear_fichero_json(lista_productos))
    
    # Vuelca el contenido de la lista dentro de un fichero JSON.
    def crear_fichero_json(self, lista_productos: list) -> None:
        fecha = datetime.date.today().strftime("%Y-%m-%d")
        with open(f'./json_files/wallapop_{fecha}.json', 'w') as file:
            json.dump(lista_productos, file, ensure_ascii=False, indent=4)
        print(f'\n{bcolors.OKGREEN}{bcolors.UNDERLINE}- Fichero generado con exito.{bcolors.ENDC}\n{bcolors.OKCYAN}PATH: ./json_files/wallapop_{fecha}.json{bcolors.ENDC}')