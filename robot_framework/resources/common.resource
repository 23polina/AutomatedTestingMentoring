*** Settings ***
Library     SeleniumLibrary
Library     ../listeners/ScreenshotListener.py    screenshot

*** Variables ***
${URL}          https://www.demoblaze.com/
${BROWSER}      chrome
${TIMEOUT}      10s

*** Keywords ***
Open Demoblaze
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}

Close Demoblaze
    Close All Browsers
