from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class CarbohydrateCalculatorPage(BasePage):

    URL = "https://www.calculator.net/calorie-calculator.html"

    METRIC = (By.LINK_TEXT, "Metric Units")
    US = (By.LINK_TEXT, "US Units")

    AGE = (By.NAME, "cage")
    HEIGHT_CM = (By.NAME, "cheightmeter")
    WEIGHT = (By.NAME, "ckg")

    FEET = (By.NAME, "cheightfeet")
    INCHES = (By.NAME, "cheightinch")
    WEIGHT_LB = (By.NAME, "cpound")

    MALE = (By.CSS_SELECTOR, "label[for='csex1']")
    #MALE = (By.ID, "csex1")
    FEMALE = (By.CSS_SELECTOR, "label[for='csex2']")

    ACTIVITY = (By.ID, "cactivity")

    CALCULATE = (By.XPATH, "//input[@value='Calculate']")

    RESULT = (By.ID, "content")

    ERROR_MSG = (By.CSS_SELECTOR, "div[style*='error.svg']")


    def open(self):
        self.driver.get(self.URL)

    def select_metric(self):
        self.click(self.METRIC)

    def select_us(self):
        self.click(self.US)

    def select_male(self):
        self.click(self.MALE)

    def select_female(self):
        self.click(self.FEMALE)

    def select_gender(self, gender):
        if gender == "male":
            self.click(self.MALE)
        else:
            self.click(self.FEMALE)

    def set_metric_values(self, age, height, weight):

        self.enter_text(self.AGE, age)
        self.enter_text(self.HEIGHT_CM, height)
        self.enter_text(self.WEIGHT, weight)

    def set_us_values(self, age, feet, inches, weight):

        self.enter_text(self.AGE, age)
        self.enter_text(self.FEET, feet)
        self.enter_text(self.INCHES, inches)
        self.enter_text(self.WEIGHT_LB, weight)

    def select_activity(self, text):
        self.select_dropdown_by_text(self.ACTIVITY, text)

    def calculate(self):
        self.click(self.CALCULATE)

    def results_displayed(self):
        return "Maintain weight" in self.get_text(self.RESULT)

    def invalid_input_error(self, text):
        return text in self.get_text(self.ERROR_MSG)