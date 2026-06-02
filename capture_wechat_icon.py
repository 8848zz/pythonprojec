# capture_wechat_icon.py
import pyautogui
import time
from PIL import Image
import os

class WeChatIconCapture:
    def __init__(self):
        # 创建 screenshots 文件夹
        self.screenshot_dir = "screenshots"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
            print(f"✓ 创建文件夹: {self.screenshot_dir}")
        
        self.output_path = os.path.join(self.screenshot_dir, "wechat_icon.png")
        
    def capture(self):
        """交互式截取微信图标"""
        print("\n" + "="*50)
        print("微信图标截图工具")
        print("="*50)
        
        # 检查是否已存在
        if os.path.exists(self.output_path):
            print(f"\n发现已存在图标文件: {self.output_path}")
            choice = input("是否重新截图？(y/n): ")
            if choice.lower() != 'y':
                print("跳过截图，使用已有文件")
                return True
        
        print("\n请按以下步骤操作：")
        print("1. 确保微信已固定在任务栏")
        print("2. 将鼠标移到任务栏的【微信图标】正中间")
        print("3. 不要移动鼠标，准备截图")
        
        input("\n按回车开始截图（5秒后自动截取）...")
        
        # 倒计时
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        
        # 获取鼠标位置并截图
        x, y = pyautogui.position()
        print(f"鼠标位置: ({x}, {y})")
        
        # 截取图标周围60x60像素区域
        region = (x-30, y-30, 60, 60)
        img = pyautogui.screenshot(region=region)
        img.save(self.output_path)
        
        # 显示截图信息
        print(f"\n✓ 微信图标已保存到: {self.output_path}")
        print(f"  图标尺寸: {img.size}")
        
        # 可选：显示截图预览
        preview = input("\n是否预览截图？(y/n): ")
        if preview.lower() == 'y':
            img.show()
        
        print("\n✓ 截图完成！现在可以运行主程序了。")
        return True
    
    def test_capture(self):
        """测试截图是否可用"""
        if not os.path.exists(self.output_path):
            print(f"请先运行截图功能，找不到文件: {self.output_path}")
            return False
        
        print("\n测试图标识别...")
        try:
            screen_w, screen_h = pyautogui.size()
            # 只在任务栏区域搜索
            pos = pyautogui.locateCenterOnScreen(
                self.output_path,
                confidence=0.7,
                region=(0, screen_h-80, screen_w, 80)
            )
            if pos:
                print(f"✓ 图标识别成功，位置: {pos}")
                return True
            else:
                print("✗ 图标识别失败，请重新截图")
                return False
        except Exception as e:
            print(f"识别出错: {e}")
            return False

def main():
    capture = WeChatIconCapture()
    
    print("\n选项：")
    print("1. 截取微信图标")
    print("2. 测试图标识别效果")
    print("3. 退出")
    
    choice = input("\n请选择 (1/2/3): ")
    
    if choice == '1':
        capture.capture()
    elif choice == '2':
        capture.test_capture()
    else:
        print("退出")

if __name__ == "__main__":
    main()