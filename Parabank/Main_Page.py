class MainPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def about_us(self):
        self.driver.find_element_by_link_text("About Us").click()

    def services(self):
        self.driver.find_element_by_link_text("Services").click()

    def products(self):
        self.driver.find_element_by_link_text("Products").click()

    def locations(self):
        self.driver.find_element_by_link_text("Locations").click()

    def admin_page(self):
        self.driver.find_element_by_link_text("Admin Page").click()

    def forum(self):
        self.driver.find_element_by_link_text("Forum").click()

    def site_map(self):
        self.driver.find_element_by_link_text("Site Map").click()

    def contact_us(self):
        self.driver.find_element_by_link_text("Contact Us").click()

    def parasoft(self):
        self.driver.find_element_by_xpath('//*[@id="footerPanel"]/ul[2]/li[2]/a').click()

    def home(self):
        self.driver.find_element_by_link_text("home").click()
