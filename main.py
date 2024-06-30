from copy import deepcopy
import tkinter as tk
import ctypes as ct
from PIL import Image, ImageTk

order = [9, 5, 3, 2, 6, 1]
array = deepcopy(order)

# graph = {
#     1: [2, 3, 4],
#     2: [1, 3, 5],
#     3: [1, 2, 4, 5, 6],
#     4: [1, 3, 6],
#     5: [2, 3, 6],
#     6: [3, 4, 5]
# }

# graph = {}

red_files = {
    1: 'pngr\\1.png',
    2: 'pngr\\2.png',
    3: 'pngr\\3.png',
    4: 'pngr\\4.png',
    5: 'pngr\\5.png',
    6: 'pngr\\6.png',
    7: 'pngr\\7.png',
    8: 'pngr\\8.png',
    9: 'pngr\\9.png'
}
green_files = {
    1: 'pngg\\1.png',
    2: 'pngg\\2.png',
    3: 'pngg\\3.png',
    4: 'pngg\\4.png',
    5: 'pngg\\5.png',
    6: 'pngg\\6.png',
    7: 'pngg\\7.png',
    8: 'pngg\\8.png',
    9: 'pngg\\9.png'
}
blue_files = {
    1: 'pngb\\1.png',
    2: 'pngb\\2.png',
    3: 'pngb\\3.png',
    4: 'pngb\\4.png',
    5: 'pngb\\5.png',
    6: 'pngb\\6.png',
    7: 'pngb\\7.png',
    8: 'pngb\\8.png',
    9: 'pngb\\9.png'
}
yellow_files = {
    1: 'pngy\\1.png',
    2: 'pngy\\2.png',
    3: 'pngy\\3.png',
    4: 'pngy\\4.png',
    5: 'pngy\\5.png',
    6: 'pngy\\6.png',
    7: 'pngy\\7.png',
    8: 'pngy\\8.png',
    9: 'pngy\\9.png'
}


def tksleep(t):
    # emulating time.sleep(seconds)
    ms = int(t * 1000)
    win = tk._get_default_root('sleep')
    var = tk.IntVar(win)
    win.after(ms, var.set, 1)
    win.wait_variable(var)


