from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from Home_Page import MainPage



def main():
    driver = webdriver.Safari()
    driver.get("https://formy-project.herokuapp.com")
    driver.set_window_size(1600, 1000)
    main_page = MainPage(driver)
    date_picker_page = main_page.datepicker()
    date_picker_page.click_date(month=6, day=16, year=3600)
    time.sleep(5)




if __name__ == '__main__':
    main()
