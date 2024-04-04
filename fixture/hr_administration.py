from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class HrAdministration:
    add_user_button = "//div[@id='systemUserDiv'] //*[text()='add']"
    filter_users_button = '//a[@data-tooltip="Filter"]'
    filtered_user_names = 'tbody td:nth-child(2) span'
    save_button = '#modal-save-button'
    filtered_user_roles = 'tbody td:nth-child(3) span'
    filter_no_records_message = '//div[text()="No Records Found"]'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    password_error_message = "//span[contains(text(),'Required')]"
    password_error_8_char = "//span[contains(text(),'Your password should have at least 8 characters.')]"
    password_very_weak = "//span[contains(text(),'Very Weak')]"
    password_weak = "//span[contains(text(),'Weak')]"
    passwords_better = "//span[contains(text(),'Better')]"
    password_strongest = "//span[contains(text(),'Strongest')]"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_add_user(self):
        self.step.click_on_element(self.add_user_button)
        self.step.specified_element_is_present(self.filtered_user_names, 10)

    def click_filter_button(self):
        self.step.specified_element_is_present(self.filtered_user_names, 30)
        self.step.click_on_element(self.filter_users_button)
        self.step.wait_for_element(self.filter_popup_table)

    def get_filtered_usernames(self):
        self.step.wait_for_element(self.filtered_user_names)
        return self.step.get_element_text(self.filtered_user_names)

    def get_filtered_user_roles(self):
        return self.step.get_element_text(self.filtered_user_roles)

    def get_filter_no_record_message(self):
        self.step.specified_element_is_present(self.filter_no_records_message)
        return self.step.get_elements_texts(self.filter_no_records_message)

    def make_sure_that_user_not_found(self):
        self.step.specified_element_is_not_present(self.filter_no_records_message,5)
        return self.step.specified_element_is_present(self.filtered_user_names)

    def get_password_error_message(self):
        return self.step.get_element_text(self.password_error_message)

    def get_password_error_8_char(self):
        return  self.step.get_element_text(self.password_error_8_char)

    def get_password_very_weak(self):
        return self.step.get_element_text(self.password_very_weak)

    def get_password_weak(self):
        return self.step.get_element_text(self.password_weak)

    def get_password_better(self):
        return  self.step.get_element_text(self.passwords_better)

    def get_password_strongest(self):
        return self.step.get_element_text(self.password_strongest)
