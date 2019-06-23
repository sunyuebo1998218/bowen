# web自动化 selenium :web自动化测试的工具集
#都是selenium1.0的组成
#1.selenium IDE 是火狐浏览器的一个插件
#作用：录制和回放
#2.selenium Grid 是自动化测试的一个辅助工具 作用：可以实现不同的环境中同时执行测试
#3.selenium Rc 是selenium 1.0 自动化测试的核心 作用：控制浏览器行为
#selenium2.0的组成：
#selenium1.0的所有工具+webdriver
#webdriver是selenium2.0的核心 作用：控制浏览器的行为
#RC 和 webdriver 的区别：
#RC:通过将测试代码转化成javascript能够识别的动作，从而间接的去控制浏览器
#webdriver：通过将浏览器的所有的原生接口集成到webdriver驱动中，然后通过驱动直接控制浏览器
#装驱动webdriver.exe
# python代码，控制浏览器打开网页
# 驱动，不同浏览器对应不同驱动
#定位：
from selenium import webdriver
from time import sleep
# dr = webdriver.Firefox()
# # 请求要打开的网页
# dr.get('http://www.baidu.com')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# # 打印打开的网页的标题
# print(dr.title)
# # 打印当前网页的网址
# print(dr.current_url)
# # 设置浏览器窗口大小
# dr.set_window_size(400,400)
# #设置浏览器的位置
# dr.set_window_position(400,400)
# # 最大化浏览器
# dr.maximize_window()
# # 最小化浏览器
# dr.minimize_window()
# dr.get('http://www.jd.com')
# sleep(2)
# # 回退
# dr.back()
# sleep(2)
# # 前进
# dr.forward()
# # 最重要：定位
# # 通过id定位 send_keys(输入) click(点击)
# dr.find_element_by_id('kw').send_keys('python')
# sleep(2)
# # 点击百度一下
# dr.find_element_by_id('su').click()
# # 通过name定位
# dr.find_element_by_name('wd').send_keys("python")
# dr.find_element_by_id('su').click()
# # 通过class属性定位
# dr.find_element_by_class_name('s_ipt').send_keys("python")
# dr.find_element_by_id('su').click()
# # 不论采用任何方式定位，要保证定位的唯一性
# dr.find_element_by_class_name('mn').click()
# # 根据文本定位
# dr.find_element_by_link_text('新闻').click()
# # 模糊定位
# dr.find_element_by_partial_link_text('hao').click
# # 根据标签来定位
# dr.find_element_by_tag_name()
# # 根据路径来定位
# dr.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/a[1]').click()
# # 根据css来定位
# dr.find_element_by_css_selector('a.mn:nth-child(1)').click()
# dr.get('http://qzone.qq.com')
# sleep(2)
# dr.switch_to.frame('login_frame')
# dr.find_element_by_css_selector('#switcher_plogin').click()
# dr.find_element_by_css_selector('#u').send_keys('1004745584')
# dr.find_element_by_css_selector('#p').send_keys('SYB.15036785126')
# dr.find_element_by_css_selector('#login_button').click()

#定位一组对象
# dr = webdriver.Firefox()
# 请求要打开的网页
# dr.get('http://www.baidu.com')
# sleep(5)
# ww=dr.find_elements_by_class_name('mn')
# print(len(ww))
# for i in ww:
#     b=i.get_attribute('href')#获取某个属性
#     print(b)
#层级定位:先定位一个大的方向 再从大的区域中定位。
# dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# sleep(5)
# dr.find_element_by_id('J_roomCountList').find_elements_by_tag_name('option')
# print(len(ww))
# for i in ww:
#     i.click()
#     sleep(2)

