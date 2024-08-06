# -*- coding: utf-8 -*-

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# URL de la página para extraer los datos.
PAGINA_PRINCIPAL = "https://www.scrapethissite.com/pages/forms/"


# Inicializar el navegador
navegador = webdriver.Chrome()
navegador.get(PAGINA_PRINCIPAL)  
navegador.implicitly_wait(10)

datos = []
equipos = navegador.find_elements(By.CLASS_NAME, 'team')

for equipo in equipos:
    nombre = equipo.find_element(By.CLASS_NAME, 'name')
    year = equipo.find_element(By.CLASS_NAME, 'year')
    wins = equipo.find_element(By.CLASS_NAME, 'wins')
    losses = equipo.find_element(By.CLASS_NAME, 'losses')
  

    datos.append({
        'Nombre': nombre.text,
        'Año': year.text,
        'Victorias': wins.text,
        'Derrotas': losses.text
    })

navegador.quit()

# Crear un DataFrame con los datos extraídos
df = pd.DataFrame(datos)
print(df)

# Guardar los datos en un archivo Excel
ruta = "C:/Users/Jess1/Downloads/Datos_proyecto_nayib.xlsx"
df.to_excel(ruta, index=False)
