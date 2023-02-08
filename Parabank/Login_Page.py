from Main_Page import MainPage
from Logged_In import LoggedInPage


class LoginPage(MainPage):
    _username = None
    _password = None

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @username.setter
    def username(self, username):
        self._username = username
        self.driver.find_element_by_name("username").send_keys(self._username)

    @password.setter
    def password(self, password):
        self._password = password
        self.driver.find_element_by_name("password").send_keys(self._password)

    def forgot_login_info(self):
        self.driver.find_element_by_link_text("Forgot login info?").click()

    def register(self):
        self.driver.find_element_by_link_text("Register").click()

    def login(self):
        if self._username is not None and self._password is not None:
            self.driver.find_element_by_xpath('//*[@id="loginPanel"]/form/div[3]/input').click()
            return LoggedInPage(self.driver)