#模拟鼠标移动
# from selenium.webdriver.common.action_chains import ActionChains
# # dr.get('https://www.jd.com/?cu=true&utm_source=c.duomai.com&utm_medium=tuiguang&utm_campaign=t_16282_87252132&utm_term=8a4c7486bf9f4c0899a3d95cf2ed0d4c')
# # sleep(5)
# # a=dr.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div/ul').find_elements_by_class_name('cate_menu_lk')
# # print(len(a))
# #
# # for i in a:
# #     ActionChains(dr).move_to_element(i).perform() #移动的代码（移动到定位的位置）
# #     sleep(2)
# from selenium import webdriver
# from time import sleep
# dr = webdriver.Firefox()
# dr.get('http://qzone.qq.com')
# sleep(2)
# dr.switch_to.frame('login_frame')
# dr.find_element_by_css_selector('html body div#login.login div#bottom_qlogin.bottom.hide a#switcher_plogin.link').click()
# sleep(2)
# dr.find_element_by_css_selector('html body div#login.login div#web_qr_login.web_qr_login div#web_qr_login_show.web_qr_login_show div#web_login.web_login div.login_form form#loginform div#uinArea.uinArea div.inputOuter input#u.inputstyle').send_keys('110584558')
# sleep(2)
# dr.find_element_by_css_selector('html body div#login.login div#web_qr_login.web_qr_login div#web_qr_login_show.web_qr_login_show div#web_login.web_login div.login_form form#loginform div#pwdArea.pwdArea div.inputOuter input#p.inputstyle.password').send_keys('SYB.15036785126')
# sleep(2)
# dr.find_element_by_css_selector('html body div#login.login div#web_qr_login.web_qr_login div#web_qr_login_show.web_qr_login_show div#web_login.web_login div.login_form form#loginform div.submit a.login_button input#login_button.btn').click()
# sleep(2)
# dr.switch_to.frame('tcaptcha_iframe')
# b=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
# #drag_and_drop 两个参数（起始位置，结束位置）
# # ActionChains(dr).drag_and_drop(b,c).perform()
# #drag_and_drop_by_offset(三个参数)（起始位置，x坐标，y坐标）
# ActionChains(dr).drag_and_drop_by_offset(b,170,0).perform()


#iframe:内嵌框架（窗口）
#dr.switch_to_frame()切换到某个框架上去  ，只能通过id得值，通过name得值切换
#dr.switch_to_default_content()回退到最开始的页面上
#dr.switch_to.parent_frame() 回退到上一个框架中

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui#导入模块只能等待
#任何浏览器管理窗口的原理   将每个窗口用一个特定的字符来标识（专业术语叫句柄）
#只需要获取到每个窗口的标识号
#通过切换标识号，就能达到切换窗口目的
dr = webdriver.Firefox()
dr.get('https://www.baidu.com/')
# sleep(2)#强制休息
#智能等待 10叫最大等待时间
unit=ui.WebDriverWait(dr,10)
#检测hao123是否出现 如果出现就执行下面的代码，如果没出现就一直等待，最大等待十秒
unit.until(lambda dr: dr.find_element_by_link_text('hao123').is_displayed())
dr.find_element_by_link_text('新闻').click()
# print(dr.title)
# #获取当前窗口的标识
# print(dr.current_window_handle)
# sleep(2)
# dr.find_element_by_css_selector('html.ua-windows.ua-ff67 body div#anony-nav div.anony-nav-links ul li a.lnk-book').click()
# sleep(2)
# #获取所有已开窗口的标识号
# a=dr.window_handles
# #切换窗口
# dr.switch_to.window(a[-1])
# print(dr.title)
# for i in range(0,100000,500):
#     qq="var q=document.documentElement.scrollTop={}".format(i)
#     dr.execute_script(qq)
#     sleep(2)

# #处理弹出框
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# #切换到弹出框上去
# ww=dr.switch_to_alert()
# #获取弹出框的数据
# print(ww.text)
# #点击确定
# ww.accept()
# #点击取消
# ww.dismiss()
# #向弹出框输入数据
# ww.send_keys()
