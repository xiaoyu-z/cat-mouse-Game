__author__ = 'zhengxiaoyu'
from Tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from Turtle  import Turtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector
from Mouse import *
from WalkingTurtle import *
from Status import *
from Cat import *
little_mouse = Mouse(Vector(345,350), 1, 1)
little_cat = Cat(Vector(800,350), 1 ,little_mouse)
little_status = Status(Vector(450,350), 1)
tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk, little_cat)                      # Create an Arena widget, arena
arena.pack()
arena.add(little_mouse)
arena.add(little_cat)
arena.add(little_status)
tk.mainloop()                          # Enter the Tkinter event loop