class App(tk.Tk, ):
    def __init__(self):
        super().__init__()

        self.title("Визуализация на алгоритми")
        # self.center_window(980, 680)
        self.dark_title_bar()
        self.configure(bg="#47505f")
        self.state('zoomed')

        self.canvas = tk.Canvas(width=1030, height=1195, background="#47505f", highlightbackground='#47505f')
        self.canvas.place(x=250, y=50, anchor=tk.W)
        self.canvas.create_text(515, 850, text="Визуализация на алгоритми", font=('Inter Black', 30), fill='white', anchor=tk.CENTER)

        self.button = None

        self.menu = tk.Canvas(width=250, height=800, background="#707CC0", highlightbackground='#707CC0')
        self.menu.pack(side="left")

        self.img = Image.open('button.png')

        self.big_img = (ImageTk.PhotoImage(self.img.resize((240, 90))))
        self.small_img = (ImageTk.PhotoImage(self.img.resize((200, 90))))

        self.sorting_lbl = tk.Label(text='Sorting', compound='center', width=235, height=110, background="#707CC0", font=('Inter Black', 25), image=self.big_img, foreground='white')
        self.sorting_lbl.place(x=10, y=0)

        self.bb_sort = tk.Button(text='Bubble Sort', compound='center', width=200, height=80, background="#707CC0", command=lambda: Algorithms.Sorting.bubble_sort(self), borderwidth=0, overrelief='flat', font=('Inter Black', 17), image=self.small_img, foreground='white', activebackground='#707CC0')
        self.bb_sort.place(x=10, y=107)

        self.sel_sort = tk.Button(text='Selection Sort', compound='center', width=200, height=80, background="#707CC0", command=lambda: Algorithms.Sorting.selection_sort(self), borderwidth=0, relief='flat', font=('Inter Black', 17), image=self.small_img, foreground='white', activebackground='#707CC0')
        self.sel_sort.place(x=10, y=197)

        self.search_lbl = tk.Label(text='Search', compound='center', width=235, height=100, background="#707CC0", font=('Inter Black', 25), image=self.big_img, foreground='white')
        self.search_lbl.place(x=10, y=282)

        self.binary_search = tk.Button(text='Binary Search', compound='center', width=200, height=80, background="#707CC0", command=lambda: Algorithms.Search.binary_search(self), borderwidth=0, relief='flat', font=('Inter Black', 17), image=self.small_img, foreground='white', activebackground='#707CC0')
        self.binary_search.place(x=10, y=385)

        self.title = tk.Label(self, text='', background='#47505f', font=('Inter Black', 30), foreground='white')
        self.title.place(x=620, y=30)

        self.info = tk.Label(self, text='', background='#47505f', font=('Inter Black', 20), foreground='white', wraplength=720, justify="center")
        self.info.place(relx=0.6, y=500, anchor=tk.CENTER)

        self.running = False

        self.tk_array = {}

        # self.visited_bfs = []
        # self.queue_bfs = []

        # self.visited_dfs = None

        self.images_blue = []
        self.images_red = []
        self.images_green = []
        self.images_yellow = []

    def dark_title_bar(self):
        self.update()
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(self.winfo_id())
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, 20, ct.byref(value), 4)

    def make_array(self):
        self.canvas = tk.Canvas(width=1030, height=1195, background="#47505f", highlightbackground='#47505f')
        self.canvas.place(x=250, y=50, anchor=tk.W)
        self.info.tkraise(self.canvas)
        self.title.tkraise(self.canvas)

        for i in range(len(array)):
            self.images_blue.append(tk.PhotoImage(file=blue_files[array[i]]))
            self.images_red.append(tk.PhotoImage(file=red_files[array[i]]))
            self.images_green.append(tk.PhotoImage(file=green_files[array[i]]))
            self.images_yellow.append(tk.PhotoImage(file=yellow_files[array[i]]))

        xpos = 180

        for i in range(len(array)):
            self.tk_array[i] = self.canvas.create_image(xpos, 750, image=self.images_blue[i], anchor=tk.NW)
            xpos += 115

    # def make_graph(self):
    #     # self.canvas = tk.Canvas(width=650, height=650, background="#47505f", highlightbackground='#47505f')
    #     # self.canvas.place(relx=0.6, rely=0.3, anchor=tk.CENTER)
    #     # self.geometry('650x650')
    #     # self.center_window(650, 650)
    #
    #     #
    #     # self.button = tk.Button(self, text='', foreground='#99A1E5', background='#47505f', width=70)
    #     # self.button['font'] = self.font_style
    #     # self.button['text'] = 'BFS'
    #     # self.button['command'] = lambda: Algorithms.Graph.bfs(self)
    #     # self.button.pack(side='bottom')
    #     # order = list(graph.keys())
    #     nodes = [1, 2, 3, 4, 5, 6]
    #     for i in range(len(nodes)):
    #         self.images_blue.append(tk.PhotoImage(file=blue_files[nodes[i]]))
    #         self.images_red.append(tk.PhotoImage(file=red_files[nodes[i]]))
    #         self.images_green.append(tk.PhotoImage(file=green_files[nodes[i]]))
    #         self.images_yellow.append(tk.PhotoImage(file=yellow_files[nodes[i]]))
    #
    #     positions = {
    #         1: (20, 325),
    #         2: (200, 100),
    #         3: (200, 290),
    #         4: (200, 500),
    #         5: (380, 200),
    #         6: (380, 400),
    #     }
    #
    #     for i in range(6):
    #         self.canvas.create_image(positions[i+1], image=self.images_blue[i], anchor=tk.NW)
    #
    #     for i in range(1, 6):
    #         for x in graph[i]:
    #             self.canvas.lower(self.canvas.create_line(positions[i][0]+45, positions[i][1]+45, positions[x][0]+45, positions[x][1]+45, width=5, fill='white', smooth=True))

    def _mvbox(self, box, pos, y=0, speed=0.003):
        direction = 1
        if y != 0:
            if pos < 0:
                direction = -1
            for i in range(abs(y)):
                tksleep(speed)
                self.canvas.move(box, 0, direction * 1)
        else:
            if pos < 0:
                direction = -1
            for i in range(abs(pos)):
                tksleep(speed)
                self.canvas.move(box, direction * 1, 0)

    def swap(self, item1, item2, speed=0.003):
        pos = int(abs(self.canvas.coords(item1)[0] - self.canvas.coords(item2)[0]))
        self._mvbox(item1, 0, 100, speed=speed)
        self._mvbox(item1, pos, speed=speed)
        self._mvbox(item2, -1 * pos, speed=speed)
        self._mvbox(item1, -1, 100, speed=speed)

    def make_red(self, box):
        img = self.images_red[box - 1]
        self.canvas.itemconfig(box, image=img)

    def make_green(self, box):
        img = self.images_green[box - 1]
        self.canvas.itemconfig(box, image=img)

    def make_blue(self, box):
        img = self.images_blue[box - 1]
        self.canvas.itemconfig(box, image=img)

    def make_yellow(self, box):
        img = self.images_yellow[box - 1]
        self.canvas.itemconfig(box, image=img)


