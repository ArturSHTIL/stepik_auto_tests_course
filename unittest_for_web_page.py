from selenium import webdriver
import unittest
import time

# a global variable is not the best solution, but....
_actual_result = 'Congratulations! You have successfully registered!'


def initiate_input_lines(link) -> str:
    """
    Function for adding information to strings
    :param link:
    :return:
    """
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector('.first_block .first')
    first_name.send_keys('Python')

    second_name = browser.find_element_by_css_selector('.first_block .second')
    second_name.send_keys('is a Great')

    email_line = browser.find_element_by_css_selector('.third_class .third')
    email_line.send_keys('Python_is_a_great@language.com')

    phone_line = browser.find_element_by_css_selector('.second_block .first')
    phone_line.send_keys('+22022022')

    address_line = browser.find_element_by_css_selector('.second_block .second')
    address_line.send_keys('Welcome to the Future my Dear')

    # this string push the button on the page
    push_button = browser.find_element_by_css_selector('.btn')
    push_button.click()

    time.sleep(1)

    # we see a new page and take the text from it
    success_message = browser.find_element_by_tag_name("h1").text
    return success_message

    time.sleep(6)
    browser.quit()


class TestForWebPages(unittest.TestCase):
    """
    This class specifically for the test results of our links! don't forget that the class and methods will
    begin with the word "test"
    """
    def test_first_web_page(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        link_answer = initiate_input_lines(link1)
        self.assertEqual(link_answer, _actual_result,"Something happen check it")

    def test_second_web_page(self):
        link2 = 'http://suninjuly.github.io/registration2.html'
        link_answer = initiate_input_lines(link2)
        self.assertEqual(link_answer, _actual_result, "Something happen check it")


if __name__ == '__main__':
    unittest.main()
