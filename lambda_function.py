import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os

#Returns string containing carrier url if tracking number belongs to carrier
#Otherwise, returns false
def ABF_Freight(tracking,driver):
    driver.get("https://arcb.com/tools/tracking.html")

    element= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/article/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/form/textarea")))

    search = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/article/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/form/textarea")
    search.send_keys(tracking)

    try:
        enter= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/article/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/form/div[2]/button")
        enter.click()
        #driver.implicitly_wait(3)
        element= WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/article/div/div[1]/div/div/div/div[2]/div[1]/div[2]/abt-tracking-result/div/div/div[2]/div[1]/div/abt-tracking-status-bar")))
        result= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/article/div/div[1]/div/div/div/div[2]/div[1]/div[2]/abt-tracking-result/div/div/div[2]/div[1]/div/abt-tracking-status-bar")
        return "https://arcb.com/tools/tracking.html"
    except:
            return False


#Returns string containing carrier url if tracking number belongs to carrier
#Otherwise, returns false
def FedEx(tracking,driver):
    driver.get("https://www.fedex.com/en-us/shipping/freight-services/ltl.html")

    element= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div/nav/div/ul/div[2]/li/a")))
    print("Check Point 1")
    tracking_button= driver.find_element_by_xpath("/html/body/div[1]/header/div/div/nav/div/ul/div[2]/li/a")
    tracking_button.click()

    element= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div/nav/div/ul/div[2]/li/div/div[1]/div/form/div/input[1]")))
    print("Check Point 2")
    text= driver.find_element_by_xpath("/html/body/div[1]/header/div/div/nav/div/ul/div[2]/li/div/div[1]/div/form/div/input[1]")
    text.send_keys(tracking)

    button= driver.find_element_by_xpath("/html/body/div[1]/header/div/div/nav/div/ul/div[2]/li/div/div[1]/div/form/button")
    button.click()
     
    try:
        element= WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div[3]/div/div[1]/div/div[6]/div[1]/div/h4")))
        print("Check Point 3")
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div[3]/div/div[1]/div/div[6]/div[1]/div/h4")
        return "https://www.fedex.com/en-us/shipping/freight-services/ltl.html"
    except:
        
        return False       


#Returns string containing carrier url if tracking number belongs to carrier
#Otherwise, returns false
def NM_Transfer(tracking,driver):
    driver.get("https://www.nmtransfer.com/index")

    element= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.ID, "qtProNumber")))

    search = driver.find_element_by_id("qtProNumber")
    search.send_keys(tracking)

    send= driver.find_element_by_id("qtSubmit")
    send.click()
    
    try:
        element= WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "nmt-blue-bg")))
        driver.find_element_by_class_name("nmt-blue-bg")
        return "https://www.nmtransfer.com/index"
    except:
        return False


#Returns string containing carrier url if tracking number belongs to carrier
#Otherwise, returns false
def CH_Robinson(tracking, driver):
    return False
##    driver.get("https://online.chrobinson.com/tracking/#/")
##
##    element= WebDriverWait(driver,5).until(
##        EC.presence_of_element_located((By.ID, "trackingNumber")))
##
##    search = driver.find_element_by_id("trackingNumber")
##    search.send_keys(tracking)
##
##    send= driver.find_element_by_class_name("btn")
##    send.click()
##    
##    try:
##        element= WebDriverWait(driver,5).until(
##            EC.presence_of_element_located((By.CLASS_NAME, "nmt-blue-bg")))
##        driver.find_element_by_class_name("nmt-blue-bg")
##        driver.quit()
##        return True
##    except:
##        driver.quit()
##        return False


#Returns string containing carrier url if tracking number belongs to carrier
#Otherwise, returns false
def Panama_Transfer(tracking, driver):
    driver.get("https://www.panamatransfer.com/")

    element= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.ID, "proNo")))

    search = driver.find_element_by_id("proNo")
    search.send_keys(tracking)

    send= driver.find_element_by_id("Submit")
    send.click()

    try:
        element= WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/center/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/div/table/tbody/tr[1]/td/div/table/tbody/tr/td/table/tbody/tr[1]/td")))
        driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/div/table/tbody/tr[1]/td/div/table/tbody/tr/td/table/tbody/tr[1]/td")
        return "https://www.panamatransfer.com/"
    except:
        return False


#Returns string containing carrier url if tracking number belongs to carrier
#Otherwise, returns false
def RL_Carriers(tracking,driver):
    driver.get("https://www.rlcarriers.com/freight/shipping/shipment-tracing")

    element= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.ID, "ctl00_cphBody_txtTraceNumbers")))

    search = driver.find_element_by_id("ctl00_cphBody_txtTraceNumbers")
    search.send_keys(tracking)

    send= driver.find_element_by_class_name("btnSubmit")
    driver.execute_script("arguments[0].click();",send)

    try:
        element= WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "st-result")))
        driver.find_element_by_class_name("st-result")
        return "https://www.rlcarriers.com/freight/shipping/shipment-tracing"
    except:
        return False

#Dictionary mapping carriers to their test functions
#carrier_dict= {'N&M Transfer':NM_Transfer, 'R&L Carriers': RL_Carriers,'FedEx':FedEx,'Panama Transfer':Panama_Transfer, 'CH Robinson': CH_Robinson,'Canada Economy':FedEx, "ABF Freight":ABF_Freight}
carrier_dict= {'N&M Transfer':NM_Transfer, 'R&L Carriers': RL_Carriers,'FedEx':FedEx,'Panama Transfer':Panama_Transfer, "ABF Freight":ABF_Freight}


def lambda_handler(event, context):

    #Prepare Chrome Options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

    #Launch Headless Chrome
    driver = webdriver.Chrome(chrome_options=chrome_options)

    #Configure query params
    tracking= event['tracking']
    function= event['carrier']

    #Execute function test on specified carrier
    f= carrier_dict[function](tracking,driver)

    driver.close()
    driver.quit()

    # If tracking number matches carrier, return carrier url
    if f != False:
        return {
            'statusCode': 200,
            'body': f
            }
    #Otherwise, return false
    return {
        'statusCode': 200,
        'body': json.dumps(False)
    }


