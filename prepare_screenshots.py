# prepare_screenshots.py
import pyautogui
import time

print("=== 截图准备工具 ===")
print("请打开微信主界面（能看到聊天列表的那个窗口）")
input("按回车开始截图...")

# 1. 截取搜索框图标
print("\n1. 将鼠标移到微信主界面的【搜索框】上（那个放大镜图标的位置）")
input("放好后按回车，3秒后自动截图...")
time.sleep(3)
# 以鼠标位置为中心，截取 200x50 的区域
x, y = pyautogui.position()
search_img = pyautogui.screenshot(region=(x-100, y-25, 200, 50))
search_img.save("screenshots/search_box.png")
print("✓ 搜索框截图已保存")

# 2. 截取联系人（可选，用来验证）
print("\n2. 将鼠标移到任意一个【联系人】名字上")
input("放好后按回车，3秒后自动截图...")
time.sleep(3)
x, y = pyautogui.position()
contact_img = pyautogui.screenshot(region=(x-100, y-20, 200, 40))
contact_img.save("screenshots/contact.png")
print("✓ 联系人截图已保存")

print("\n截图完成！现在 screenshots 文件夹里应该有 search_box.png 和 contact.png")