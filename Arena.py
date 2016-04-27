from Tkinter import *
from PIL import Image, ImageTk
from math import sin, cos, pi
from Vector import *
from Color import *
class Arena(Frame):
    """This class provides the user interface for an arena of turtles."""
    cat = None
    def __init__(self, parent, cat,width=900, height=750, **options):
        Frame.__init__(self, parent, **options)
        self.width, self.height = width, height
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()
        self.time = StringVar()
        self.cat_r = StringVar()
        self.cat_degree = StringVar()
        self.mouse_degree = StringVar()
        self.var = IntVar()
        Arena.cat = cat
        parent.title("UC Bereley CS9H Turtle Arena")
        Button(self, text='step', command=self.step).pack(side=LEFT)
        Button(self, text='run', command=self.run).pack(side=LEFT)
        Button(self, text='stop', command=self.stop).pack(side=LEFT)
        Button(self, text='quit', command=parent.quit).pack(side=LEFT)
        Button(self, text='rest', command=self.reset).pack(side=LEFT)
        Label(self, textvariable = self.time, width= 15).pack(side = RIGHT)
        Label(self, textvariable = self.cat_r, width= 15).pack(side = RIGHT)
        Label(self, textvariable = self.cat_degree, width=15).pack(side = RIGHT)
        Label(self, textvariable = self.mouse_degree, width=15).pack(side = RIGHT)
        Radiobutton(self, text="Clockwise Mouse", variable=self.var, value=1, command=self.mouse_direction).pack(anchor=W)
        menubar = Menu(parent)
        parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="About...", command=self.about)
        fileMenu.add_command(label="Quit", command=parent.quit)

        self.turtles = []
        self.start_turtles =[]
        self.items = {}
        self.running = 0
        self.time_in_int = 0
        self.period = 45
        self.canvas.bind('<ButtonPress>', self.press)
        self.canvas.bind('<Motion>', self.motion)
        self.canvas.bind('<ButtonRelease>', self.release)
        self.dragging = None
        self.time.set('Time: '+ str((self.time_in_int/60))+':' + str(self.time_in_int % 60))
        self.cat_r.set('CatRadius: '+ str(Arena.cat.distance_to_r()))
        self.cat_degree.set('CatAngle: ' + str(Arena.cat.degree))
        self.mouse_degree.set('MouseAngle:' + str(Arena.cat.Mouse.degree))

    def mouse_direction(self):
        '''
        The commond of radiobutton, used for changes the mouse's direction
        :return:
        '''
        for i in self.turtles:
            if i == self.cat.Mouse:
                i.angle = -i.angle
                if i.angle > 0:
                    self.var.set(0)
                else:
                    self.var.set(1)

        #self.cat.Mouse.degree = -self.cat.Mouse.degree



    def about(self):
        '''
        :return: display the about window
        '''
        newFrame = Toplevel()
        newFrame.geometry("600x450")
        newFrame.title("UC Berkeley CS9H Turtle Arena About")
        handler = lambda: newFrame.destroy()
        Label(newFrame, text="Name: Xiaoyu Zheng").pack()
        Label(newFrame, text="Project 5").pack()
        image = Image.open("1.jpg").resize((200, 250))
        photo = ImageTk.PhotoImage(image)
        photo_label = Label(newFrame, image=photo)
        photo_label.image = photo
        photo_label.pack()
        Button(newFrame, text="OK", command=handler).pack()


    def reset(self):
        '''
        :return: resst the simulation
        '''
        self.stop()
        for i in range(len(self.turtles)):
            self.turtles[i].position = self.start_turtles[i]
        self.time_in_int = 0
        self.time.set('time: ' + str((self.time_in_int / 60))+':' + str(self.time_in_int % 60))
        for i in self.turtles:
            self.update(i)

    def press(self, event):
        '''
        check if the mouse drags
        '''
        dragstart = Vector(event.x, event.y)
        for turtle in self.turtles:
            if (dragstart - turtle.position).length() < 10 and turtle == self.cat:
                self.dragging = turtle
                self.dragstart = dragstart
                self.start = turtle.position
                return

    def motion(self, event):
        '''
        make the dragged cat move
        '''
        drag = Vector(event.x, event.y)

        if self.dragging and self.cat.Mouse.dead:
            self.dragging.position = self.start + drag - self.dragstart
            self.update(self.dragging)
            #self.step()



    def release(self, event):
        '''
        make the self.dragging none if the mouse don't drag 
        '''
        self.dragging = None

    def update(self, turtle):
        """Update the drawing of a turtle according to the turtle object."""
        item = self.items[turtle]
        vertices = [(v.x, v.y) for v in turtle.getshape()]

        self.canvas.coords(item, sum(vertices, ()))
        if self.dragging == turtle:
            style = {'width': 1, 'outline': Color(0.000000, 0.000000, 0.000000), 'fill': Color(0.000000, 0.000000, 0.000000)}
            self.canvas.itemconfigure(item, **style)
        else:
            self.canvas.itemconfigure(item, **turtle.style)




    def add(self, turtle):
        """Add a new turtle to this arena."""

        self.start_turtles.append(turtle.position)
        self.turtles.append(turtle)
        self.items[turtle] = self.canvas.create_polygon(0, 0)
        self.update(turtle)


    def step(self, stop=1):
        """Advance all the turtles one step."""
        nextstates = {}
        if stop:
            self.running = 0
        for turtle in self.turtles:
            nextstates[turtle] = turtle.getnextstate()
        for turtle in self.turtles:
            turtle.setstate(nextstates[turtle])
            self.update(turtle)
        self.cat_r.set('CatRadius: '+ str(round(Arena.cat.distance_to_r()/100, 3)))
        self.cat_degree.set('CatAngle: ' + str(round(Arena.cat.degree, 1)))
        self.mouse_degree.set('MouseAngle:' + str(round(Arena.cat.Mouse.degree, 1)))
        self.time.set('time: ' + str((self.time_in_int / 60))+':' + str(self.time_in_int % 60))
        self.time_in_int += 1



    def run(self):
        """Start the turtles running."""
        if self.running == 1:
            self.running = 0
        else:
            self.running = 1
            self.loop()

    def loop(self):
        """Repeatedly advance all the turtles one step."""
        self.step(0)

        if self.running:
            self.tk.createtimerhandler(self.period, self.loop)

    def stop(self):
        """Stop the running turtles."""
        self.running = 0
