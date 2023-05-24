from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
initial_url = "https://www.tucasa.com/compra-venta/viviendas/alicante/elche-elx/?r=&idz=0003.0009.9999.0002"


def parse_page(url, current_page): 
  print('Scrapeando página ' + str(current_page));
  browser.get(url)
  start_time = time.time()
  containers = browser.find_elements(By.CLASS_NAME, "contenedor-inmueble")
  elapsed_time = (time.time() - start_time) * 10

  i = 1
  for container in containers:
      print('-------')
      try:
          
          title = container.find_element(By.CLASS_NAME, "titulo-inmueble")
          precio_listado = container.find_element(By.CLASS_NAME, "precio-listado")
          num_habitaciones = container.find_element(By.CLASS_NAME, "num-habitaciones.hidden-xs")
          num_banos = container.find_element(By.CLASS_NAME, "num-baños")

          print("Vivvienda " + str(i))
          print(title.text)
          print(precio_listado.text)
          print(num_habitaciones.text)
          print(num_banos.text)
          i += 1
      except NoSuchElementException:
          continue
      print('-------')

  try:
    siguiente = browser.find_elements(By.CLASS_NAME, "btn-paginacion.br5.tr05")[1]
    current_page +=1
    print("Introduciendo un delay de " + str(elapsed_time) + " segundos")
    time.sleep(elapsed_time)
    parse_page(siguiente.get_attribute('href'), current_page)
  except NoSuchElementException:
    exit()


parse_page("https://www.tucasa.com/compra-venta/viviendas/alicante/elche-elx/?r=&idz=0003.0009.9999.0002", 1)