# Test Case 6: Verify Password Field Required Validation
# Test Name: Test_Password_Field_Required
# Purpose: To verify that the password field shows a 'required' error message when left empty.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Add User' button.
# 5. Leave the 'Password' and 'Confirm Password' fields empty.
# 6. Click outside the password fields to trigger validation.
# Expected Result:
# An error message stating 'Required' should appear under both 'Password' and 'Confirm Password' fields.
# ---------------------------------------------------------------------------------------------

def test_password_field_required(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()


# ---------------------------------------------------------------------------------------------
# Test Case 7: Verify Password Minimum Length Validation
# Test Name: Test_Password_Min_Length
# Purpose:To verify that the password field shows a minimum length error message when fewer
# than 8 characters are entered.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter a single character in the 'Password' field.
# 3. Click outside the password field to trigger validation.
# Expected Result:
# An error message stating 'Your password must have at least 8 characters.' should appear under the 'Password' field.
# ---------------------------------------------------------------------------------------------

def test_password_min_length(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()


# ---------------------------------------------------------------------------------------------
# Test Case 8: Verify Password Strength Indicator - Very Weak
# Test Name: Test_Password_Strength_Very_Weak
# Purpose: To verify that the password strength indicator shows 'Very Weak' when 8 identical characters are entered.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter '00000000' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Very Weak' message.
# ---------------------------------------------------------------------------------------------

def test_password_strength_very_weak(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()


# ---------------------------------------------------------------------------------------------
# Test Case 9: Verify Password Strength Indicator - Weak
# Test Name: Test_Password_Strength_Weak
# Purpose: To verify that the password strength indicator shows 'Weak' when the password includes two uppercase letters.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter 'AA000000' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Weak' message.
# ---------------------------------------------------------------------------------------------

def test_password_strength_weak(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()


# ---------------------------------------------------------------------------------------------
# Test Case 10: Verify Password Strength Indicator - Better
# Test Name: Test_Password_Strength_Better
# Purpose: To verify that the password strength indicator shows 'Better' when the password
# includes three uppercase letters.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter 'AAA00000' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Better' message.
# ---------------------------------------------------------------------------------------------

def test_password_strength_better(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()


# ---------------------------------------------------------------------------------------------
# Test Case 11: Verify Password Strength Indicator - Strongest
# Test Name: Test_Password_Strength_Strongest
# Purpose: To verify that the password strength indicator shows 'Strongest' when the password includes
# a mix of uppercase letters, lowercase letters, numbers, and special symbols.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter 'Aa1!Aa1!' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Strongest' message.
# ---------------------------------------------------------------------------------------------

def test_password_strength_strongest(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
