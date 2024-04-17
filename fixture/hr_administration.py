import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.table import Table


class HrAdministration:
    add_user_button = "//div[@id='systemUserDiv'] //*[text()='add']"
    filter_users_button = '//a[@data-tooltip="Filter"]'
    filtered_user_names = 'tbody td:nth-child(2) span'
    save_button = '#modal-save-button'
    filtered_user_roles = 'tbody td:nth-child(3) span'
    filter_no_records_message = '//div[text()="No Records Found"]'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    password_error_message = "#password+span"
    password_error_8_char = "//span[contains(text(),'Your password should have at least 8 characters.')]"
    password_very_weak = "//span[contains(text(),'Very Weak')]"
    password_weak = "//span[contains(text(),'Weak')]"
    passwords_better = "//span[contains(text(),'Better')]"
    password_strongest = "//span[contains(text(),'Strongest')]"
    first_table_row = '#systemUserDiv tbody tr:nth-child(2)'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#systemUserDiv tbody tr',
                           column_selectors={'check_box': 'td:nth-child(1)',
                                             'user_name': 'td:nth-child(2)',
                                             'user_role': 'td:nth-child(3)'})

    def wait_for_table(self):
        self.step.wait_for_element(self.first_table_row, 40)

    def click_add_user(self):
        self.step.wait_for_element(self.first_table_row,40)
        self.step.click_on_element(self.add_user_button)

    def click_filter_button(self):
        self.step.specified_element_is_present(self.filtered_user_names, 30)
        self.step.click_on_element(self.filter_users_button)
        self.step.wait_for_element(self.filter_popup_table)

    def get_filtered_usernames(self):
        self.step.wait_for_element(self.filtered_user_names)
        return self.step.get_element_text(self.filtered_user_names)

    def get_filtered_user_roles(self):
        return self.step.get_element_text(self.filtered_user_roles)

    def is_list_of_users_displayed(self):
        self.step.specified_element_is_not_present(self.filter_no_records_message, 5)
        return self.step.specified_element_is_present(self.filtered_usernames)
    def get_filter_no_record_message(self):
        self.step.specified_element_is_present(self.filter_no_records_message)
        return self.step.get_elements_texts(self.filter_no_records_message)

    def make_sure_that_user_not_found(self):
        self.step.specified_element_is_not_present(self.filter_no_records_message,5)
        return self.step.specified_element_is_present(self.filtered_user_names)

    def get_password_error_message(self):
        return self.step.get_element_text(self.password_error_message)

