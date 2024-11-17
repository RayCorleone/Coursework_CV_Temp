import matplotlib.pyplot as plt
import numpy as np
import pickle as pk

rectified1 = pk.load(open('./data/rectified1.pkl','rb'))
rectified2 = pk.load(open('./data/rectified2.pkl','rb'))
disparity_map = pk.load(open('./data/disparity_map.pkl','rb'))

image_A = rectified1
image_B = disparity_map



fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(image_A, cmap='gray', extent=[0, image_A.shape[1], image_A.shape[0], 0])
ax.imshow(image_B, cmap='hot', alpha=0.5, extent=[0, image_B.shape[1], image_B.shape[0], 0])
ax.set_title("Overlay of Grayscale Images A and B")
ax.set_xlabel("X-axis (pixels)")
ax.set_ylabel("Y-axis (pixels)")
def on_mouse_move(event):
    if event.xdata is not None and event.ydata is not None:
        x, y = int(event.xdata), int(event.ydata)  # 获取鼠标位置的整数像素坐标
        if 0 <= x < image_B.shape[1] and 0 <= y < image_B.shape[0]:  # 检查坐标是否有效
            value_B = image_B[y, x]  # 获取灰度图片 B 的值
            print(f"Mouse Position: (X={x}, Y={y}), Disparity: {value_B}")

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
plt.show()
