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
    enter_code_sms = (By.XPATH, "//div[@class='input-container']//input[@id='code']")  # Almacena el campo para ingresar el código sms
    payment_method_button = (By.CLASS_NAME, 'pp-button.filled')  # Almacena el botón para Método de pago
    add_card_button = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled')
    # Almacena botón para agregar tarjeta de crédito
    card_number = (By.CLASS_NAME, 'card-number-input')  # Almacena el campo para número de tarjeta
    card_code = (By.CLASS_NAME, 'card-code-input')  # Almacena el campo para código de tarjeta
    close_window_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    ok_button_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > form > div.pp-buttons > button:nth-child(1)')
    # Almacena el botón para agregar datos de tarjeta de crédito y continuar
    card_select = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div:nth-child(3)')
    # Almacena la casilla para selccionar la tarjeta de crédito
    message_for_driver = (By.ID, 'comment')  # Almacena el campo Mensaje para el conductor
    blanket_scarves = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div')
    # Almacena la casilla Manta y pañuelos
    selector_blanket_scarves = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    checkbox_blanket_scarves = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
    # Almacena checkbox para seleccionar mantas y pañuelos
    ice_cream_counter = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')
    # Almacena el contador de helados
    add_ice_cream = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    # Almacena el botón para agregar helado
    find_taxi = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')  # Almacena botón para buscar un taxi
    arrival_time_driver = (By.CLASS_NAME, 'order-header-title')  # Almacena tiempo de llegada del conductor
    assigned_taxi_driver = (By.XPATH, '/html/body/div/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img')  # Almacena información del conductor