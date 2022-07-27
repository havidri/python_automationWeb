import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"//span[contains(text(),'Products')]").text
        self.assertEqual(response_data, 'PRODUCTS')

    def test_b_failed_login_with_lock_out_user(self): 
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("locked_out_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        self.assertEqual(response_data, 'Epic sadface: Sorry, this user has been locked out.')

    def test_c_failed_login_with_user_not_registered(self): 
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("notregistered")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("abcdefg")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        self.assertEqual(response_data, 'Epic sadface: Username and password do not match any user in this service')

    
    def test_d_order_product(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        #Add to Cart
        browser.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
        time.sleep(1)
        browser.find_element(By.ID,"checkout").click()
        time.sleep(1)

        #Checkout Information
        browser.find_element(By.ID,"first-name").send_keys("Havid")
        time.sleep(1)
        browser.find_element(By.ID,"last-name").send_keys("Havid")
        time.sleep(1)
        browser.find_element(By.ID,"postal-code").send_keys("12345")
        time.sleep(1)
        browser.find_element(By.ID,"continue").click()
        time.sleep(1)
        browser.find_element(By.ID,"finish").click()
        time.sleep(1)


        # validasi
        response_data = browser.find_element(By.XPATH,"//h2[@class='complete-header']").text
        self.assertEqual(response_data, 'THANK YOU FOR YOUR ORDER')

    def test_e_order_product_first_name_empty(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        #Add to Cart
        browser.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
        time.sleep(1)
        browser.find_element(By.ID,"checkout").click()
        time.sleep(1)

        #Checkout Information
        browser.find_element(By.ID,"first-name").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"last-name").send_keys("Havid")
        time.sleep(1)
        browser.find_element(By.ID,"postal-code").send_keys("12345")
        time.sleep(1)
        browser.find_element(By.ID,"continue").click()
        time.sleep(1)


        # validasi
        response_data = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        self.assertEqual(response_data, 'Error: First Name is required')

    def test_f_order_product_last_name_empty(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        #Add to Cart
        browser.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
        time.sleep(1)
        browser.find_element(By.ID,"checkout").click()
        time.sleep(1)

        #Checkout Information
        browser.find_element(By.ID,"first-name").send_keys("Havid")
        time.sleep(1)
        browser.find_element(By.ID,"last-name").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"postal-code").send_keys("12345")
        time.sleep(1)
        browser.find_element(By.ID,"continue").click()
        time.sleep(1)


        # validasi
        response_data = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        self.assertEqual(response_data, 'Error: Last Name is required')

    def test_g_order_product_last_name_empty(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        #Add to Cart
        browser.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
        time.sleep(1)
        browser.find_element(By.ID,"checkout").click()
        time.sleep(1)

        #Checkout Information
        browser.find_element(By.ID,"first-name").send_keys("Havid")
        time.sleep(1)
        browser.find_element(By.ID,"last-name").send_keys("Havid")
        time.sleep(1)
        browser.find_element(By.ID,"postal-code").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"continue").click()
        time.sleep(1)


        # validasi
        response_data = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        self.assertEqual(response_data, 'Error: Postal Code is required')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()