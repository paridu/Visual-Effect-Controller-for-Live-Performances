import PySimpleGUI as sg
import lunar_tools as lt
import numpy as np
import time

# ตั้งค่าขนาดหน้าจอสำหรับการแสดงผลภาพ
sz = (800, 800)

# สร้าง renderer สำหรับการแสดงผลภาพ
renderer = lt.Renderer(width=sz[1], height=sz[0])

# ออกแบบ layout ของ GUI โดยใช้ PySimpleGUI
layout = [
    [sg.Text('Brightness'), sg.Slider(range=(0, 100), orientation='h', size=(20, 15), default_value=50, key='-BRIGHTNESS-')],
    [sg.Text('Color Shift'), sg.Slider(range=(0, 100), orientation='h', size=(20, 15), default_value=50, key='-COLOR_SHIFT-')],
    [sg.Text('Speed'), sg.Slider(range=(0, 100), orientation='h', size=(20, 15), default_value=50, key='-SPEED-')],
    [sg.Button('Update')]
]

window = sg.Window('Visual Effect Controller', layout)

while True:
    event, values = window.read(timeout=10)
    if event == sg.WINDOW_CLOSED:
        break

    # รับค่าจาก sliders
    brightness = values['-BRIGHTNESS-'] / 100
    color_shift = values['-COLOR_SHIFT-'] / 100
    speed = values['-SPEED-'] / 100

    # สร้างภาพสุ่มเพื่อจำลองการแสดงผล
    image = np.random.rand(sz[0], sz[1], 3) * 255

    # ปรับ brightness ของภาพ
    image = image * brightness

    # ปรับการเลื่อนสี (color shift)
    image[:, :, 0] = np.clip(image[:, :, 0] + color_shift * 100, 0, 255)
    image[:, :, 1] = np.clip(image[:, :, 1] + color_shift * 100, 0, 255)

    # เพิ่มเอฟเฟกต์การเคลื่อนไหวตามค่า speed
    shift_amount = int(speed * 10)
    image = np.roll(image, shift_amount, axis=0)

    # แสดงผลภาพบนหน้าจอ
    renderer.render(image)

window.close()
