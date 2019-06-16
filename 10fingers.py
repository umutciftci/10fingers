from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = "YOURDRIVERPATH"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://10fastfingers.com/typing-test/turkish/")

time.sleep(1)
#get the word
for i in range(1,289):
    word = driver.find_element_by_xpath("//*[@id='row1']/span[%d]" %(i,))

#input box
    input_box = driver.find_element_by_xpath("//*[@id='inputfield']")
    input_box.send_keys(word.text + " ")







