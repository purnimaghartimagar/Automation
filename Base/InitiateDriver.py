from selenium.webdriver import Chrome,Edge,Firefox
from Library.ConfigReader import configRead

def startBrowser():
    global driver
    if configRead('Details','browser')=='chrome':
        driver=Chrome()
    elif configRead('Details','browser')=='edge':
        driver=Edge()
    else:
        driver=Firefox()        
    # driver.get("https://www.facebook.com/r.php")
    driver.get(configRead('Details','APP_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()