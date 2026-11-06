*** Settings ***
Documentation     Login tests for https://www.demoblaze.com/
Resource          ../resources/common.resource
Resource          ../resources/test_data.resource
Resource          ../resources/login_page.resource
Test Setup        Open Demoblaze
Test Teardown     Close Demoblaze

*** Test Cases ***
TC1 User Can Log In
    [Tags]    login    smoke
    Click Login Button
    Login And Password Fields Should Be Presented
    Set Up Login And Password    ${USERNAME}    ${PASSWORD}
    Click Login Submit Button
    Logout Button And Welcome Message Should Be Presented    ${USERNAME}
