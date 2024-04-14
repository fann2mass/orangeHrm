import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class PopUp:
    add_username_field = "#user_name"
    add_employee_name_field = "#selectedEmployee_value"
    filter_username_field = '#systemuser_uname_filter'
    filter_employee_name_field = "#employee_name_filter_value"
    password_field = "//input[@id='password']"
    confirm_password_field = "//input[@id='confirmpassword']"
    save_button = "//button[contains(text(),'Save')]"
    user_exists_error_massage = "//span[text()='Already exists']"
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    search_button = "//a[text()='Search']"
    employee_name_auto_drop = '#employee_name_filter_dropdown span.angucomplete-title'
    no_results_found = "//div[contains(text(),'No results found')]"
    strength_indicator = '.password-strength-check'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_add_employee_name_field(self, text):
        self.step.input_text(self.add_employee_name_field, text)

    def set_add_username_field(self, text):
        self.step.input_text(self.add_username_field, text)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_name_field, text)
        self.step.specified_element_is_not_present(self.searching_text, 6)
        if self.step.specified_element_is_present(self.message_no_results, 3) == False:
            self.step.click_element_containing_text(self.list_of_found_employee_names, text)

    def set_password(self, text):
        self.step.click_on_element(self.password_field)
        self.step.input_text(self.password_field, text)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        self.step.click_on_element(self.save_button)

    def get_user_exist_error(self):
        return self.step.get_element_text(self.user_exists_error_massage)

    def click_on_search(self):
        self.step.click_on_element(self.filter_search_button)

    def get_strength_indicator_text(self):
        self.step.specified_element_is_present(self.strength_indicator, 5)
        return self.step.get_element_text(self.strength_indicator)

    def get_password_error(self):
        return self.step.get_element_text(self.password_error_massage)

    def get_confirm_password_error(self):
        return self.step.get_element_text(self.confirm_password_error_massage)