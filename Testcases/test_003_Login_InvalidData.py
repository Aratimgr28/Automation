#from Base.InitiateDriver import startBrowser, closeBrowser
from selenium.webdriver import Firefox

def test_InvalidateLogin():
    driver=Firefox()
    driver.get("https:/www.facebook.com/login")
    driver.find_element('xpath',"//input[@name='email']").send_keys("Arati")
    driver.find_element('xpath',"//input[@name='pass']").send_keys("Arati@1234")
    driver.find_element('link text','Create new account').click()
    # closeBrowser()
    driver.close()
