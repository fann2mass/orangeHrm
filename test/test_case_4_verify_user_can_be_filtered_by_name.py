# Test Case 4: Verify that a user can be filtered by username
# Steps:
# 1. Navigate to the "HR Administration" section in the OrangeHRM application.
# 2. Click on the "Filter" icon/button.
# 3. Enter the username of an existing user in the Username field.
# 4. Click on the "Search" button.
# Expected Result:
# The system should filter out and display only the user(s) matching the entered username.
def test_case_4_verify_user_can_be_filtered_by_name(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_button()
    app.assert_that(app.orangeHrm.popUp.get_filter_table_name()).is_equal_to('Filter Users')
    app.orangeHrm.popUp.click_on_username_filter_field()
    app.orangeHrm.popUp.set_username_filter("Admin")
    app.orangeHrm.popUp.click_on_search_button()
    app.assert_that(app.orangeHrm.hrAdministration.get_filtered_usernames()).is_equal_to("Admin")
    app.assert_that(app.orangeHrm.hrAdministration.get_filtered_user_roles()).is_equal_to('Global Admin')
