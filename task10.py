import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Search(unittest.TestCase):

    def setUp(self):
        # s = Service('chromedriver.exe')
        # self.drv = webdriver.Chrome(service=s)
        self.drv = webdriver.Chrome('chromedriver.exe')
        self.drv.get('http://google.com')

    def test_search(self):
        assert 'Google' in self.drv.title
        elm = self.drv.find_element(By.NAME, "q")
        # 2. Выполнить поиск слова “selenide”
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        # 3. Проверить, что первый результат – ссылка на сайт selenide.org.
        elm1 = self.drv.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a')
        assert 'selenide.org' in elm1.text
        print("Первый результат – ссылка на сайт selenide.org.")
        t1 = elm1.text
        # 4. Перейти в раздел поиска изображений
        elm = self.drv.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        elm.click()
        # 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
        elm = self.drv.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]')
        elm.click()
        try:
            WebDriverWait(self.drv, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[text() = "ru.selenide.org"]')))
        except TimeoutException:
            raise Exception('Unable to find text in this element after waiting 5 seconds')
        # 6. Вернуться в раздел поиска Все
        elm = self.drv.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
        self.drv.execute_script("arguments[0].click()", elm)
        # 7. Проверить, что первый результат такой же, как и на шаге 3.
        elm2 = self.drv.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a')
        assert "ru.selenide.org" in elm2.text
        assert t1 in elm2.text
        print("Первый результат такой же, как и на шаге 3.")

        assert 'No results found' not in self.drv.page_source

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()