from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.idealista.com/venta-viviendas/elche-elx/elche-ciudad/"

browser.get(url)

page_source = browser.page_source

print(page_source)



time.sleep(20)

"""
El ejercicio se puede hacer correctamente.

Al entrar al portal de idealista con selenium aparece el 
mismo código que aparece con un navegador normal.

Tras ver la solución en el ordenador del profesor, 
entiendo que sale un captcha cuando realizas varias 
peticiones con BeautifulSoup, como este no manda el user agent
idealista muestra un captcha para verificar que el usuario 
no es un robot.
"""