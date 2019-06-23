from selenium import webdriver
from time import sleep
dr = webdriver.Firefox()
dr.get('http://qzone.qq.com')
sleep(2)
dr.switch_to.frame('login_frame')
dr.find_element_by_css_selector('html body div#login.login div#bottom_qlogin.bottom.hide a#switcher_plogin.link').click()
dr.find_element_by_css_selector('html body div#login.login div#web_qr_login.web_qr_login div#web_qr_login_show.web_qr_login_show div#web_login.web_login div.login_form form#loginform div#uinArea.uinArea div.inputOuter input#u.inputstyle').send_keys('1004745584')
dr.find_element_by_css_selector('html body div#login.login div#web_qr_login.web_qr_login div#web_qr_login_show.web_qr_login_show div#web_login.web_login div.login_form form#loginform div#pwdArea.pwdArea div.inputOuter input#p.inputstyle.password').send_keys('SYB.15036785126')
dr.find_element_by_css_selector('html body div#login.login div#web_qr_login.web_qr_login div#web_qr_login_show.web_qr_login_show div#web_login.web_login div.login_form form#loginform div.submit a.login_button input#login_button.btn').click()