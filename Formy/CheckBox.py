class CheckBox:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def check_box_1(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("checkbox-1").click()

    def check_box_2(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("checkbox-2").click()

    def check_box_3(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("checkbox-3").click()

    def is_selected(self, index) -> bool:
        if index < 1 or index > 3:
            raise IndexError
        self.driver.implicitly_wait(20)
        box = self.driver.find_element_by_id(f"checkbox-{index}")
        return box.is_selected()
