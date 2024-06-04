*** Settings ***
Library     SeleniumLibrary
Library    XML



*** Variables ***
*** Test Cases ***
LoginTest
    Open Browser        https://demo.nopcommerce.com/      chrome
    Maximize Browser Window
    log           priti
    Click Link    //a[contains(@href,'login')]
    Sleep    5
    @{ele}=   Get WebElements    //input
#    Log     ${ele}
    FOR    ${element}    IN    @{ele}
        Log    ${element}

    END

#    Wait Until Element Is Visible    //input[@class='email valid']
#    nput Text    //input[@class='email valid']    pritibhushanf@gmail.com
#    Input Text    //input[@class='password valid']      Test@123
#    Click Button    //button[contains(@class,'login')]
    
    Sleep    10
*** Keywords ***