class Algorithms:
    class Sorting(App):
        def bubble_sort(self):
            while not self.running:
                self.running = True
                target = deepcopy(order)
                App.make_array(self)

                self.title['text'] = 'Bubble Sort'
                self.info['text'] = 'При Bubble Sort се сравняват два съседни елемента и при нужда се разменят. Така най-малкият елемент елемент "изплува" най-отпред.'

                tksleep(1)

                sorted_order = target.copy()
                sorted_order.sort()
                for x in range(len(target)):
                    for i in range(len(target) - 1):
                        self.make_yellow(self.tk_array[i])
                        self.make_yellow(self.tk_array[i + 1])
                        tksleep(1)
                        self.make_blue(self.tk_array[i])
                        self.make_blue(self.tk_array[i + 1])

                        if target[i] > target[i + 1]:
                            temp = target[i]
                            target[i] = target[i + 1]
                            target[i + 1] = temp

                            self.make_blue(self.tk_array[i])
                            self.make_blue(self.tk_array[i + 1])

                            self.make_red(self.tk_array[i])
                            self.make_red(self.tk_array[i + 1])

                            # tksleep(0.5)

                            self.swap(self.tk_array[i], self.tk_array[i + 1], 0.001)

                            tksleep(0.5)

                            self.make_blue(self.tk_array[i])
                            self.make_blue(self.tk_array[i + 1])

                            tmp = self.tk_array[i]
                            self.tk_array[i] = self.tk_array[i + 1]
                            self.tk_array[i + 1] = tmp

                        if target[-1] == sorted_order[-1]:
                            self.make_green(self.tk_array[len(target) - 1])
                        if target[i] == sorted_order[i]:
                            self.make_green(self.tk_array[i])
                    if target == sorted_order:
                        break
            self.running = False

        def selection_sort(self, speed=0.001, color=True):
            while not self.running:
                self.running = True
                target = deepcopy(order)
                App.make_array(self)
                self.title['text'] = 'Selection Sort'
                self.info['text'] = 'При Selection Sort се намира най-малкият \nелемент от масива и се поставя най-отпред.\n Това продължава докато масивът се подреди.'

                if speed > 0:
                    tksleep(1)
                for i in range(len(target)):
                    index_min = i
                    for j in range(i + 1, len(target)):
                        if target[j] < target[index_min]:
                            index_min = j

                    if self.tk_array[i] != self.tk_array[index_min]:
                        if color:
                            self.make_yellow(self.tk_array[index_min])
                        if speed != 0:
                            tksleep(1)
                        if color:
                            self.make_blue(self.tk_array[index_min])
                        self.swap(self.tk_array[i], self.tk_array[index_min], speed)

                    tmp = target[i]
                    target[i] = target[index_min]
                    target[index_min] = tmp

                    tmp = self.tk_array[i]
                    self.tk_array[i] = self.tk_array[index_min]
                    self.tk_array[index_min] = tmp
                    if color:
                        self.make_green(self.tk_array[i])
            self.running = False

    class Search(App):
        def binary_search(self, x=5, low=0, high=len(order)-1):
            target = deepcopy(order)
            Algorithms.Sorting.selection_sort(self, 0.0, False)
            self.title['text'] = 'Binary Search'
            self.info['text'] = 'Binary Search е алгоритъм за намиране на позицията на даден елемент в сортиран масив чрез намаляване на претърсваното пространство на половина.'

            while low <= high:
                mid = low + (high - low) // 2
                self.make_yellow(self.tk_array[mid])
                tksleep(0.5)
                # self.make_blue(self.tk_array[mid])
                if order[mid] == x:
                    return mid
                elif order[mid] < x:
                    tksleep(0.5)
                    for i in range(order[mid]):
                        self.make_red(self.tk_array[i])
                    low = mid + 1
                else:
                    tksleep(0.5)
                    for i in range(order[mid]-2, len(order)):
                        self.make_red(self.tk_array[i])
                    high = mid - 1
            self.make_green(self.tk_array[mid])
            return -1

    # class Graph(App):
    #     def bfs(self, node=1):
    #         App.make_graph(self)
    #         tksleep(1)
    #         self.visited_bfs.append(node)
    #         self.queue_bfs.append(node)
    #
    #         while self.queue_bfs:  # Creating loop to visit each node
    #             m = self.queue_bfs.pop(0)
    #             tksleep(0.5)
    #             self.make_green(m)
    #             print(m, end=" ")
    #
    #             for neighbour in graph[m]:
    #                 if neighbour not in self.visited_bfs:
    #                     self.visited_bfs.append(neighbour)
    #                     self.queue_bfs.append(neighbour)


if __name__ == '__main__':
    root = App()
    # App.make_array(root)
    # App.make_graph(root)
    root.mainloop()
