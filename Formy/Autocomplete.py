class AutoComplete:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def address(self, address):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('autocomplete').send_keys(address)

    def street_address_1(self, street_address):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('street_number').send_keys(street_address)

    def street_address_2(self, street_address):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('route').send_keys(street_address)

    def city(self, city):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('locality').send_keys(city)

    def state(self, state):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('administrative_area_level_1').send_keys(state)

    def zip_code(self, zip_code):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('postal_code').send_keys(zip_code)

    def country(self, country):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('country').send_keys(country)


