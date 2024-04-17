# Test Case 7: Verify Employee Name Autocomplete Suggestion
# Test Name: Test_Employee_Name_Autocomplete
# Purpose: To verify that the autocomplete suggests names based on the entered value in the 'Employee Name' field.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Start typing a known employee name in the 'Employee Name' field.
# Expected Result:
# As the user types, an autocomplete dropdown should appear with employee name suggestions.

def test_case_7_test_employee_name_autocomplete(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_button()
    app.orangeHrm.popUp.set_filter_employee_name("Jason")
    app.assert_that(app.orangeHrm.popUp.get_employee_name_auto_drop()).contains('Jason Marshal', 'Jason Morgan')


# -----------------------------------------------------------------------------------

# Test Case 7_1: Verify No Results Found Error Message
# Test Name: Test_Employee_Name_No_Results
# Purpose: To verify that an appropriate error message is shown when no employee names match the entered value.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Enter a non-existing employee name in the 'Employee Name' field.
# Expected Result:
# A message indicating 'no results found' should appear if no employee names match the entered value.
def test_case_7_1_test_employee_name_no_results(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_button()
    app.orangeHrm.popUp.set_filter_employee_name("Sasha")
    app.assert_that(app.orangeHrm.popUp.get_no_result_found_text()).is_equal_to('No results found')


# -----------------------------------------------------------------------------------

# Test Case 7_2: Verify Dropdown Default Values
# Test Name: Test_Dropdown_Default_Values
# Purpose: To verify that the dropdowns in the 'Filter Users' pop-up are set to their default values upon opening.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Get default values from all drop-downs (you should create a separate method for each drop-down)
# 6. Assert values from all drop-downs in test (you should assert values separately for each drop-down) using assert_that(['a','b']).is_equal_to(['a','b'])
# Expected Result:
# All dropdowns in the 'Filter Users' pop-up should display their default values.

def test_case_7_2_test_dropdown_default_values(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_button()
    app.orangeHrm.popUp.click_ess_role_field()
    app.assert_that(app.orangeHrm.popUp.get_ess_role_dropdown()).is_equal_to(['All', 'Default ESS'])
    app.orangeHrm.popUp.click_admin_role_field()
    app.assert_that(app.orangeHrm.popUp.get_admin_role_dropdown()).is_equal_to(['All', 'Global Admin', 'Leave Admin',
                                                                                'Regional HR Admin', 'Report Admin'])
    app.orangeHrm.popUp.click_supervisor_role_field()
    app.assert_that(app.orangeHrm.popUp.get_supervisor_role_dropdown()).is_equal_to(['All', 'Default Supervisor'])
    app.orangeHrm.popUp.click_status_field()
    app.assert_that(app.orangeHrm.popUp.get_status_dropdown()).is_equal_to(['All', 'Enabled', 'Disabled'])
    app.orangeHrm.popUp.click_location_field()
    app.assert_that(app.orangeHrm.popUp.get_location_dropdown()).is_equal_to(['-- Select --', 'All', 'Australia',
                                                                              'Australia office', 'Canada',
                                                                              'Canadian Development Center',
                                                                              'France', 'France Office', 'Germany',
                                                                              'German Office', 'India',
                                                                              'India Office', 'Jamaica',
                                                                              'Jamaica training center',
                                                                              'Mexico', 'Mexico Office',
                                                                              'Philippines',
                                                                              'Philippine call center',
                                                                              'Singapore',
                                                                              'Singapore Regional HQ',
                                                                              'South Africa',
                                                                              'South Africa Satellite Office',
                                                                              'United Kingdom', 'UK Office',
                                                                              'United States', 'US Office'])


# -----------------------------------------------------------------------------------

# Test Case 7_3: Verify Reset Button Functionality
# Test Name: Test_Reset_Button
# Purpose: To verify that the 'Reset' button clears all input fields and selections and closes the 'Filter Users' pop-up.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Change values in the input fields and dropdown selections.
# 6. Click on the 'Reset' button.
# 7. Reopen the 'Filter Users' pop-up by clicking on the 'Filter' button.
# Expected Result:
# The 'Filter Users' pop-up should close upon clicking the 'Reset' button and upon reopening, all input fields and dropdowns should be reset to their default selections.

def test_case_7_3_test_reset_button(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_button()
    app.orangeHrm.popUp.set_filter_username("Admin")
    app.orangeHrm.popUp.set_filter_employee_name("aa")
    app.orangeHrm.popUp.set_ess_role_dropdown("Default ESS")
    app.orangeHrm.popUp.set_admin_role_dropdown("Leave Admin")
    app.orangeHrm.popUp.set_supervisor_role_dropdown("Default Supervisor")
    app.orangeHrm.popUp.set_status_dropdown("Disabled")
    app.orangeHrm.popUp.set_location_dropdown("Australia")
    app.orangeHrm.popUp.click_reset_filter()
    app.orangeHrm.popUp.wait_filter_users_table_desapeared()
    app.orangeHrm.hrAdministration.click_filter_button()
    app.assert_that(app.orangeHrm.popUp.get_ess_role_dropdown()).is_equal_to("All")
    app.assert_that(app.orangeHrm.popUp.get_admin_role_dropdown()).is_equal_to("All")
    app.assert_that(app.orangeHrm.popUp.get_supervisor_role_dropdown()).is_equal_to("All")
    app.assert_that(app.orangeHrm.popUp.get_status_dropdown()).is_empty()
    app.assert_that(app.orangeHrm.popUp.get_location_dropdown()).is_equal_to("All")


# -----------------------------------------------------------------------------------
# Test Case 7_4: Verify Cancel Button Functionality
# Test Name: Test_Cancel_Button
# Purpose: To verify that the 'Cancel' button closes the 'Filter Users' pop-up without clearing selected values.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Change values in the input fields and dropdown selections.
# 6. Click on the 'Cancel' button.
# 7. Reopen the 'Filter Users' pop-up by clicking on the 'Filter' button.
# Expected Result:
# The 'Filter Users' pop-up should close upon clicking the 'Cancel' button and upon reopening, the previously selected values should be retained.

def test_case_7_4_test_cancel_button(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_button()
    app.orangeHrm.popUp.click_reset_filter()
    app.orangeHrm.popUp.wait_filter_users_table_desapeared()
    app.orangeHrm.hrAdministration.click_filter_button()
    app.orangeHrm.popUp.set_filter_username("Admin")
    app.orangeHrm.popUp.set_filter_employee_name("aa")
    app.orangeHrm.popUp.set_ess_role_dropdown("Default ESS")
    app.orangeHrm.popUp.set_admin_role_dropdown("Leave Admin")
    app.orangeHrm.popUp.set_supervisor_role_dropdown("Default Supervisor")
    app.orangeHrm.popUp.set_status_dropdown("Disabled")
    app.orangeHrm.popUp.set_location_dropdown("Australia")
    app.orangeHrm.popUp.click_filter_cancel_btn()
    app.orangeHrm.popUp.wait_filter_users_table_desapeared()
    app.orangeHrm.hrAdministration.click_filter_button()
    app.assert_that(app.orangeHrm.popUp.get_ess_role_dropdown()).is_equal_to("Default ESS")
    app.assert_that(app.orangeHrm.popUp.get_admin_role_dropdown()).is_equal_to("Leave Admin")
    app.assert_that(app.orangeHrm.popUp.get_supervisor_role_dropdown()).is_equal_to("Default Supervisor")
    app.assert_that(app.orangeHrm.popUp.get_status_dropdown()).is_equal_to("Disabled")
    app.assert_that(app.orangeHrm.popUp.get_location_dropdown()).contains("Australia office")