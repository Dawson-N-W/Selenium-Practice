import time
class DatePicker:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def enter_explicit_date(self, date):
        """Only mmddyyyy or mm/dd/yyyy are acceptable date inputs"""
        if len(date) == 8:
            for char in date:
                if not char.isdigit():
                    raise ValueError
            date = f"{date[0:2]}/{date[2:4]}/{date[4:]}"
        elif len(date) == 10:
            for i, char in enumerate(date):
                if i == 2 or i == 5:
                    if char != '/':
                        raise ValueError
                elif not char.isdigit():
                    raise ValueError
        else:
            raise ValueError

        print(date)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('datepicker').send_keys(date)

    def next(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/thead/tr[2]/th[3]").click()


    def previous(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/thead/tr[2]/th[1]").click()

    def date_picker_switch(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name("datepicker-switch").click()

    def click_to_years(self):
        self.driver.implicitly_wait(20)
        self.date_picker_switch()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/table/thead/tr[2]/th[2]').click()

    def click_month(self, index: int):
        if not 0 < index < 12:
            raise ValueError
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('datepicker').click()
        self.driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/table/tbody/tr/td/span{[index]}').click()

    def click_year(self, my_year: int):
        if len(str(my_year)) != 4:
            raise ValueError
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('datepicker').click()
        self.click_to_years()
        self.driver.implicitly_wait(20)
        years = self.driver.find_elements_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr/td/span')

        while my_year < int(years[0].text) or my_year > int(years[len(years) - 1].text):
            if my_year < int(years[0].text):
                self.previous()
                years = self.driver.find_elements_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr/td/span')
            else:
                self.next()
                years = self.driver.find_elements_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr/td/span')

        for year in years:
            if year.text == str(my_year):
                year.click()
                return
        raise LookupError

    def click_day(self, day: int):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('datepicker').click()
        calendar = []
        for i in range(1, 7):
            calendar.append(self.driver.find_elements_by_xpath(f'/html/body/div[2]/div[1]/table/tbody/tr[{i}]/td'))
        calendar = [one_day for week in calendar for one_day in week]
        for days in calendar:
            if days.text == str(day):
                days.click()
                return
        raise LookupError

    def click_date(self, *, month: int, day: int, year: int):
        self.click_year(year)
        self.click_month(month)
        self.click_day(day)




