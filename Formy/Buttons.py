class Buttons:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def primary(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('btn-primary').click()

    def success(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('btn-success').click()

    def info(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('btn-info').click()

    def warning(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('btn-warning').click()

    def danger(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('btn-danger').click()

    def link(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('btn-link').click()

    def _get_directional_buttons(self):
        self.driver.implicitly_wait(20)
        return self.driver.find_elements_by_xpath(f'/html/body/div/form/div[2]/div/div/div/button')

    def left(self):
        left_button = self._get_directional_buttons()[0]
        left_button.click()

    def middle(self):
        middle_button = self._get_directional_buttons()[1]
        middle_button.click()

    def right(self):
        right_button = self._get_directional_buttons()[2]
        right_button.click()

    def one(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//button[text() = "1"]').click()


    def two(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//button[text() = "2"]').click()


    def drop_down(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("btnGroupDrop1").click()

    def drop_down_link_1(self):
        self.drop_down()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_link_text("Dropdown link 1").click()

    def drop_down_link_2(self):
        self.drop_down()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_link_text("Dropdown link 2").click()
