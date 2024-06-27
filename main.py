import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import helpers
import UrbanRoutesPage

class TestUrbanRoutes:

    driver = webdriver.Chrome

    @classmethod
    # Configuración opciones de Chrome
    def setup_class(cls):
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920x1080")
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)




