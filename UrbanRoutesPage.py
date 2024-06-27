from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


# Define localizadores y métodos
class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    log_image = (By.CLASS_NAME, 'logo-image')  # Almacena el logotipo de la aplicación
    button_round = (By.CLASS_NAME, 'button.round')  # Almacena botón para pedir un taxi
    comfort_select = (By.XPATH, "//div[@class='tcard-icon']//img[@alt='Comfort']")  # Almacena la opción para tarifa Comfort
    phone_number_button = (By.CLASS_NAME, 'np-text')  # Almacena botón Número de teléfono
    enter_phone_number = (By.ID, 'phone')  # Almacena campo para ingresar número de teléfono
    send_phone_number = (By.XPATH, "//div[@class='buttons']//button[text()='Siguiente']") # Almacena el botón para enviar el número de teléfono
    confirm_code = (By.CSS_SELECTOR,'#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)')
    # Almacena botón para confirmar código sms
    enter_code_sms = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[1]/div/input')  # Almacena el campo para ingresar el código sms
    payment_method_button = (By.XPATH, "//div[@class='pp-button filled']//div[text()='Método de pago']")  # Almacena el botón para Método de pago
    add_card_button = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled')
    # Almacena botón para agregar tarjeta de crédito
    card_number_field = (By.CLASS_NAME, 'card-number-input')  # Almacena el campo para número de tarjeta
    card_code_field = (By.CLASS_NAME, 'card-code-input')  # Almacena el campo para código de tarjeta
    close_window_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')  # Almacena el botoón para cerrar ventana Método de pago
    ok_button_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > form > div.pp-buttons > button:nth-child(1)')
    # Almacena el botón para agregar datos de tarjeta de crédito y continuar
    card_select = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div:nth-child(3)')
    # Almacena la casilla para selccionar la tarjeta de crédito
    message_for_driver_field = (By.ID, 'comment')  # Almacena el campo Mensaje para el conductor
    blanket_scarves = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div')
    # Almacena la casilla Manta y pañuelos
    selector_blanket_scarves = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    checkbox_blanket_scarves = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
    # Almacena checkbox para seleccionar mantas y pañuelos
    ice_cream_counter = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')
    # Almacena el contador de helados
    add_ice_cream = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    # Almacena el botón para agregar helado
    find_taxi_button = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')  # Almacena botón para buscar un taxi
    arrival_time_driver = (By.CLASS_NAME, 'order-header-title')  # Almacena tiempo de llegada del conductor
    assigned_taxi_driver = (By.XPATH, '/html/body/div/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img')  # Almacena información del conductor

# Métodos
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Hacer click en el botón Pedir un taxi
    def click_button_round(self):
        self.driver.find_element(*self.button_round).click()

    # Hacer click en tárifa Comfort
    def click_comfort_select(self):
        self.driver.find_element(*self.comfort_select).click()

    # Verifica que se ha seleccionado tárifa comfort
    def chek_comfort_select(self):
        elemento = self.driver.find_element(*self.blanket_scarves)
        comfort_is_chek = elemento.is_displayed()
        return comfort_is_chek

    # Hacer click en el campo para ingresar número de telefono
    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    # Ingresar número de teléfono
    def set_phone_number(self, number_phone):
        self.driver.find_element(*self.enter_phone_number).send_keys(number_phone)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_button).get_property('outerText')

    def click_send_phone_number(self):
        self.driver.find_element(*self.send_phone_number).click()

    # Enviar código sms
    def set_enter_code_sms(self, code_sms):
        self.driver.find_element(*self.enter_code_sms).send_keys(code_sms)

    # Hacer click para confirmar código sms
    def click_confirm_code(self):
        self.driver.find_element(*self.confirm_code).click()

    # Hacer click en el campo Método de pago
    def click_payment_method_button(self):
        self.driver.find_element(*self.payment_method_button).click()

    # Hacer click para añadir una tarjeta de crétido
    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    # Enviar datos de tarjeta de crédito
    def set_card_number_field(self, number_card):
        self.driver.find_element(*self.card_number_field).send.keys(number_card)

    def set_card_code_field(self, code_card):
        code_field = self.driver.find_element(*self.card_code_field)
        code_field.send_keys(code_card)
        code_field.send_keys(Keys.TAB)

    def get_card_number_field(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_card_code_field(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    # Hacer click para guardar tarjeta de crédito y continuar
    def click_ok_button_card(self):
        self.driver.find_element(*self.ok_button_card).click()

    def check_card_select(self):
        elemento = self.driver.find_element(*self.card_select)
        agree_tcard =elemento.is_displayed()
        return agree_tcard

    # Cerrar ventana Tarjeta de crédito
    def click_close_window_card(self):
        self.driver.find_element(*self.close_window_card).click()

    # Enviar mensaje para el conductor
    def set_message_for_driver_field(self, driver_message):
        self.driver.find_element(*self.message_for_driver_field).send_keys(driver_message)

    def get_message_for_driver_field(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

    # Seleccionar manta y pañuelos
    def click_blanket_scarves(self):
        self.driver.find_element(*self.blanket_scarves).click()

    def get_selector_blanket_scarves(self):
        return self.driver.find_element(*self.selector_blanket_scarves).get_property('value')

    # Agregar helados
    def click_add_ice_cream(self):
        self.driver.find_element(*self.add_ice_cream).click()

    def get_ice_cream_counter(self):
        return self.driver.find_element(*self.ice_cream_counter).get_property('outerText')

    # Pedir un taxi
    def click_find_taxi_button(self):
        self.driver.find_element(*self.find_taxi_button).click()

    def check_find_taxi_button(self):
        elemento = self.driver.find_element(*self.find_taxi_button)
        find_taxi_button = elemento.is_displayed()
        return find_taxi_button

    # Verificar información de taxista
    def check_assigned_taxi_driver(self):
        elemento = self.driver.find_element(*self.assigned_taxi_driver)
        assignned_taxi_driver = elemento.is_displayed()
        return assignned_taxi_driver

    def heck_arrival_time_driver(self):
        elemento = self.driver.find_element(*self.arrival_time_driver)
        arrival_time_driver_show = elemento.is_displayed()
        return arrival_time_driver_show