from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def read_config(config_file):
    config = {}
    with open(config_file, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                name, value = line.split('=', 1)
                config[name.strip()] = value.strip()
            elif line:
                print(f"Warning: Skipping malformed line: {line}")
    return config

def automate_user_creation(username, password, first_name, last_name, contact_number, email, role, site_tag, user_password):
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.get("http://abc@example.com")
        wait = WebDriverWait(driver, 10)
        time.sleep(1)

        email_input = wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        password_input = driver.find_element(By.XPATH, '__')

        email_input.send_keys(username)
        time.sleep(1)
        password_input.send_keys(password)

        sign_in_button = driver.find_element(By.XPATH, '__')
        sign_in_button.click()

        manage_users = wait.until(EC.element_to_be_clickable((By.XPATH, '__')))
        manage_users.click()

        add_user = wait.until(EC.element_to_be_clickable((By.XPATH, '__')))
        add_user.click()

        first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        last_name_input = driver.find_element(By.XPATH, '__')
        contact_number_input = driver.find_element(By.XPATH, '__')
        email_input = driver.find_element(By.XPATH, '__')
        role_dropdown = driver.find_element(By.XPATH, '__')
        site_tag_dropdown = driver.find_element(By.XPATH, '__')
        user_password_input = driver.find_element(By.XPATH, '__')
        confirm_password_input = driver.find_element(By.XPATH, '__')

        first_name_input.send_keys(first_name)
        time.sleep(1)
        last_name_input.send_keys(last_name)
        time.sleep(1)
        contact_number_input.send_keys(contact_number)
        time.sleep(1)
        email_input.send_keys(email)
        time.sleep(1)

        role_dropdown.click()
        time.sleep(1)
        role_option = wait.until(EC.presence_of_element_located((By.XPATH, f'__, "{role}")]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", role_option)  # Scroll into view
        role_option.click()
        time.sleep(1)

        site_tag_dropdown.click()
        time.sleep(1)
        site_tag_option = wait.until(EC.presence_of_element_located((By.XPATH, f'__, "{site_tag}")]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", site_tag_option)  # Scroll into view
        site_tag_option.click()
        time.sleep(1)

        user_password_input.send_keys(user_password)
        time.sleep(1)
        confirm_password_input.send_keys(user_password)
        time.sleep(1)

        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "__")))

        save_user = wait.until(EC.element_to_be_clickable((By.XPATH, '__')))
        driver.execute_script("arguments[0].scrollIntoView(true);", save_user)
        driver.execute_script("arguments[0].click();", save_user)
        time.sleep(2)

        success_message = wait.until(EC.presence_of_element_located((By.XPATH, '__')))
        print("Success message found.")
        time.sleep(2)


    except Exception as e:
        print("An error occurred:", e)
    finally:
        if driver:
            input("Press Enter to close the browser")
            driver.quit()

if __name__ == "__main__":
    config = read_config("manage_users.txt") #file consisting of the required values
    website_username = config.get('username')
    website_password = config.get('password')
    
    first_name = config.get('first_name')
    last_name = config.get('last_name')
    contact_number = config.get('contact_number')
    email = config.get('email')
    role = config.get('role')
    site_tag = config.get('site_tag')
    user_password = config.get('user_password')
    
    automate_user_creation(website_username, website_password, first_name, last_name, contact_number, email, role, site_tag, user_password)
