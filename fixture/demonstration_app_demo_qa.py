import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from fixture.step import StepHelper

class DemonstrationAppDemoQa:
    parent_element_of_sub_menu = '//div[@class="element-list collapse show"]/../span'
    opened_sub_menu = 'div[class="element-list collapse show"]'
    list_of_side_menu_items = 'div[class="left-pannel"] div[class="header-text"]'
    list_of_side_menu_sub_items = 'div[class="left-pannel"] div[class="element-list collapse show"] li'
    draggable = '#draggable'
    droppable = '#droppable'
    old_style_drop_down = '#oldSelectMenu'
    file_upload_input = '#uploadFile'

    def __init__(self, app):
        self.app = app
        self.step: StepHelper = self.app.step
        self.wd = self.app.wd

    def openUrl(self, url="https://demoqa.com/select-menu"):
        self.wd.get(url)

    def go_to_side_menu_section(self, section_name, sub_section_name):
        self.collapse_all_menu_elements()
        self.step.click_element_by_text(self.list_of_side_menu_items, section_name, True)
        self.step.click_element_by_text(self.list_of_side_menu_sub_items, sub_section_name, True)

    def drag_and_drop(self):
        # Wait for the draggable and droppable elements to be visible
        source_element = self.step.wait_for_element(self.draggable)
        target_element = self.step.wait_for_element(self.droppable)
        self.step.scroll_element_into_center(self.droppable)
        # Perform the drag and drop action
        ActionChains(self.wd).drag_and_drop(source_element, target_element).perform()

    def collapse_all_menu_elements(self):
        if self.step.specified_element_is_present(self.opened_sub_menu):
            self.step.scroll_element_into_center(self.parent_element_of_sub_menu)
            self.step.click_on_element(self.parent_element_of_sub_menu)
            time.sleep(1)

    def select_value_from_old_style_drop_down(self, text):
        self.step.scroll_element_into_center(self.old_style_drop_down)
        self.step.select_dropdown_by_text(self.old_style_drop_down, text)

    def upload_file(self, file_path):
        self.step.scroll_element_into_center(self.file_upload_input)
        file_input = self.wd.find_element(By.CSS_SELECTOR, self.file_upload_input)
        file_input.send_keys(file_path)