from selenium import webdriver
browser = webdriver.Firefox()
response = browser.get("https://github.com")
signin_link = browser.find_element_by_link_text("Sign in")
click = signin_link.click()
username_box = browser.find_element_by_id("login_field")
username_box.send_keys("****")

password = browser.find_element_by_id("password")
password.send_keys("*****")
password.submit()

assert "username" in browser.page_source

# exit browser
browser.quit()
