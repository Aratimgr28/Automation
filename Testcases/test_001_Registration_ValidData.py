from Base.InitiateDriver import startBrowser, closeBrowser
from Library.ConfigReader import ElementsRead

def test_ValidateRegistration():
    driver=startBrowser()
    #driver.find_element('xpath',"//input[@name='firstname']").send_keys('Arati')
    #driver.find_element('xpath',"//input[@name='lastname']").send_keys('Rana Magar')

    driver.find_element('name',ElementsRead('Registration','fname')).send_keys('Arati')
    driver.find_element('name',ElementsRead('Registration','lname')).send_keys('Rana Magar')
    driver.find_element('name',ElementsRead('Registration','month')).send_keys('04')
    driver.find_element('name',ElementsRead('Registration','day')).send_keys('02')
    driver.find_element('name',ElementsRead('Registration','year')).send_keys('2003')
    driver.find_element('xpath',ElementsRead('Registration','gender_xpath')).click
    driver.find_element('xpath',ElementsRead('Registration','email')).send_keys('9847828584')
    driver.find_element('xpath',ElementsRead('Registration','pwd')).send_keys('A@1234')
    driver.find_element('xpath',ElementsRead('Registration','submit')).click


    # driver.find_element('name','birthday_month').send_keys("November")
    # driver.find_element('name','birthday_day').send_keys("28")
    # driver.find_element('name','birthday_year').send_keys("2002")
    # driver.find_element('xpath',"//input[@value='1']").click()
    # driver.find_element('xpath',"//input[@name='reg_email__']").send_keys(9847828584")
    # driver.find_element('xpath',"//input[@aria-label='New password']").send_keys("Arati@1234")
    # driver.find_element('xpath',"//button[@name='websubmit']").click()
    # driver.find_element('link text','Already have an account?').click()
    closeBrowser()

   