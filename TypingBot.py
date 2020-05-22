from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Listener
from bs4 import BeautifulSoup
import time

typingTestUrl = "https://www.typingtest.com/test.html?textfile=words.txt&minutes=1&mode=words&result_url=result.html"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(typingTestUrl)

def on_release(key):
    if key == Key.f2:
        start()


def start():
    try:
        
    except:
        print(Exception)


with Listener(on_release=on_release) as listener:
    listener.join()
