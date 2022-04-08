from tkinter import Canvas, Tk

class Ui:
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry('600x600')
    
        self.canvas = Canvas(self.screen, width = 600, height = 600, bg = "white")
        self.canvas.pack()

    def __call__(self):

        prev_cords = [0, 0]

        def move_mouse(event):
            nonlocal self, prev_cords
            
            # if first line cross second line, first line will be red, green otherwise
            if line_cross([[event.x, event.y], [event.x - 30, event.y + 60]], [[500, 125], [107, 160]]):
                self.canvas.create_line(event.x, event.y, event.x - 30, event.y + 60, fill = "red")
            else:
                self.canvas.create_line(event.x, event.y, event.x - 30, event.y + 60, fill = "green")
            
            self.canvas.create_line(prev_cords[0], prev_cords[1], prev_cords[0] - 30, prev_cords[1] + 60, fill = "white")
            self.canvas.create_line(500, 125, 107, 160, fill = "blue")
            prev_cords = [event.x, event.y]
            
        self.screen.bind("<Motion>", move_mouse)
        self.screen.mainloop()

def isBetween(a : list, b : list, c : list) -> bool:
    EPS = 0.001
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])
    if abs(crossproduct) >= EPS: return False
    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1]) * (b[1] - a[1])
    if dotproduct < 0: return False
    sqr_ba = (b[0] - a[0]) ** 2 + (b[1] - a[1])**2
    if dotproduct > sqr_ba: return False
    return True

def line_cross(cords1 : list, cords2 : list) -> bool:
    """ 
    This function determines, whether line with cords1 and line with cords2 cross each other
    cords1 : this is tuple with two lists, first list is start x,y cords, second list is end x,y cords
    
    """

    x1_1 = cords1[0][0]
    y1_1 = cords1[0][1]
    x1_2 = cords1[1][0]
    y1_2 = cords1[1][1]

    x2_1 = cords2[0][0]
    y2_1 = cords2[0][1]
    x2_2 = cords2[1][0]
    y2_2 = cords2[1][1]

    # find a1, a2, b1, b2 using Lagrange interpolation

    a1 = (y1_1 / (x1_1 - x1_2) + y1_2 / (x1_2 - x1_1))
    b1 = - (y1_1 / (x1_1 - x1_2)) * x1_2 - (y1_2 / (x1_2 - x1_1)) * x1_1

    a2 = y2_1 / (x2_1 - x2_2) + y2_2 / (x2_2 - x2_1)
    b2 = - (y2_1 / (x2_1 - x2_2)) * x2_2 - (y2_2 / (x2_2 - x2_1)) * x2_1

    # find (x, y) cross point, using Gauss method (used easy formulas)

    X = (b2 - b1) / (-a2 - (-a1))
    Y = b1 + (a1) * X

    if isBetween([x1_1, y1_1], [x1_2, y1_2], [X, Y]) and isBetween([x2_1, y2_1], [x2_2, y2_2], [X, Y]): return True
    return False

ui = Ui()
ui()