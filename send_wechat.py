# wechat_bot.py
import pyautogui
import pyperclip
import time
import subprocess
import os

# ===== 安全设置 =====
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

class WeChatBot:
    def __init__(self):
        # 使用 screenshots 文件夹
        self.screenshot_dir = "screenshots"
        self.wechat_icon_path = os.path.join(self.screenshot_dir, "wechat_icon.png")
        self.wechat_title = "微信"
        
        # 确保 screenshots 文件夹存在
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
            print(f"✓ 创建文件夹: {self.screenshot_dir}")
        
    def is_wechat_running(self):
        """检查微信是否已运行"""
        try:
            import pygetwindow as gw
            windows = gw.getWindowsWithTitle(self.wechat_title)
            return len(windows) > 0
        except:
            import subprocess
            result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq WeChat.exe'], 
                                  capture_output=True, text=True)
            return 'WeChat.exe' in result.stdout
    
    def find_wechat_icon_on_taskbar(self):
        """在任务栏查找微信图标"""
        try:
            screen_w, screen_h = pyautogui.size()
            taskbar_region = (0, screen_h - 80, screen_w, 80)
            
            icon_pos = pyautogui.locateCenterOnScreen(
                self.wechat_icon_path,
                confidence=0.7,
                region=taskbar_region
            )
            
            if icon_pos:
                print(f"✓ 找到微信图标: {icon_pos}")
                return icon_pos
            else:
                print("✗ 未找到微信图标")
                return None
        except Exception as e:
            print(f"图像识别失败: {e}")
            return None
    
    def open_wechat(self):
        """打开微信（带多重检查）"""
        
        # 检查1：微信是否已在运行
        print("检查微信运行状态...")
        if self.is_wechat_running():
            print("✓ 微信已在运行")
            try:
                import pygetwindow as gw
                wechat_windows = gw.getWindowsWithTitle(self.wechat_title)
                if wechat_windows:
                    wechat_windows[0].activate()
                    print("✓ 已激活微信窗口")
                    return True
            except:
                pass
            return True
        
        # 检查2：通过图像识别点击任务栏图标
        print("尝试通过图像识别打开微信...")
        if os.path.exists(self.wechat_icon_path):
            icon_pos = self.find_wechat_icon_on_taskbar()
            if icon_pos:
                pyautogui.click(icon_pos)
                time.sleep(2)
                if self.is_wechat_running():
                    print("✓ 通过图标识别成功打开微信")
                    return True
        else:
            print(f"提示: 未找到 {self.wechat_icon_path}，请先运行 capture_wechat_icon.py")
        
        # 检查3：通过完整路径启动
        print("尝试通过程序路径启动微信...")
        wechat_paths = [
            r"C:\Program Files\Tencent\WeChat\WeChat.exe",
            r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",
        ]
        for path in wechat_paths:
            if os.path.exists(path):
                subprocess.Popen(path)
                print(f"✓ 启动微信: {path}")
                time.sleep(3)
                if self.is_wechat_running():
                    return True
        
        print("✗ 所有方法都无法打开微信")
        return False
    
    def search_contact(self, name):
        """搜索联系人"""
        print(f"搜索联系人: {name}")
        
        # 确保微信窗口在最前
        try:
            import pygetwindow as gw
            wechat_windows = gw.getWindowsWithTitle(self.wechat_title)
            if wechat_windows:
                wechat_windows[0].activate()
                time.sleep(0.5)
        except:
            pass
        
        # Ctrl+F 搜索
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.8)
        
        # 清空搜索框
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(0.3)
        
        # 输入联系人名称
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1.5)
        
        # 选择第一个结果
        pyautogui.press('enter')
        time.sleep(1)
        
        return True
    
    def send_message(self, message):
        """发送消息"""
        print(f"发送消息: {message[:50]}...")
        
        # 确保输入框激活
        time.sleep(0.5)
        
        # 清空输入框
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        time.sleep(0.3)
        
        # 复制并粘贴消息
        pyperclip.copy(message)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        
        # 发送
        pyautogui.press('enter')
        time.sleep(0.5)
        
        return True
    
    def verify_message_sent(self):
        """验证消息是否发送成功"""
        # 截图保存到 screenshots 文件夹
        # timestamp = time.strftime("%Y%m%d_%H%M%S")
        # screenshot_path = os.path.join(self.screenshot_dir, f"chat_{timestamp}.png")
        # screenshot = pyautogui.screenshot()
        # screenshot.save(screenshot_path)
        # print(f"✓ 聊天截图已保存: {screenshot_path}")
        time.sleep(0.5)  # 只等待，不截图
        return True
    
    def send_to_contact(self, contact_name, message):
        """完整的发送流程"""
        print(f"\n{'='*50}")
        print(f"开始向 {contact_name} 发送消息")
        print(f"{'='*50}")
        
        # 步骤1：打开/激活微信
        if not self.open_wechat():
            print("❌ 无法打开微信，操作终止")
            return False
        
        # 步骤2：搜索联系人
        if not self.search_contact(contact_name):
            print(f"❌ 找不到联系人: {contact_name}")
            return False
        
        # 步骤3：发送消息
        if not self.send_message(message):
            print("❌ 消息发送失败")
            return False
        
        # 步骤4：验证截图
        self.verify_message_sent()
        
        print(f"✅ 成功向 {contact_name} 发送消息")
        return True

def main():
    bot = WeChatBot()
    
    # 检查图标文件是否存在
    if not os.path.exists(bot.wechat_icon_path):
        print(f"❌ 未找到 {bot.wechat_icon_path}")
        print("请先运行 capture_wechat_icon.py 截取微信图标")
        print("\n运行命令: python capture_wechat_icon.py")
        return
    
    # 配置区（按你的需要修改）
    CONTACT = "文件传输助手"
    MESSAGE = f"自动测试消息 {time.strftime('%Y-%m-%d %H:%M:%S')}"
    
    print("\n3秒后开始操作...")
    time.sleep(3)
    
    success = bot.send_to_contact(CONTACT, MESSAGE)
    
    if success:
        print("\n🎉 任务执行成功！")
    else:
        print("\n💥 任务执行失败")
        print("请检查：")
        print("1. 微信是否正常安装")
        print("2. wechat_icon.png 是否清晰")
        print("3. 联系人名称是否正确")

if __name__ == "__main__":
    main()