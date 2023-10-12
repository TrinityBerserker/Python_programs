from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def buscar_y_clickear_furni():
    # Inicializar el navegador
    driver = webdriver.Chrome('/ruta/al/driver/chrome')  # Reemplazar con la ubicación de tu controlador de Chrome

    # Abrir la sala
    driver.get('https://www.ejemplo.com/sala')  # Reemplazar con la URL de la sala que deseas acceder

    # Esperar a que la página se cargue completamente
    time.sleep(5)

    # Encontrar el elemento del furni específico
    furni = driver.find_element_by_xpath('//xpath/del/furni')  # Reemplazar con el XPath del furni específico que deseas buscar

    # Realizar clics en el furni
    for _ in range(10):
        ActionChains(driver).move_to_element(furni).click().perform()
        time.sleep(1)

    # Cerrar el navegador
    driver.quit()

# Ejecutar la función
buscar_y_clickear_furni()
