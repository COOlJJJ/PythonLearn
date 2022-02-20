import pyautogui

# 建议PAUSE和FAILSAFE一起使用。
# 程序如果失控了，需要中断PyAutoGUI函数，就把鼠标光标在屏幕左上角。要禁用这个特性，就把FAILSAFE设置成False
pyautogui.FAILSAFE = False

# 通过把pyautogui.PAUSE设置成float或int时间（秒），可以为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。在函数循环执行的时候，这样做可以让PyAutoGUI运行的慢一点，非常有用
pyautogui.PAUSE = 2.0

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)  # 返回所用显示器的分辨率； 输出：Size(width=1920, height=1080)
# Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表
# 移动到绝对位置  向右移动x ，向下移动 y, 这个过程持续x秒钟
# for i in range(10):
#     pyautogui.moveTo(300, 300, duration=0.25)
#     pyautogui.moveTo(400, 300, duration=0.25)
#     pyautogui.moveTo(400, 400, duration=0.25)
#     pyautogui.moveTo(300, 400, duration=0.25)
# 相对位置
# for i in range(10):
#     pyautogui.moveRel(100, 0, duration=0.25)
#     pyautogui.moveRel(0, 100, duration=0.25)
#     pyautogui.moveRel(-100, 0, duration=0.25)
#     pyautogui.moveRel(0, -100, duration=0.25)

#获取鼠标位置
# x, y = pyautogui.position()
# print(x,y)

# 鼠标点击
#
# 使用click()函数发送虚拟鼠标点击，默认情况下在鼠标所在的位置点击左键。函数原型：
#
# pyautogui.click(x=cur_x, y=cur_y, button='left')
# x，y是要点击的位置，默认是鼠标当前位置
# button是要点击的按键，有三个可选值：‘left’, ‘middle’,  ‘right’
# pyautogui.click(10,10)   # 鼠标点击指定位置，默认左键
# pyautogui.click(10,10,button='left')  # 单击左键
# pyautogui.click(1000,300,button='right')  # 单击右键
# pyautogui.click(1000,300,button='middle')  # 单击中间
# pyautogui.doubleClick(10,10)  # 指定位置，双击左键
# pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
# pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

#  双击左键
# pyautogui.click(clicks=2)
# #  两次单击之间停留0.25秒
# pyautogui.click(clicks=2, interval=0.25)
# #  三击右键
# pyautogui.click(button='right', clicks=2, interval=0.25)


# 拖动到指定位置
# 将鼠标拖动到指定的坐标；duration 的作用是设置移动时间，所有的gui函数都有这个参数，而且都是可选参数
pyautogui.dragTo(100,300,duration=1)

# 按方向拖动
# 向右拖动100px，向下拖动500px, 这个过程持续 1 秒钟
# pyautogui.dragRel(100,500,duration=4)   # 第一个参数是左右移动像素值，第二个是上下

# pyautogui.scroll(300)  # 向下滚动300个单位；
#键盘事件
# pyautogui.keyDown('shift')    # 按下shift
# pyautogui.press('4')    # 按下 4
# pyautogui.keyUp('shift')
# 第一参数是输入内容，第二个参数是每个字符间的间隔时间
# pyautogui.typewrite('$*……%……￥', 0.5)
# ：typewrite 还可以传入单字母的列表
# pyautogui.typewrite(['T','i','s','left','left','h',])
# pyautogui.moveTo(screenWidth / 2, screenHeight / 2)


