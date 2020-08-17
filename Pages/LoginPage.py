class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.lnkSignin_xpath='''//a[text()='Sign In']'''
        self.txtUsername_name = "username"
        self.txtPassword_name = "password"
        self.btnLogin_name = "signon"
        print('Login page object created')

    def login(self, username, password):
        self.driver.find_element_by_xpath(self.lnkSignin_xpath).click()
        self.driver.find_element_by_name(self.txtUsername_name).send_keys(username)
        self.driver.find_element_by_name(self.txtPassword_name).clear()
        self.driver.find_element_by_name(self.txtPassword_name).send_keys(password)
        self.driver.find_element_by_name(self.btnLogin_name).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.lnkSignin_xpath).click()
        