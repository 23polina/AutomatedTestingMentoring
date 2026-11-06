*** Settings ***
Library     SeleniumLibrary
Resource    locators.resource

*** Keywords ***
Click Login Button
    Wait Until Element Is Visible    ${LOGIN_NAV_BUTTON}
    Click Element    ${LOGIN_NAV_BUTTON}

Login And Password Fields Should Be Presented
    Wait Until Element Is Visible    ${LOGIN_USERNAME_FIELD}
    Element Should Be Visible        ${LOGIN_USERNAME_FIELD}
    Element Should Be Visible        ${LOGIN_PASSWORD_FIELD}

Set Up Login And Password
    [Arguments]    ${username}    ${password}
    Input Text        ${LOGIN_USERNAME_FIELD}    ${username}
    Input Password    ${LOGIN_PASSWORD_FIELD}    ${password}

Click Login Submit Button
    Click Button    ${LOGIN_SUBMIT_BUTTON}

Logout Button And Welcome Message Should Be Presented
    [Arguments]    ${username}
    [Tags]    screenshot
    Wait Until Element Is Visible    ${LOGOUT_NAV_BUTTON}
    Element Should Be Visible        ${LOGOUT_NAV_BUTTON}
    Wait Until Element Is Visible    ${WELCOME_MESSAGE}
    Element Text Should Be           ${WELCOME_MESSAGE}    Welcome ${username}

Log In As Registered User
    [Arguments]    ${username}    ${password}
    Click Login Button
    Login And Password Fields Should Be Presented
    Set Up Login And Password    ${username}    ${password}
    Click Login Submit Button
    Logout Button And Welcome Message Should Be Presented    ${username}
    Wait Until Element Is Not Visible    ${LOGIN_MODAL}
