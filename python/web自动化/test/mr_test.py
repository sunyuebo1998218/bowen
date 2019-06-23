from selenium import webdriver
from time import sleep
from web自动化.data.导入数据 import shuju
def mr(x):
    dr = webdriver.Firefox()
    dr.get('http://www.moore.ren/')
    sleep(2)
    # dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/li[1]').click()
    # sleep(2)
    # a = dr.window_handles
    # dr.switch_to.window(a[-1])
    # dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('17629712980')
    # dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('A1998218')
    # dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/form/input[1]').click()
    sleep(1)
    dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[4]/form/input[1]').send_keys(x)
    dr.find_element_by_xpath('//*[@id="search-submit"]').click()
    try:
        c = dr.find_element_by_xpath('/html/body/div[2]/div/div/div[6]/div/ul/li/p[1]').text
        return c

    except:
        b = dr.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/span[2]').text
        return b
# for i in shuju():
# #     mr(i[0])