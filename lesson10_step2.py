from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyperclip

import math
import time


def calc(x):
    """
    Function realized mathematical formula
    :param x: str
    :return: int
    """
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # make a link
    link = "http://suninjuly.github.io/explicit_wait2.html"
    #
    browser = webdriver.Chrome()
    # move to page
    browser.get(link)

    # Waiting when hose price will be 100
    actual_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))

    # check house price
    if actual_price:
        # if price == 100 find the button and click it
        button = browser.find_element_by_id('book').click()

    # we must scroll down our page and we do it
    button = browser.find_element_by_id('solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # we must read the number for our mathematical expression and send them
    nowrap = browser.find_element_by_id('input_value').text
    expression_result = calc(nowrap)

    # we must find the line for our answer and put our answer there
    output_answer = browser.find_element_by_name("text")
    output_answer.send_keys(expression_result)

    button.click()

    # we want copy the alert answer to buffer
    alert = browser.switch_to.alert
    alert_text = alert.text
    add_to_clip_board = alert_text.split(': ')[-1]
    pyperclip.copy(add_to_clip_board)

finally:
    time.sleep(5)
    browser.quit()
