from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

class Uzytkownik:
    def __init__(self):
        login=[]
        haslo=[]
        hashtags=[]

        self.driver=webdriver.Chrome('./chromedriver')

    def log_in(self):
        print("Podaj login :")
        self.login=input()
        print("Podaj hasło :")
        self.haslo=input()
        print("Wpisz hasztag :")
        self.hasztags=input()

    def autorisation(self):
        self.driver.get("http://www.instagram.com")
        time.sleep(3)
        cookie_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/button[2]')
        cookie_button.click()
        time.sleep(4)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        username.clear()
        username.send_keys(self.login)
        password.clear()
        password.send_keys(self.haslo)
        login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()
        time.sleep(6)
        save_info_button = self.driver.find_element(by=By.XPATH,
                                               value='//*[@id="react-root"]/section/main/div/div/div/div/button')
        save_info_button.click()
        time.sleep(4)
        powiadomienia_info_button = self.driver.find_element(by=By.XPATH,
                                                             value='/html/body/div[5]/div/div/div/div[3]/button[2]')
        powiadomienia_info_button.click()

    def searching(self):
        search = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Szukaj']")))
        search.clear()
        tags = self.hasztags
        search.send_keys(tags)
        time.sleep(5)
        my_link = self.driver.find_element(by=By.XPATH,
                                      value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
        my_link.click()
        time.sleep(5)

    def action(self):
        photo = self.driver.find_element(by=By.XPATH,
                                    value='//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        photo.click()

        time.sleep(4)

        self.like = self.driver.find_element(by=By.XPATH,
                                   value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
        self.like.click()

        time.sleep(3)

        nextpic = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[2]/div/div/button")
        nextpic.click()

        time.sleep(3)

    def next_pic(self):
        nextpic = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[2]/div/div[2]/button")
        nextpic.click()
        time.sleep(3)

    def liked(self):
        self.like = self.driver.find_element(by=By.XPATH,
                                        value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
        self.like.click()
        time.sleep(3)