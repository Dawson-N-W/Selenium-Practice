from Main_Page import MainPage


class LoggedInPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_new_account(self):
        self.driver.find_element_by_link_text("Open New Account").click()

    def account_overview(self):
        self.driver.find_element_by_link_text("Account Overview").click()

    def transfer_funds(self):
        self.driver.find_element_by_link_text("Transfer Funds").click()

    def bill_pay(self):
        self.driver.find_element_by_link_text("Bill Pay").click()

    def find_transactions(self):
        self.driver.find_element_by_link_text("Find Transactions").click()

    def update_contact_info(self):
        self.driver.find_element_by_link_text("Update Contact Info").click()

    def request_loan(self):
        self.driver.find_element_by_link_text("Request Loan").click()

    def log_out(self):
        self.driver.find_element_by_link_text("Log Out").click()

    def accounts(self):
        all_accounts = [balance.text for balance in self.driver.find_elements_by_class_name("ng-binding")]
        
        '''Take every 3rd element and combine into a list to signify each account'''
        accounts_ordered = [all_accounts[i:i + 3] for i in range(0, len(all_accounts), 3)]
        return accounts_ordered

    def click_account(self, account):
        a = [accounts[:1] for accounts in self.accounts()]
        '''Removing total account value'''
        if len(a) > 0:
            a.pop()
        '''Flattening a'''
        flat_a = [item for sublist in a for item in sublist]
        for item in flat_a:
            if item == account:
                self.driver.find_element_by_link_text(account).click()
                return
        raise ValueError


