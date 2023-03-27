import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_are_present(go_to_my_pets):
   '''Проверка того, что на странице "Мои питомцы" присутствуют все питомцы'''

   # Сохранение элементов статистики в переменную "statistic" 
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

   # Сохранение элементов карточек питомцев в переменную "pets"
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Получение количества питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Получение количества карточек питомцев
   number_of_pets = len(pets)

   # Проверка того, что количество питомцев из статистики совпадает с количеством карточек питомцев
   assert number == number_of_pets
