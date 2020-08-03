from selenium import webdriver
import os
import time


def t():
    time.sleep(1)  # Сон в N секунд для удобства просмотра действий


def before_all(context):
    context.driver = webdriver.Chrome()
    link = "http://qa-assignment.oblakogroup.ru/board/:alexander_zilin_test2"
    context.driver.get(link), t()  # Переходим на тестируемый сайт

    # chrome_option = webdriver.ChromeOptions()
    # if os.environ.get('docker') == 'true':
    #   print("Init docker env")
    #   chrome_option.add_argument("headless")
    #   chrome_option.add_argument("--no-sandbox")
    #   chrome_option.add_argument("--disable-dev-shm-usage")
    #   context.driver = webdriver.Chrome(chrome_options=chrome_option)
    # else:
    #   context.driver = webdriver.Chrome(executable_path='./drivers/chromedriver', chrome_options=chrome_option)
    #
    # context.driver.implicitly_wait(5)


def after_all(context):
    context.driver.quit()
