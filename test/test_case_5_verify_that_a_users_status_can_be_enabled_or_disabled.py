# Test Case 5: Verify that a user's status can be enabled or disabled
# Steps:
# 1. Navigate to the "HR Administration" section in the OrangeHRM application.
# 2. Click on the "Filter" icon/button.
# 3. Enter the username of non-existing user in the Username field.
# 4. Click on the "Search" button.
# Expected Result:
# The system should filter out and display empty list of users.
# The Message: 'No Records Found' should be displayed.
import time


def test_case_5_verify_that_a_users_status_can_be_enabled_or_disabled(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_button()
    app.orangeHrm.popUp.click_on_username_filter_field()
    app.orangeHrm.popUp.set_filter_username("local")
    app.orangeHrm.popUp.click_on_search_button()
    app.assert_that(app.orangeHrm.hrAdministration.get_filter_no_record_message()).contains("No Records Found")

