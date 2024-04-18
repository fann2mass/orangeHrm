def test_case_9_employee_management_table_verification(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    a = sorted(app.orangeHrm.employeeManagement.table.get_column_data('employee_id'))
    b = sorted(app.orangeHrm.employeeManagement.table.get_column_data('employee_name'))
    c = sorted(app.orangeHrm.employeeManagement.table.get_column_data('job_title'))
    d = sorted(app.orangeHrm.employeeManagement.table.get_column_data('employment_status'))
    app.assert_that(app.orangeHrm.employeeManagement.table[1]['employee_id']).is_equal_to('1061')
    app.assert_that(app.orangeHrm.employeeManagement.table[0]['employee_name']).is_equal_to('Mazie Abraham')
    app.assert_that(app.orangeHrm.employeeManagement.table[4]['employment_status']).is_equal_to('Full-Time Permanent')

    # 1 Create a new object of the table class inside the employee management component (based on the example from hr_administration).
    # 2 Find selectors: For list of rows and list of column elements (Employee Id, Name, Job Title, Employment Status).
    # 3 Get list of elements from each defined column and assert them with the expected one.
    # 4 Get second element from the 'Employee Id' column and assert it with the expected one.
    # 5 Get first element from the 'Name' column and assert it with the expected one.
    # 6 Get fifth element from the 'Employment Status' column and assert it with the expected one.


table_employee_id = ['0123', '1061', '1055', '0125', '1058', '1002', '1072', '1080', '1144', '1149', '1122', '1139',
                     '1071', '0119', '1117', '1032', '1158', '1104', '1102', '1171', '1083', '1110', '1039', '1093',
                     '1165', '0129', '1121', '201', '1123', '1038', '1127', '1015', '1142', '1135', '1068', '1081',
                     '1118', '1059', '0120', '0203', '1097', '1146', '1050', '1103', '1092', '1074', '1035', '1141',
                     '1163', '1006']
