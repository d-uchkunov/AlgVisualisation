import random
import tkinter as tk
import ctypes as ct
import tkinter.font as font

array = [1, 6, 5, 4, 9, 8]
graph = {
    1: [2, 3, 4],
    2: [1, 3, 5],
    3: [1, 2, 4, 5, 6],
    4: [1, 3, 6],
    5: [2, 3, 6],
    6: [3, 4, 5]
}

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


# class RoundedButton(tk.Canvas):
#     def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None, text=''):
#         tk.Canvas.__init__(self, parent, borderwidth=0,
#             relief="flat", highlightthickness=0, bg=bg)
#         self.command = command
#         self.text = text
#
#         if cornerradius > 0.5*width:
#             print("Error: cornerradius is greater than width.")
#             return None
#
#         if cornerradius > 0.5*height:
#             print("Error: cornerradius is greater than height.")
#             return None
#
#         rad = 2*cornerradius
#         def shape():
#             # self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline='white', width=5)
#             # self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
#             # self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
#             # self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
#             # self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)
#             self.create_rectangle((0,height, width, 0), fill=color, )
#             self.create_text(width/2, height/2, text=self.text, anchor=tk.CENTER, font=("Helvetica 15 bold"), fill='#40396E')
#
#         id = shape()
#         (x0,y0,x1,y1)  = self.bbox("all")
#         width = (x1-x0)
#         height = (y1-y0)
#         self.configure(width=width, height=height)
#         self.bind("<ButtonPress-1>", self._on_press)
#         self.bind("<ButtonRelease-1>", self._on_release)
#
#     def _on_press(self, event):
#         self.configure(relief="sunken")
#
#     def _on_release(self, event):
#         self.configure(relief="raised")
#         if self.command is not None:
#             self.command()


