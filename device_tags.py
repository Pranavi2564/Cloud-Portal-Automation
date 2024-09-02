#code for automatic login to the cloud portal and creation of tags
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
def create_tag(username, password, tag_name, description):
    driver = None
    try:
        #options = webdriver.ChromeOptions()
        driver = webdriver.Chrome()
       
        driver.get("https://abc@example.com")
        time.sleep(2)  
 
       
        wait = WebDriverWait(driver, 10)
 
       
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        password_input = driver.find_element(By.XPATH, '__')
        time.sleep(1)  
        email_input.send_keys(username)
        time.sleep(1)  
        password_input.send_keys(password)
 
       
        sign_in_button = driver.find_element(By.XPATH, '__')
        time.sleep(1)  
        sign_in_button.click()
 
       
        manage_devices_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '__')))
        time.sleep(1)  
        manage_devices_button.click()
 
       
        device_tags_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '__')))
        time.sleep(1)  
        device_tags_button.click()
 
       
        add_tag_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '__')))
        time.sleep(1)  
        add_tag_button.click()
 
       
        tag_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        description_input = driver.find_element(By.XPATH, '__')
 
       
       
 
       
        time.sleep(1)  
        tag_name_input.send_keys(tag_name)
        time.sleep(1)  
        description_input.send_keys(description)
 
       
        create_tag_button = driver.find_element(By.XPATH, '__')
        time.sleep(1)
        create_tag_button.click()
 
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, '__')))
        time.sleep(2)
        #print("Tag created successfully: ", success_message.text)
 
    except Exception as e:
        print("An error occurred:", e)
    finally:
        if driver:
            input("Press Enter to close the browser...")
            driver.quit()
 
 
create_tag('xyz256@gmail.com', 'password', 'PranaviN_trialtag', 'Automated_TrialTag')