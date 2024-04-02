from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class PopUp:
    user_name_field = '#user_name'
    employee_name_field = '#selectedEmployee_value'
    password_field = '#password'
    confirm_password_field = '#confirmpassword'
    save_button = '#modal-save-button'
    user_exists_error_massage = "//span[text()='Already exists']"
    username_filter_field = '//input[@id="systemuser_uname_filter"]'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    search_button = "//a[text()='Search']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_username(self, text):
        self.step.input_text(self.user_name_field, text)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_name_field, text)

    def set_password(self, text):
        self.step.input_text(self.password_field, text)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        self.step.click_on_element(self.save_button)

    def get_user_exist_error(self):
        return self.step.get_element_text(self.user_exists_error_massage)

    def click_on_username_filter_field(self):
        self.step.specified_element_is_present(self.username_filter_field,10)
        self.step.jsXpathClick(self.username_filter_field)

    def click_on_search_button(self):
        self.step.jsXpathClick(self.search_button)

    def get_filter_table_name(self):
        self.step.specified_element_is_present(self.filter_popup_table,20)
        return self.step.get_element_text(self.filter_popup_table)

    def set_username_filter(self, text):
        self.step.input_text(self.username_filter_field, text)

    def get_filtered_usernames(self):
        return self.step.get_elements_texts(self.filtered_usernames)
