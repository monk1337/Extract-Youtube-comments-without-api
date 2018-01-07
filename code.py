from selenium import webdriver

import time

driver=webdriver.Chrome()

driver.get('https://www.youtube.com/watch?v=iFPMz36std4')  #example video 

time.sleep(2)  #if you have slow internet , increase the value of sleep


driver.execute_script('window.scrollTo(1, 500);')
#Here is a trick , Youtube only load comments when you scroll just down of video , if you scroll bottom or elsewhere, comments will not load , so first scroll to that down part and wait for loading comments after that scroll to bottom or whenever you want 
#now wait let load the comments
time.sleep(5)

driver.execute_script('window.scrollTo(1, 3000);')



comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
for comment in comments:
    print(comment.text)
