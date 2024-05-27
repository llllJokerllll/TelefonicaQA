from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def get_texts_from_section(driver, section_name):
    # Hacer clic en la sección
    section_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, section_name))
    )
    section_link.click()
    
    # Esperar a que los elementos con la clase "text" sean visibles
    time.sleep(15)
    texts = WebDriverWait(driver, 15).until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, "text"))
    )
    
    # Extraer y retornar los textos
    return [text.text for text in texts]

def main():
    # Configura ChromeOptions
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-fullscreen")

    # Inicializa el ChromeDriver con las opciones
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://bcncgroup.com/")
    
    try:
        # Espera hasta que el botón de cookies sea visible y haz clic en él
        boton_cookies = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cc-btn.cc-deny"))
        )
        boton_cookies.click()
        print("Botón de cookies encontrado y clicado")
    except Exception as e:
            print(f"Error: {e}")

    # Extraer textos de las secciones
    sections = ["HOME", "WHO WE ARE"]
    extracted_texts = {}
    time.sleep(15)

    for section in sections:
        extracted_texts[section] = get_texts_from_section(driver, section)
    
    # Guardar los resultados en un archivo JSON
    with open("extracted_texts.json", "w") as f:
        json.dump(extracted_texts, f, indent=4)
    
    # Esperar unos segundos antes de cerrar el navegador
    time.sleep(15)
    driver.quit()

    # Comparar los textos guardados con los actuales
    with open("extracted_texts.json", "r") as f:
        saved_texts = json.load(f)

    # Inicializa el ChromeDriver con las opciones
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://bcncgroup.com/")
    
    try:
        # Espera hasta que el botón de cookies sea visible y haz clic en él
        boton_cookies = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cc-btn.cc-deny"))
        )
        boton_cookies.click()
        print("Botón de cookies encontrado y clicado")
    except Exception as e:
            print(f"Error: {e}")

    time.sleep(15)
    
    current_texts = {}
    for section in sections:
        current_texts[section] = get_texts_from_section(driver, section)

    driver.quit()

    for section in sections:
        assert saved_texts[section] == current_texts[section], f"Textos de la sección {section} no coinciden."

    print("Todos los textos coinciden con los datos guardados.")

if __name__ == "__main__":
    main()
