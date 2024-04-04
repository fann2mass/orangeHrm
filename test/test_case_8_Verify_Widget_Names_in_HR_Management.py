# Test Case 8: Verify Retrieval of Widget Names in HR Management Component
# Test Name: Test_Get_Widget_Names_HR_Management
# Purpose: To verify that the HR Management component is created and the method to retrieve all widget names functions as expected.
# Precondition: The user has created a new component in the project named 'HRManagement'.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Log in to the application with valid credentials.
# 3. Navigate to the 'HR Management' component from the main menu.
# 4. Click on the 'Home' button
# 5. Execute the 'get_widget_names' method to retrieve the list of widget names.
# 6. Verify that the list of retrieved widget names matches the expected list.
# Expected Result:
# The 'get_widget_names' method should return an accurate list of widget names that are present within the HR Management component.

def test_case_8_test_get_widget_names_hr_management(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')