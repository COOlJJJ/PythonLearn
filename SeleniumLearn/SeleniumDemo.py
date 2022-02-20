# pip install selenium 安装selenium
# 下载chrome驱动 https://chromedriver.storage.googleapis.com/index.html
# http://www.byhy.net/tut/auto/selenium/01/ 参考文章
# 格式化 Ctrl+Alt+L
# C# JS Java都可以用这个工具
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# 最基础的操作
# 结合官网文档实操和百度即可。

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')
# title = wd.title
# url = wd.current_url
# print(title)
# print(url)
# 按下浏览器的后退按钮:
# wd.back()
# 按下浏览器的前进键:
# wd.forward()
# 刷新当前页面:
# wd.refresh()


# 获取整个元素对应的HTML
# 要获取整个元素对应的HTML文本内容，可以使用 element.get_attribute('outerHTML')
#
# 如果，只是想获取某个元素 内部 的HTML文本内容，可以使用 element.get_attribute('innerHTML')
#
# 获取输入框里面的文字
# 对于input输入框的元素，要获取里面的输入文本，用text属性是不行的，这时可以使用 element.get_attribute('value')
#
# 比如
#
# element = wd.find_element(By.ID, "input1")
# print(element.get_attribute('value')) # 获取输入框中的文本
# 获取元素文本内容2
# 通过WebElement对象的 text 属性，可以获取元素 展示在界面上的 文本内容。
#
# 但是，有时候，元素的文本内容没有展示在界面上，或者没有完全完全展示在界面上。 这时，用WebElement对象的text属性，获取文本内容，就会有问题。
#
# 出现这种情况，可以尝试使用 element.get_attribute('innerText') ，或者 element.get_attribute('textContent')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.ID, 'kw')
# 强制睡眠
sleep(2)
# 隐式超时 没超过该时间就会一直找
wd.implicitly_wait(2)

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys('Python' + Keys.ENTER)

# 定义一系列键盘操作 用链式写法
action = webdriver.ActionChains(wd)
search = wd.find_element(By.NAME, "q")
# Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
action.key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()

element.clear()
# 找一个元素
element1 = wd.find_element(By.NAME, 'wd')
# 多个元素
elements = wd.find_elements(By.CLASS_NAME, 'toplist1-right-num_3FteC toplist1-td_3zMd4')
# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)

# 根据标签查找
elementTags = wd.find_elements(By.TAG_NAME, 'div')
element_btn = wd.find_element(By.ID, 'su')
element1.send_keys('DDD')
element_btn.click()
