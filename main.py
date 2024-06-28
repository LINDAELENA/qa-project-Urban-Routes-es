import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ConfirmationCode
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

    # Test 1 Configurar la dirección
    def test1_configurar_direccion(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)  # Almacena el archivo UrbanRoutesPage
        self.driver.get(data.urban_routes_url)  # Abre URL de Urban Routs
        ConfirmationCode.wait_visibility_of_element(self.driver, routes_page.log_image, 3) # Espera a que cargue el logotipo
        address_from = data.address_from  # Iguala la variable de dirección de origen
        address_to = data.address_to  # Iguala la variable de dirección de destino
        routes_page.set_from(address_from)  # Llama a set_from de UrbanRoutesPage
        routes_page.set_to(address_to)  # Llama a set_to de UrbanRoutesPage
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to