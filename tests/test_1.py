import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By #
from selenium.webdriver.support import expected_conditions as ec #слово as(как) разрешает сокращать или переименовывать фукцию
from selenium.webdriver.support.ui import WebDriverWait #ждать пока это условие не исполнится


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) #тк элемент может быстро не найтись через селектор, тут мы прописываем время поиска
        element1 = driver.find_element(By.CSS_SELECTOR, '#id_123')#тут прописываем через клас By.css_selektor 'то что хотим найти на странице' присутствует ли на странице

        wait = WebDriverWait(driver, 15, 0.3)#драйвер делает новый запрос каждые 15сек с частотой 0.3сек
        element = wait.until(ec.visibility_of_element_located(By.CSS_SELECTOR, '#id_123'))