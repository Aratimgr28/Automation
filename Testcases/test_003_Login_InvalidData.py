from Base.InitiateDriver import startBrowser, closeBrowser

def test_InvalidateLogin():
    driver=startBrowser()
    driver.find_element('xpath',"//input[@name='email']").send_keys("==========")
    driver.find_element('xpath',"//input[@name='pass']").send_keys("Arati@1234")
    driver.find_element('link text','Create new account').click()
    closeBrowser()

   