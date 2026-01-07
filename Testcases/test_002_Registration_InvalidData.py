from Base.InitiateDriver import startBrowser, closeBrowser

def test_InvalidateRegistration():
    driver=startBrowser()
    driver.find_element('xpath',"//input[@name='firstname']").send_keys('@#$$%^^^')
    driver.find_element('xpath',"//input[@name='lastname']").send_keys('23456')
    driver.find_element('name','birthday_month').send_keys("66")
    driver.find_element('name','birthday_day').send_keys("abc")
    driver.find_element('name','birthday_year').send_keys("2002")
    driver.find_element('xpath',"//input[@value='1']").click()
    driver.find_element('xpath',"//input[@name='reg_email__']").send_keys("9847828584")
    driver.find_element('xpath',"//input[@aria-label='New password']").send_keys("Arati@1234")
    driver.find_element('xpath',"//button[@name='websubmit']").click()
    driver.find_element('link text','Already have an account?').click()
    closeBrowser()

   