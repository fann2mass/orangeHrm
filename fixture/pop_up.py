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
    cancel_button = '//a[@ng-click="modal.cancel()"]'
    user_exists_error_massage = "//span[text()='Already exists']"
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    search_button = "//a[text()='Search']"
    employee_name_auto_drop = '#employee_name_filter_dropdown span.angucomplete-title'
    no_results_found = "//div[contains(text(),'No results found')]"
    strength_indicator = '.password-strength-check'
    password_required_message = 'div.col-12 .invalid-feedback'
    ess_role_field = '#essroles_inputfileddiv input'
    ess_role_dropdown = '#essroles_inputfileddiv li'
    admin_role_field = '#adminroles_inputfileddiv input'
    admin_role_dropdown = '#adminroles_inputfileddiv li'
    supervisor_role_field = '#supervisorroles_inputfileddiv input'
    supervisor_role_dropdown = "#supervisorroles_inputfileddiv li"
    status_field = '#status_inputfileddiv input'
    status_dropdown = '#status_inputfileddiv li'
    location_field = '#location_inputfileddiv input'
    location_dropdown = '#location_inputfileddiv li'
    searching_text = '//div[contains(text(),"Searching...")]'
    list_of_found_employee_name = '#employee_name_filter_dropdown div[ng-repeat="result in results"] span[class="angucomplete-title"]'
    filter_reset_button = '//a[text()="Reset"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_add_employee_name(self, text):
        self.step.input_text(self.add_employee_name_field, text)

    def set_add_username(self, text):
        self.step.input_text(self.add_username_field, text)

    def set_filter_employee_name(self, text):
        self.step.input_text(self.filter_employee_name_field, text)
        self.step.specified_element_is_not_present(self.searching_text, 6)
        if  self.step.specified_element_is_present(self.no_results_found,3) == False:
            self.step.click_element_containing_text(self.list_of_found_employee_name,text)

    def set_filter_username(self, text):
        self.step.click_on_element(self.filter_username_field)
        self.step.input_text(self.filter_username_field, text)

    def set_password(self, text):
        self.step.click_on_element(self.password_field)
        self.step.input_text(self.password_field, text)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        self.step.click_on_element(self.save_button)

    def get_user_exist_error(self):
        return self.step.get_element_text(self.user_exists_error_massage)

    def click_on_username_filter_field(self):
        self.step.specified_element_is_present(self.filter_username_field, 10)
        self.step.click_on_element(self.filter_username_field)

    def click_on_search_button(self):
        self.step.click_on_element(self.search_button)
        time.sleep(1)

    def get_filter_table_name(self):
        self.step.specified_element_is_present(self.filter_popup_table, 20)
        return self.step.get_element_text(self.filter_popup_table)

    def get_employee_name_auto_drop(self):
        return self.step.get_elements_texts(self.employee_name_auto_drop)

    def get_no_result_found_text(self):
        self.step.specified_element_is_present(self.no_results_found, 10)
        return self.step.get_element_text(self.no_results_found)

    def get_strength_indicator_text(self):
        self.step.specified_element_is_present(self.strength_indicator, 5)
        return self.step.get_element_text(self.strength_indicator)

    def get_password_required_message(self):
        return self.step.get_element_text(self.password_required_message)

    def click_ess_role_field(self):
        self.step.click_on_element(self.ess_role_field)
        time.sleep(1)

    def set_ess_role_dropdown(self, text):
        self.step.click_on_element(self.ess_role_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.ess_role_dropdown, text)

    def get_ess_role_dropdown(self):
        return self.step.get_element_attribute_value(self.ess_role_field, 'value', True)

    def click_admin_role_field(self):
        self.step.click_on_element(self.admin_role_field)
        time.sleep(1)

    def set_admin_role_dropdown(self, text):
        self.step.click_on_element(self.admin_role_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.admin_role_dropdown, text)

    def get_admin_role_dropdown(self):
        return self.step.get_element_attribute_value(self.admin_role_field,'value', True)

    def click_supervisor_role_field(self):
        self.step.click_on_element(self.supervisor_role_field)
        time.sleep(1)

    def set_supervisor_role_dropdown(self, text):
        self.step.click_on_element(self.supervisor_role_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.supervisor_role_dropdown, text)

    def get_supervisor_role_dropdown(self):
        return self.step.get_element_attribute_value(self.supervisor_role_field,'value', True)

    def set_status_dropdown(self, text):
        self.step.click_on_element(self.status_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.status_dropdown, text)

    def click_status_field(self):
        self.step.click_on_element(self.status_field)
        time.sleep(1)

    def get_status_dropdown(self):
        return self.step.get_element_attribute_value(self.status_field, 'value', True)

    def set_location_dropdown(self, text):
        self.step.click_on_element(self.location_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.location_dropdown, text)

    def click_location_field(self):
        self.step.click_on_element(self.location_field)
        time.sleep(1)

    def get_location_dropdown(self):
        return self.step.get_element_attribute_value(self.location_field, 'value', True)

    def click_reset_filter(self):
        self.step.click_on_element(self.filter_reset_button)

    def wait_filter_users_table_desapeared(self):
        self.step.specified_element_is_not_present(self.filter_popup_table)

    def click_filter_cancel_btn(self):
        self.step.click_on_element(self.cancel_button)


