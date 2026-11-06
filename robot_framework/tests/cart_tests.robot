*** Settings ***
Documentation     Cart tests for https://www.demoblaze.com/
Resource          ../resources/common.resource
Resource          ../resources/test_data.resource
Resource          ../resources/login_page.resource
Resource          ../resources/shop_page.resource
Test Setup        Open Demoblaze
Test Teardown     Close Demoblaze

*** Test Cases ***
TC2 Most Expensive Monitor Can Be Added To Cart
    [Tags]    cart
    Log In As Registered User    ${USERNAME}    ${PASSWORD}
    Open Monitors Category
    ${name}    ${price_text}    ${price_value}=    Get Highest Priced Product On Page
    Open Product Page    ${name}
    Product Page Should Show Name And Price    ${name}    ${price_text}
    Click Add To Cart Button
    Click Cart Button
    Cart Should Contain Product    ${name}    ${price_value}
