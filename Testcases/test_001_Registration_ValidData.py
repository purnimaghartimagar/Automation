#from Base import InitiateDriver
from Base.InitiateDriver import startBrowser,closeBrowser
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Library.ConfigReader import ElementsRead

def test_ValidateRegistration():
    driver=startBrowser()
    #driver=InitiateDriver.startBrowser()
    # driver.find_element('xpath',"//input[@name='firstname']").send_keys('Shyam')
    # driver.find_element('xpath',"//input[@name='lastname']").send_keys('Thapa')
    
    driver.find_element('name',ElementsRead('Registration','fname')).send_keys('Shyam')
    driver.find_element('name',ElementsRead('Registration','lname')).send_keys('Thapa')
    
    month_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='birthday_month']"))
    month_dropdown.select_by_visible_text('Dec')
    day_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='birthday_day']"))
    day_dropdown.select_by_visible_text('10')
    year_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='birthday_year']"))
    year_dropdown.select_by_visible_text('2003')
    #InitiateDriver.closeBrowser()
    closeBrowser()
    import time
    time.sleep(50)
    
    #torun 
    #pytest-k function_name