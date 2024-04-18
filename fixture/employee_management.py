from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.table import Table


class EmployeeManagement:
    home_button = "a[data-automation-id='menu_home']"
    list_of_widgets_header_texts = ".widget-header span:last-child"
    gear_button = '.config-button'
    my_widget_button = '.nav-tabs li:nth-child(2)'
    my_widgets_names = '.oxd-switch-label'
    table_first_row = '#content tbody tr:nth-child(2)'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#content tbody tr',
                           column_selectors={'employee_id': 'td:nth-child(2)',
                                             'employee_name': 'td:nth-child(3)',
                                             'job_title': 'td:nth-child(4)',
                                             'employment_status': 'td:nth-child(5)'})

    def click_home(self):
        self.step.click_on_element(self.home_button)

    def click_gear_button(self):
        self.step.click_on_element(self.gear_button)

    def get_widgets_headers(self):
        return self.step.get_elements_texts(self.list_of_widgets_header_texts)

    def click_my_widget_button(self):
        self.step.click_on_element(self.my_widget_button)

    def get_widget_names(self):
        return self.step.get_elements_texts(self.my_widgets_names)

    def wait_for_table(self):
        self.step.wait_for_element(self.table_first_row, 40)
