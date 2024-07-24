from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from googletrans import Translator

options = webdriver.ChromeOptions()
options.add_argument('--headless')

urls = [
    'https://ejemplo.com/',
    'https://ejemplo2.com/',
    'https://ejemplo3.com/',
    'https://ejemplo4.com/'
]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

translator = Translator()

for url in urls:
    driver.get(url)

    time.sleep(5)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    paragraphs = soup.find_all('p')

    translated_paragraphs = []
    for p in paragraphs:
        text = p.get_text(strip=True)
        try:
            translated_text = translator.translate(text, src='auto', dest='es').text
        except Exception as e:
            print(f"Error al traducir texto: {e}")
        translated_paragraphs.append(translated_text)

    filename = f"{url.strip('/').split('/')[-1]}_es.txt" 
    with open(filename, 'w', encoding='utf-8') as file:
        for text in translated_paragraphs:
            file.write(text + '\n')

driver.quit()

print("El contenido de todas las páginas ha sido traducido y guardado en archivos individuales en español.")
