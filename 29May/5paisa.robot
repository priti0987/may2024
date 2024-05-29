*** Setting ***
Library             SeleniumLibrary
Library             Dialogs
Suite Setup         Log  Test Project
Suite Teardown      tearDown

*** Variables ***
${data}=     123456

*** Test Cases ***
Test_Home
    Open Browser     https://login.5paisa.com/      chrome
    maximize browser window
    loginin5paisa
    Sleep    10
#    Service_Link
#    AboutUs_Link
#    Contact_Us_FailScenario

*** Keywords ***
Service_Link
    click element                   //a[normalize-space()='Careers']
    #verification
    element text should be          //span[contains(text(),'Remote Work')]      Remote Work

AboutUs_Link
    click element                   //a[normalize-space()='About Us']
    #verification
#    element text should be          //*[@id=\"aboutus\"]//div/h2                ABOUT US

Contact_Us_FailScenario
    click element                   //a[text()='Contact Us']
    #verification

tearDown
    Close All Browsers

loginin5paisa
    Log    login
    Input Text       //input[@id='loginUser']    {data}
    Sleep    10
    Click Button    //button[@id='btnGenerateOTP']
    Sleep    10
