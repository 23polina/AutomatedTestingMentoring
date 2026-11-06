*** Settings ***
Library     SeleniumLibrary
Resource    locators.resource

*** Keywords ***
Open Monitors Category
    Click Element    ${MONITORS_CATEGORY}
    Wait Until Page Contains Element    xpath=//div[@id='tbodyid']//a[text()='Apple monitor 24']

Get Highest Priced Product On Page
    [Documentation]    Returns the product name, price text (e.g. $400) and numeric price.
    Wait Until Element Is Visible    ${FIRST_PRODUCT_TITLE}
    ${titles}=    Get WebElements    ${PRODUCT_TITLES}
    ${prices}=    Get WebElements    ${PRODUCT_PRICES}
    ${max_value}=    Set Variable    ${-1}
    ${max_name}=     Set Variable    ${EMPTY}
    ${max_text}=     Set Variable    ${EMPTY}
    FOR    ${title}    ${price}    IN ZIP    ${titles}    ${prices}
        ${name_text}=     Get Text    ${title}
        ${price_text}=    Get Text    ${price}
        ${value}=         Evaluate    int($price_text.replace('$', '').strip())
        IF    ${value} > ${max_value}
            ${max_value}=    Set Variable    ${value}
            ${max_name}=     Set Variable    ${name_text}
            ${max_text}=     Set Variable    ${price_text}
        END
    END
    RETURN    ${max_name}    ${max_text}    ${max_value}

Open Product Page
    [Arguments]    ${name}
    Click Element    xpath=//div[@id='tbodyid']//a[text()='${name}']

Product Page Should Show Name And Price
    [Arguments]    ${name}    ${price_text}
    Wait Until Element Is Visible    ${PRODUCT_PAGE_NAME}
    Element Text Should Be    ${PRODUCT_PAGE_NAME}    ${name}
    Element Should Contain    ${PRODUCT_PAGE_PRICE}    ${price_text}

Click Add To Cart Button
    Wait Until Element Is Visible    ${ADD_TO_CART_BUTTON}
    Click Element    ${ADD_TO_CART_BUTTON}
    ${message}=    Handle Alert    action=ACCEPT    timeout=10s
    Should Contain    ${message}    Product added

Click Cart Button
    Click Element    ${CART_NAV_BUTTON}

Cart Should Contain Product
    [Documentation]    The cart page shows the price without the $ sign (e.g. 400).
    [Arguments]    ${name}    ${price_value}
    [Tags]    screenshot
    ${row}=    Set Variable
    ...    xpath=//tbody[@id='tbodyid']/tr[td[2]='${name}' and td[3]='${price_value}']
    Wait Until Element Is Visible    ${row}
    Element Should Be Visible        ${row}
