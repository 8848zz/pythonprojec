# WeChat RPA Bot

## 环境
- Python 3.10.11, 虚拟环境: `.venv/`
- 依赖: `pyautogui`, `pyperclip`, `Pillow`, `pygetwindow`, `opencv-python`

## 运行顺序（必须）
1. `capture_wechat_icon.py` — 截取任务栏微信图标（生成 `screenshots/wechat_icon.png`）
2. `prepare_screenshots.py` — 截取搜索框和联系人参考图（可选）
3. `send_wechat.py` — 自动发送消息主程序

## 使用方式
- 发送目标和消息内容在 `send_wechat.py:212-213` 修改 `CONTACT` 和 `MESSAGE`
- 首次使用必须运行 `capture_wechat_icon.py`，否则 `send_wechat.py` 无法启动

## 约束
- 运行期间请勿移动鼠标或键盘（pyautogui 自动操作中）
- 截图图片位于 `screenshots/`，不提交到 Git
