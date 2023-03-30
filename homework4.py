from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class homework4 :
    def empty (self):
        driver = webdriver.Chrome(ChromeDriverManager().install() )
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
       
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        
        loginBtn =driver.find_element(By.ID,"login-button")

        loginBtn.click()
        erroMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = erroMessage.text== "Epic sadface: Username is required" 
        print(testResult)
        print(f"Test result :{testResult}")
        sleep(5)


    def empty_password (self) :
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
    
        usernameInput.send_keys("Hanife")
        passwordInput.send_keys("")

        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(testResult)
        print(f"Test Result :{testResult}")
        sleep(5)
     
    def loced(self):
          driver =webdriver.Chrome(ChromeDriverManager().install())
          driver.maximize_window()
          driver.get("https://www.saucedemo.com/")

          usernameInput =driver.find_element(By.ID,"user-name")
          passwordInput =driver.find_element(By.ID,"password")
          usernameInput.send_keys("locked_out_user")
          passwordInput.send_keys("secret_sauce")

          loginBtn = driver.find_element(By.ID,"login-button")
          loginBtn.click()
          errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
          testResult = errorMessage.text==("Epic sadface: Sorry, this user has been locked out.")
          print(testResult)
          print(f"Test result :{testResult}")
          sleep(6)

    def x_button_close(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")

        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(3)

        errorButton= driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorButton.click()
        sleep(15)

    def routing(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput =driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")

        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()

        sleep(5)
    def urun_list(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput =driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")

        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()

        itemsList = driver.find_elements(By.CLASS_NAME, "inventory_item")
        if len(itemsList) == 6:
            print (f'the number of products displayed to the user {len(itemsList)} : True')

        

testClass = homework4()
# testClass.empty()
# testClass.empty_password()
# testClass.loced()
# testClass.x_button_close()
# testClass.routing()
testClass.urun_list()

while True:
    continue












