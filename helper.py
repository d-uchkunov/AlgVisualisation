# import tkinter as tk
# import random
# import ctypes as ct
#
#
# def tksleep(t):
#     # emulating time.sleep(seconds)
#     ms = int(t*1000)
#     win = tk._get_default_root('sleep')
#     var = tk.IntVar(win)
#     win.after(ms, var.set, 1)
#     win.wait_variable(var)
#
#
# def mvbox(canvas, box, pos, y=0, speed=0.003):
#     direction = 1
#     if y != 0:
#         if pos < 0:
#             direction = -1
#         for i in range(abs(y)):
#             tksleep(speed)
#             canvas.move(box, 0, direction*1)
#     else:
#         if pos < 0:
#             direction = -1
#         for i in range(abs(pos)):
#             tksleep(speed)
#             canvas.move(box, direction*1, 0)
#
# def swap(canvas, item1, item2, speed = 0.003):
#     first_run = True
#     if first_run:
#         # if item1 > item2:
#         #     tmp = item1
#         #     item1 = item2
#         #     item2 = tmp
#         pos = int(abs(canvas.coords(item1)[0]-canvas.coords(item2)[0]))
#         mvbox(canvas, item1, 0, 80, speed=speed)
#         mvbox(canvas, item1, pos, speed=speed)
#         mvbox(canvas, item2, -1*pos, speed=speed)
#         mvbox(canvas, item1, -1, 80, speed=speed)
#         first_run = False
#     else:
#         if item1 > item2:
#             tmp = item1
#             item1 = item2
#             item2 = tmp
#         pos = -1*int(abs(canvas.coords(item1)[0] - canvas.coords(item2)[0]))
#         mvbox(item1, 0, 80, speed=speed)
#         mvbox(item1, pos, speed=speed)
#         mvbox(item2, -1*pos, speed=speed)
#         mvbox(item1, -1, 80, speed=speed)
#         first_run = True
#
#
# def center_window(root, width=300, height=200):
#     # get screen width and height
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#
#     # calculate position x and y coordinates
#     x = (screen_width / 2) - (width / 2)
#     y = (screen_height / 2) - (height / 2)
#     root.geometry('%dx%d+%d+%d' % (width, height, x, y))
#
#
# red_files = {
#     1: 'pngr\\1.png',
#     2: 'pngr\\2.png',
#     3: 'pngr\\3.png',
#     4: 'pngr\\4.png',
#     5: 'pngr\\5.png',
#     6: 'pngr\\6.png',
#     7: 'pngr\\7.png',
#     8: 'pngr\\8.png',
#     9: 'pngr\\9.png'
# }
# green_files = {
#     1: 'pngg\\1.png',
#     2: 'pngg\\2.png',
#     3: 'pngg\\3.png',
#     4: 'pngg\\4.png',
#     5: 'pngg\\5.png',
#     6: 'pngg\\6.png',
#     7: 'pngg\\7.png',
#     8: 'pngg\\8.png',
#     9: 'pngg\\9.png'
# }
# blue_files = {
#     1: 'pngb\\1.png',
#     2: 'pngb\\2.png',
#     3: 'pngb\\3.png',
#     4: 'pngb\\4.png',
#     5: 'pngb\\5.png',
#     6: 'pngb\\6.png',
#     7: 'pngb\\7.png',
#     8: 'pngb\\8.png',
#     9: 'pngb\\9.png'
# }
# yellow_files = {
#     1: 'pngy\\1.png',
#     2: 'pngy\\2.png',
#     3: 'pngy\\3.png',
#     4: 'pngy\\4.png',
#     5: 'pngy\\5.png',
#     6: 'pngy\\6.png',
#     7: 'pngy\\7.png',
#     8: 'pngy\\8.png',
#     9: 'pngy\\9.png'
# }
#
#
# boxes = {}
# images_blue = []
# images_red = []
# images_green = []
# images_yellow = []
#
#
# def make_boxes(canvas, order):
#     xpos = 20
#     for i in range(len(order)):
#         images_blue.append(tk.PhotoImage(file=blue_files[order[i]]))
#         images_red.append(tk.PhotoImage(file=red_files[order[i]]))
#         images_green.append(tk.PhotoImage(file=green_files[order[i]]))
#         images_yellow.append(tk.PhotoImage(file=yellow_files[order[i]]))
#
#     for i in range(len(order)):
#         boxes[i] = canvas.create_image(xpos, 2, image=images_blue[i], anchor=tk.NW)
#         xpos += 90
#
#
# def make_red(canvas, box, order):
#     img = images_red[box-1]
#     canvas.itemconfig(box, image=img)
#
#
# def make_green(canvas, box, order):
#     img = images_green[box-1]
#     canvas.itemconfig(box, image=img)
#
#
# def make_blue(canvas, box, order):
#     img = images_blue[box - 1]
#     canvas.itemconfig(box, image=img)
#
#
# def make_yellow(canvas, box, order):
#     img = images_yellow[box - 1]
#     canvas.itemconfig(box, image=img)
#
#
# def test_yellow(canvas, boxes, order):
#     for i in range(len(order)):
#         tksleep(0.5)
#         make_yellow(canvas, boxes[i], order)
#
# def dark_title_bar(root):
#     root.update()
#     set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
#     get_parent = ct.windll.user32.GetParent
#     hwnd = get_parent(root.winfo_id())
#     value = 2
#     value = ct.c_int(value)
#     set_window_attribute(hwnd, 20, ct.byref(value), 4)