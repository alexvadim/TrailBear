import allure
from TrailBearPage import TrailBearHelper
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from allure_commons.types import AttachmentType
@allure.title('Тест mywork')
@allure.feature('Проверка click mywork')
@allure.story('Проверка ссылки Мои работы ')
def test_click_mywork(browser):
    with allure.step('Открыть сайт'):
        mywork = TrailBearHelper(browser)
        mywork.go_to_site()
    with allure.step('Кликнуть Мои работы'):
        mywork.click_mywork()
    element = mywork.browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div[3]/div[1]/p[1]').text
    allure.attach(mywork.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert element == 'Сумка мужская', 'Ошибка!'

@allure.title('Тест reviews')
@allure.feature('Проверка click reviews')
@allure.story('Проверка ссылки Отзывы ')
def test_click_reviews(browser):
    with allure.step('Открыть сайт'):
        reviews = TrailBearHelper(browser)
        reviews.go_to_site()
    with allure.step('Кликнуть Отзывы'):
        reviews.click_reviews()
    element = reviews.browser.find_element(By.XPATH, '//*[@id="feedback"]/div/div/h5').text
    allure.attach(reviews.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert element == 'Есть вопросы? Нужна консультация?', 'Ошибка!'

@allure.title('Тест feedback')
@allure.feature('Проверка click feedback')
@allure.story('Проверка ссылки Контакты ')
def test_click_feedback(browser):
    with allure.step('Открыть сайт'):
        feedback = TrailBearHelper(browser)
        feedback.go_to_site()
    with allure.step('Кликнуть Контакты'):
        feedback.click_feedback()
    element = feedback.browser.find_element(By.XPATH, '//*[@id="feedback"]/footer/button').text
    allure.attach(feedback.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert element == 'TrailBear', 'Ошибка!'