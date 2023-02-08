from selenium import webdriver
import time
from Login_Page import LoginPage



def main():
    driver = webdriver.Safari()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    front_page = LoginPage(driver)
    front_page.username = "john"
    front_page.password = "demo"
    logged_in_page = front_page.login()
    time.sleep(2)
    logged_in_page.click_account('13011')
    time.sleep(10)


if __name__ == '__main__':
    main()