class App(tk.Tk, ):
    def __init__(self):
        super().__init__()

        self.title("Визуализация на алгоритми")
        self.center_window(980, 680)
        self.dark_title_bar()
        self.configure(bg="#343C4A")

        self.canvas = tk.Canvas(width=650, height=650, background="#343C4A", highlightbackground='#343C4A')
        self.canvas.create_text(230, 400, text="                   Визуализация на алгоритми", font='Inter 30 bold', fill='#9AA2E6')
        self.canvas.place(relx=0.3, rely=0.4, anchor=tk.W)
        self.button = None

        self.menu = tk.Canvas(width=250, height=680, background="#4d5666", highlightbackground='#4d5666')
        self.menu.pack(side="left")

        self.sorting_lbl = tk.Label(text='Sorting', width=19, height=2, background="#6c74b9", font='Inter 14 bold')
        self.sorting_lbl.place(x=10, y=10)

        self.bb_sort = tk.Button(text='Bubble Sort', width=17, height=2, background="#9AA2E6", command=lambda: Algorithms.Sorting.bubble_sort(self), borderwidth=0, relief='flat', font='Inter 14 bold')
        self.bb_sort.place(x=10, y=80)

        self.sel_sort = tk.Button(text='Selection Sort', width=17, height=2, background="#6c74b9", command=lambda: Algorithms.Sorting.selection_sort(self), borderwidth=0, relief='flat', font='Inter 14 bold')
        self.sel_sort.place(x=10, y=150)

        self.sel_sort = tk.Button(text='Quick Sort', width=17, height=2, background="#5961a4", borderwidth=0, relief='flat', font='Inter 14 bold')
        self.sel_sort.place(x=10, y=220)

        self.sorting_lbl = tk.Label(text='Graphs', width=19, height=2, background="#7b88de", font='Inter 14 bold')
        self.sorting_lbl.place(x=10, y=300)

        self.sel_sort = tk.Button(text='BFS', width=17, height=2, background="#444a87", borderwidth=0, relief='flat', font='Inter 14 bold', command=lambda : Algorithms.Graph.bfs(self))
        self.sel_sort.place(x=10, y=370)

        self.font_style = font.Font(family='Inter', size=20, weight="bold")

        self.tk_array = {}

        self.visited_bfs = []
        self.queue_bfs = []

        self.visited_dfs = None

        self.images_blue = []
        self.images_red = []
        self.images_green = []
        self.images_yellow = []

    def center_window(self, width=300, height=200):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def dark_title_bar(self):
        self.update()
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(self.winfo_id())
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, 20, ct.byref(value), 4)

    def make_array(self):
        self.canvas.delete('all')
        self.canvas = tk.Canvas(width=650, height=176, background="#343C4A", highlightbackground='#343C4A')
        self.canvas.place(relx=0.6, rely=0.3, anchor=tk.CENTER)

        for i in range(len(array)):
            self.images_blue.append(tk.PhotoImage(file=blue_files[array[i]]))
            self.images_red.append(tk.PhotoImage(file=red_files[array[i]]))
            self.images_green.append(tk.PhotoImage(file=green_files[array[i]]))
            self.images_yellow.append(tk.PhotoImage(file=yellow_files[array[i]]))

        xpos = 20

        for i in range(len(array)):
            self.tk_array[i] = self.canvas.create_image(xpos, 2, image=self.images_blue[i], anchor=tk.NW)
            xpos += 90

    def make_graph(self):
        # self.geometry('650x650')
        # self.center_window(650, 650)
        self.canvas = tk.Canvas(width=650, height=650, background="#343C4A", highlightbackground='#343C4A')
        self.canvas.place(relx=0.67, rely=0.4, anchor=tk.CENTER)
        #
        # self.button = tk.Button(self, text='', foreground='#99A1E5', background='#343C4A', width=70)
        # self.button['font'] = self.font_style
        # self.button['text'] = 'BFS'
        # self.button['command'] = lambda: Algorithms.Graph.bfs(self)
        # self.button.pack(side='bottom')
        # order = list(graph.keys())
        nodes = [1, 2, 3, 4, 5, 6]
        for i in range(len(nodes)):
            self.images_blue.append(tk.PhotoImage(file=blue_files[nodes[i]]))
            self.images_red.append(tk.PhotoImage(file=red_files[nodes[i]]))
            self.images_green.append(tk.PhotoImage(file=green_files[nodes[i]]))
            self.images_yellow.append(tk.PhotoImage(file=yellow_files[nodes[i]]))

        positions = {
            1: (20, 325),
            2: (200, 100),
            3: (200, 290),
            4: (200, 500),
            5: (380, 200),
            6: (380, 400),
        }

        for i in range(6):
            self.canvas.create_image(positions[i+1], image=self.images_blue[i], anchor=tk.NW)

        for i in range(1, 6):
            for x in graph[i]:
                self.canvas.lower(self.canvas.create_line(positions[i][0]+45, positions[i][1]+45, positions[x][0]+45, positions[x][1]+45, width=5, fill='white', smooth=True))

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
        self._mvbox(item1, 0, 80, speed=speed)
        self._mvbox(item1, pos, speed=speed)
        self._mvbox(item2, -1 * pos, speed=speed)
        self._mvbox(item1, -1, 80, speed=speed)

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
            global lbl, array, info
            self.canvas['height'] = 176
            array = [4, 6, 8, 2, 1, 5]
            App.make_array(self)
            lbl['text'] = 'Bubble Sort'
            info['text'] = 'При Bubble Sort се сравняват два съседни елемента \nи при нужда се разменят. Така най-малкият елемент\nелемент "изплува" най-отпред.'
            tksleep(1)

            sorted_order = array.copy()
            sorted_order.sort()
            for x in range(len(array)):
                for i in range(len(array) - 1):
                    self.make_yellow(self.tk_array[i])
                    self.make_yellow(self.tk_array[i + 1])
                    tksleep(1)
                    self.make_blue(self.tk_array[i])
                    self.make_blue(self.tk_array[i + 1])

                    if array[i] > array[i + 1]:
                        temp = array[i]
                        array[i] = array[i + 1]
                        array[i + 1] = temp

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

                    if array[-1] == sorted_order[-1]:
                        self.make_green(self.tk_array[len(array) - 1])
                    if array[i] == sorted_order[i]:
                        self.make_green(self.tk_array[i])
                if array == sorted_order:
                    break

        def selection_sort(self, speed=0.001, color=True):
            global lbl, array
            array = [4, 6, 8, 2, 1, 5]
            App.make_array(self)
            lbl['text'] = 'Selection Sort'
            info['text'] = 'При Selection Sort се намира най-малкият \nелемент от масива и се поставя най-отпред.\n Това продължава докато масивът се подреди.'
            tksleep(1)
            for i in range(len(array)):
                index_min = i
                for j in range(i + 1, len(array)):
                    if array[j] < array[index_min]:
                        index_min = j

                if self.tk_array[i] != self.tk_array[index_min]:
                    if color:
                        self.make_yellow(self.tk_array[index_min])
                    if speed != 0:
                        tksleep(1)
                    if color:
                        self.make_blue(self.tk_array[index_min])
                    self.swap(self.tk_array[i], self.tk_array[index_min], speed)

                tmp = array[i]
                array[i] = array[index_min]
                array[index_min] = tmp

                tmp = self.tk_array[i]
                self.tk_array[i] = self.tk_array[index_min]
                self.tk_array[index_min] = tmp
                if color:
                    self.make_green(self.tk_array[i])

        def partition(self, low, high):
            pivot = array[high]
            self.make_red(pivot)
            i = low - 1
            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])
            (array[i + 1], array[high]) = (array[high], array[i + 1])
            return i + 1

        def quickSort(self, low, high):
            if low < high:
                pi = Algorithms.Sorting.partition(self, low, high)
                Algorithms.Sorting.quickSort(self, low, pi - 1)
                Algorithms.Sorting.quickSort(self, pi + 1, high)

    class Graph(App):
        def bfs(self, node=1):
            App.make_graph(self)
            tksleep(1)
            self.visited_bfs.append(node)
            self.queue_bfs.append(node)

            while self.queue_bfs:  # Creating loop to visit each node
                m = self.queue_bfs.pop(0)
                tksleep(0.5)
                self.make_green(m)
                print(m, end=" ")

                for neighbour in graph[m]:
                    if neighbour not in self.visited_bfs:
                        self.visited_bfs.append(neighbour)
                        self.queue_bfs.append(neighbour)


if __name__ == '__main__':
    root = App()

    lbl = tk.Label(root, text="", background='#343C4A', font='Inter 20 bold', foreground='#9aa2e6')
    lbl.place(relx=0.5, y=30)

    info = tk.Label(root, width=50, height=10, text='', background='#343C4A', font='Inter 20 bold', foreground='#9aa2e6')
    info.place(x=300, y=300)
    # App.make_array(root)
    # App.make_graph(root)

    root.mainloop()
