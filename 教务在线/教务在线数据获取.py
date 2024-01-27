import requests
from selenium import webdriver
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# 访问的网页url
login_url = 'https://webvpn.lntu.edu.cn/http/77726476706e69737468656265737421a1a70fcd767e3a033059da/ca/login?service=https%3A%2F%2Fwebvpn.lntu.edu.cn%2Flogin%3Fcas_login%3Dtrue'
# 初始化浏览器
driver = webdriver.Edge()
# 访问这个url
driver.get(login_url)

  # 登录输入密码
time.sleep(3)
# 填上你的账号
driver.find_element(By.XPATH, "//*[@id='un']").send_keys('')
time.sleep(1)
# 填上你的密码
driver.find_element(By.XPATH, "//*[@id='pd']").send_keys('')
time.sleep(6)
# 验证码怎么破解我还没写出来只能手动输入
driver.find_element(By.XPATH,"//*[@id='index_login_btn']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='__layout']/div/div/div[3]/div/div[2]/div/div[1]/div/div[1]/div/div[2]").click()
time.sleep(5)

# 切换到第二个窗口
all_handles = driver.window_handles
driver.switch_to.window(all_handles[1])

# 悬停在我的上面
hover = driver.find_element("xpath","//*[@id='main-nav']/ul/li[2]/a")
action = ActionChains(driver)
action.move_to_element(hover).perform()
time.sleep(5)

# 点击我的成绩
driver.find_element(By.XPATH,"//*[@id='main-nav']/ul/li[2]/ul/li[5]").click()
time.sleep(4)

# 悬停别的位置
hover2 = driver.find_element("xpath","//*[@id='main-top']/div/a/img[1]")
action = ActionChains(driver)
action.move_to_element(hover2).perform()
time.sleep(5)

# 找到iframe
iframe = driver.find_element(By.XPATH, "/html/body/div[3]/div/iframe")
driver.switch_to.frame(iframe)
dit = {}
i = 1

while True:
    try:
        key_j = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[4]").text
        value_j = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[12]").text
        dit[key_j] = value_j
        # 打印当前行的 XPath
        print(f"Processing row: {key_j} - {value_j}")
        i += 1  # 增加 i 的值，以访问下一行
    except NoSuchElementException:
        # 捕获到异常，说明当前行不存在，停止遍历
        print("No more rows to process.")
        break
print(dit)
# dit = {}
# for i in range(1,10):
#     print(f'/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[4]')
#     print(f'/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[12]')
#     key_j = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[4]").text
#     value_j = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/table/tbody/tr[{i}]/td[12]").text
#     dit[key_j] = value_j
# print(dit)
# print(form_element)
# time.sleep(50)

time.sleep(20)

driver.quit()
