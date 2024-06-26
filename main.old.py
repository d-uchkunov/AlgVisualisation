# from helper import *
# import tkinter as tk
# import random
# import tkinter.font as font

# order = random.sample(list(blue_files.keys()), k=6)
# order = [9, 8, 1, 6, 5, 4]
# order = [1, 4, 5, 6, 8, 9]
# order = [1, 2, 3, 4, 6, 5]


# def bubble_sort():
#     global order
#     sorted_order = order.copy()
#     sorted_order.sort()
#     for x in range(len(order)):
#         for i in range(len(order)-1):
#             make_yellow(canvas, boxes[i], order)
#             make_yellow(canvas, boxes[i+1], order)
#             tksleep(1)
#             make_blue(canvas, boxes[i], order)
#             make_blue(canvas, boxes[i+1], order)
#
#             if order[i] > order[i+1]:
#                 temp = order[i]
#                 order[i] = order[i+1]
#                 order[i+1] = temp
#
#                 make_blue(canvas, boxes[i], order)
#                 make_blue(canvas, boxes[i+1], order)
#
#                 make_red(canvas, boxes[i], order)
#                 make_red(canvas, boxes[i+1], order)
#
#                 # tksleep(0.5)
#
#                 swap(canvas, boxes[i], boxes[i+1], 0.001)
#
#                 tksleep(0.5)
#
#                 make_blue(canvas, boxes[i], order)
#                 make_blue(canvas, boxes[i+1], order)
#
#                 tmp = boxes[i]
#                 boxes[i] = boxes[i+1]
#                 boxes[i+1] = tmp
#
#             if order[-1] == sorted_order[-1]:
#                 make_green(canvas, boxes[len(order)-1], order)
#             if order[i] == sorted_order[i]:
#                 make_green(canvas, boxes[i], order)
#         if order == sorted_order:
#             break


def selection_sort(speed=0.001, color=True):
    for i in range(len(order)):
        index_min = i
        for j in range(i+1, len(order)):
            if order[j] < order[index_min]:
                index_min = j

        if boxes[i] != boxes[index_min]:
            if color:
                make_yellow(canvas, boxes[index_min], order)
            if speed != 0:
                tksleep(1)
            if color:
                make_blue(canvas, boxes[index_min], order)
            swap(canvas, boxes[i], boxes[index_min], speed)

        tmp = order[i]
        order[i] = order[index_min]
        order[index_min] = tmp

        tmp = boxes[i]
        boxes[i] = boxes[index_min]
        boxes[index_min] = tmp
        if color:
            make_green(canvas, boxes[i], order)


# def binary_search(number, low=0, high=len(order)):
#     # Check base case
#     if high >= low:
#
#         mid = low + (high - low) // 2
#
#         if order[mid] == number:
#             tksleep(0.5)
#             make_green(canvas, boxes[mid], order)
#             print(mid)
#             return mid
#
#         elif order[mid] > number:
#             tksleep(0.5)
#             for i in range(mid, len(order)):
#                 tksleep(0.2)
#                 make_red(canvas, boxes[i], order)
#             return binary_search(number, low, mid - 1)
#
#         else:
#             tksleep(0.5)
#             for i in range(high-1):
#                 make_red(canvas, boxes[i], order)
#             return binary_search(number, mid + 1, high)
#     # Element is not present in the array
#     else:
#         return -1
#
#
# root = tk.Tk()
#
#
# center_window(root, 650, 250)
# dark_title_bar(root)
#
# root.title('BubbleSort')
# root.configure(bg="#343C4A")
# font_style = font.Font(family='Helvetica', size=20, weight="bold")
#
# canvas = tk.Canvas(width=650, height=176, background="#343C4A",highlightbackground='#343C4A')
# canvas.place(relx=0.55, rely=0.4, anchor=tk.CENTER)
# # canvas.pack(side='left')
#
# make_boxes(canvas, order)
#
#
# # btn = tk.Button(root, text='SORT', command=lambda: test_yellow(canvas, boxes, order), foreground='#99A1E5', background='#343C4A', width=70)
# # btn = tk.Button(root, text='SORT', command=bubble_sort, foreground='#99A1E5', background='#343C4A', width=70)
# # btn = tk.Button(root, text='SORT', command=selection_sort, foreground='#99A1E5', background='#343C4A', width=70)
# selection_sort(0, False)
# btn = tk.Button(root, text='SORT', command=lambda: binary_search(6), foreground='#99A1E5', background='#343C4A', width=70)
# btn['font'] = font_style
# btn.pack(side='bottom')
#
#
# root.mainloop()
