import cv2
import pyvirtualcam
import tkinter as tk
from tkinter import simpledialog


def get_video_source():
    # 创建一个隐藏的 tkinter 根窗口
    root = tk.Tk()
    root.withdraw()
    # 弹出对话框，让用户输入视频源的URL或本地文件路径
    video_source = simpledialog.askstring("听风说", "输入视频源的URL或本地文件路径:")
    return video_source


def main():
    # 从用户输入中获取视频源
    video_source = get_video_source()

    # 如果用户未提供视频源，则退出
    if video_source is None:
        print("未提供视频源。退出...")
        return

    # 打开视频流
    cap = cv2.VideoCapture(video_source)

    # 检查视频流是否被正确打开
    if not cap.isOpened():
        print("错误：无法打开视频源。")
        return

    # 获取视频帧的尺寸
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 使用与视频流相同尺寸的虚拟摄像头
    with pyvirtualcam.Camera(width=frame_width, height=frame_height, fps=30) as cam:
        # 循环读取视频流中的每一帧
        while True:
            # 读取一帧
            ret, frame = cap.read()

            # 检查是否成功读取到一帧
            if not ret:
                print("错误：无法读取帧。")
                break

            # 在这里添加任何你认为必要的图像处理步骤，例如颜色空间转换或调整

            # 将视频帧发送到虚拟摄像头
            cam.send(frame)

            # 显示当前帧（可选）
            cv2.imshow('视频流', frame)

            # 按 'q' 键退出循环
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # 释放视频流对象
    cap.release()

    # 关闭所有打开的窗口
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
