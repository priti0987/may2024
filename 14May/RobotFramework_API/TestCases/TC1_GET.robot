*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${baseUrl}      https://reqres.in/api/


*** Test Cases ***
list_Users
    Create Session    mySession    ${baseUrl}
    ${response}=    Get Request    mySession   users?page=2
    Log    ${response.status_code}
#    Log    ${response.content}
#    Log To Console    ${response.headers}
    #validation
    ${status_code}=     Convert To String    ${response.status_code}
    Should Be Equal    ${status_code}    200
    ${body}=            Convert To String   ${response.content}
    Should Contain    ${body}    michael.lawson@reqres.in
    ${contentTypeValue}=    Get From Dictionary    ${response.headers}      Content-Type
    Should Be Equal    ${contentTypeValue}    application/json; charset=utf-8