from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TrailBearLocators:
    LOCATOR_TrailBear_FIELD_MYWORK = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/a[1]')
    LOCATOR_TrailBear_FIELD_REVIEWS = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/a[2]')
    LOCATOR_TrailBear_FIELD_FEEDBACK = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/a[3]')
    LOCATOR_TrailBear_FIELD_VK = (By.XPATH, '//*[@id="feedback"]/footer/p[1]/a/img')


class TrailBearHelper(BasePage):

    def click_mywork(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FIELD_MYWORK).click()


    def click_reviews(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FIELD_REVIEWS).click()


    def click_feedback(self):
        self.driverwait(TrailBearLocators.LOCATOR_TrailBear_FIELD_FEEDBACK).click()


    def click_vk(self):
        self.driverwait(TrailBearFormLocators.LOCATOR_TrailBear_FIELD_VK).click()
