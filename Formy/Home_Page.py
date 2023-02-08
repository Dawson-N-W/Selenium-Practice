from Autocomplete import AutoComplete
from Buttons import Buttons
from CheckBox import CheckBox
from DatePicker import DatePicker


class MainPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def auto_complete(self):
        links = [link for link in self.driver.find_elements_by_link_text("Autocomplete")]
        links[1].click()
        return AutoComplete(self.driver)

    def buttons(self):
        links = [link for link in self.driver.find_elements_by_link_text("Buttons")]
        links[1].click()
        return Buttons(self.driver)

    def checkbox(self):
        links = [link for link in self.driver.find_elements_by_link_text("Checkbox")]
        links[1].click()
        return CheckBox(self.driver)

    def datepicker(self):
        links = [link for link in self.driver.find_elements_by_link_text("Datepicker")]
        links[1].click()
        return DatePicker(self.driver)

    def drag_and_drop(self):
        self.driver.find_element_by_link_text("Drag and Drop").click()

    def dropdown(self):
        self.driver.find_element_by_link_text("Dropdown").click()

    def enabled_and_disabled_elements(self):
        self.driver.find_element_by_link_text("Enabled and disabled elements").click()

    def file_upload(self):
        self.driver.find_element_by_link_text("File Upload").click()

    def key_and_mouse_press(self):
        self.driver.find_element_by_link_text("Key and Mouse Press").click()

    def modal(self):
        self.driver.find_element_by_link_text("Modal").click()

    def page_scroll(self):
        self.driver.find_element_by_link_text("Page Scroll").click()

    def radio_button(self):
        self.driver.find_element_by_link_text("Radio Button").click()

    def switch_window(self):
        self.driver.find_element_by_link_text("Switch Window").click()

    def complete_web_form(self):
        self.driver.find_element_by_link_text("Complete Web Form").click()
