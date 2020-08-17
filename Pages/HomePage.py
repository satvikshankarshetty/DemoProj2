class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.lnkSignOut_xpath = '''//a[text()='Sign Out']'''

    def logout(self):
        self.driver.find_element_by_xpath(self.lnkSignOut_xpath).click()
