# coding=utf-8

import argparse
from scrapper   import Scrapper
from scrolldown import ScrollDown
from concurrent.futures import ThreadPoolExecutor
import time
import sys


def help() -> None:
    print(
    '''
    Wollopop: An API to store Wallapop products into a JSON file.
    Usage: lanzador.py URL TIME (in minutes).
    Example: lanzador.py 'wallapop.com/example/' 10
    ''')

def main():
    args = sys.argv[1:]
    if '-h' in args or '--help' in args:
        help()
        sys.exit(-1)

    URL = sys.argv[1]
    TIEMPO = int(sys.argv[2])

    TIEMPO_FINAL = (time.time() + (60 * TIEMPO))
    srp = Scrapper(URL)
    scroll = ScrollDown(srp.driver, 800, TIEMPO_FINAL)

    with ThreadPoolExecutor() as executor:
        if (executor.submit(srp.aceptar_politicas_privacidad).done):
            executor.submit(scroll.desplazar_web)
            executor.submit(srp.get_fichero_datos, (TIEMPO_FINAL))

if __name__ == '__main__':
    main()