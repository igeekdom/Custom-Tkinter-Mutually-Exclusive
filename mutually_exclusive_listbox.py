from tkinter import *
import tkinter.ttk as ttk

class ScrolledListbox(Frame):

  def __init__(self, parent, *args, **kwargs):
    Frame.__init__(self, parent)
    self.listbox = Listbox(self, *args, **kwargs)
    self.listbox_scrollbar = Scrollbar(self, orient="vertical", command=self.listbox.yview)
    self.listbox.configure(yscrollcommand=self.listbox_scrollbar.set)
    self.listbox_scrollbar.pack(side="right", fill="y")
    self.listbox.pack(side="left", fill="both", expand=True)
    self.listbox.bind('<Enter>', self.enter)
    self.listbox.bind('<Leave>', self.leave)

  def configure(self, **kwargs):
    self.listvariable(kwargs.get('listvariable',None))
    self.setbackground(kwargs.get('bg',None))
    self.setforeground(kwargs.get('fg',None))
    self.sethighlight(kwargs.get('highlightcolor',None))
    self.setselectbackground(kwargs.get('selectbackground',None))
    self.setexportselection(kwargs.get('exportselection',1))
      
  def listvariable(self, item_list):
    if item_list != None:
      for item in item_list:
        self.listbox.insert(END, item)

  def setexportselection(self, exportselection):
    self.listbox.configure(exportselection = exportselection)

  def setbackground(self, bg):
    if bg != None:
      self.listbox.configure(bg = bg)
      
  def setforeground(self, fg):
    if fg != None:
      self.listbox.configure(fg = fg)
          
  def sethighlight(self, highlightcolor):
    if highlightcolor != None:
      self.listbox.configure(highlightcolor = highlightcolor)

  def setselectbackground(self, selectbackground):
    if selectbackground != None:
      self.listbox.configure(selectbackground = selectbackground)

  def enter(self, event):
    self.listbox.config(cursor="hand2")

  def leave(self, event):
    self.listbox.config(cursor="")

  def insert(self, location, item):
    self.listbox.insert(location, item)

  def curselection(self):
    return self.listbox.curselection()
      
  def get(self, i):
    return self.listbox.get(i)
  
  def size(self):
    return self.listbox.size()
  
  def delete(self, first, last=None):
    self.listbox.delete(first, last)

  def delete_selected(self):
    selected_item = self.listbox.curselection()
    idx_count = 0
    for item in selected_item:
      self.listbox.delete(item - idx_count)
      idx_count += 1

  def delete_unselected(self):
    selected_item = self.listbox.curselection()
    idx_count = 0
    for i, listbox_entry in enumerate(self.listbox.get(0, END)):
      if not listbox_entry in selected_item:
        self.listbox.delete(i - idx_count)
        idx_count += 1

class Mutually_Exlusive_left_listbox(Frame):

  def __init__(self, parent, *args, **kwargs):
    Frame.__init__(self, parent)
    self.parent = parent 
    self.frame = f = Frame(parent, width=200, height=80, borderwidth=2)
    f.place(x=2, y=2)
    self.left_listbox = ScrolledListbox(self.frame, selectmode=MULTIPLE)
    self.left_listbox.configure(listvariable=[])
    self.left_listbox.pack(side="left", fill="both", expand=True)    
    blank_label = Label(self.frame, text="         ")
    blank_label.pack(padx=5, pady=20, side=LEFT, anchor=CENTER) 
    self.all_left_move = Label(self.frame, text=">>", bg="dim gray", fg="white")
    self.all_left_move.bind("<Button-1>",self.move_all_right)
    self.left_move = Label(self.frame, text=">", bg="dim gray", fg="white")
    self.left_move.bind("<Button-1>",self.move_right_move)
    self.right_move = Label(self.frame, text="<", bg="dim gray", fg="white")
    self.right_move.bind("<Button-1>",self.move_left_move)
    self.all_right_move = Label(self.frame, text="<<", bg="dim gray", fg="white")
    self.all_right_move.bind("<Button-1>",self.move_all_left)
    self.right_listbox = ScrolledListbox(self.frame, selectmode=MULTIPLE)
    self.right_listbox.pack(side="left", fill="both", expand=True)
    self.frame.bind("<Configure>", lambda event:self.OnResize(event, self.all_left_move, self.left_move, self.right_move, self.all_right_move))

  def configure(self, **kwargs):
    self.left_listvariable(kwargs.get('left_listvariable',None))   
    self.left_setbackground(kwargs.get('left_bg',None))
    self.left_setforeground(kwargs.get('left_fg',None))
    self.left_sethighlight(kwargs.get('left_highlightcolor',None))
    self.left_setselectbackground(kwargs.get('left_selectbackground',None))

    self.right_listvariable(kwargs.get('right_listvariable',None))
    self.right_setbackground(kwargs.get('right_bg',None))
    self.right_setforeground(kwargs.get('right_fg',None))
    self.right_sethighlight(kwargs.get('right_highlightcolor',None))
    self.right_setselectbackground(kwargs.get('right_selectbackground',None))

    self.nav_button_setbackground(kwargs.get('nav_button_bg',None))
    self.nav_button_setforeground(kwargs.get('nav_button_fg',None))

  def left_listvariable(self, item_list):
    self.left_listbox.configure(listvariable=item_list)

  def left_setbackground(self, bg):
    self.left_listbox.configure(bg = bg)
  
  def left_setforeground(self, fg):
    if fg != None:
      self.left_listbox.configure(fg = fg)
          
  def left_sethighlight(self, highlightcolor):
    if highlightcolor != None:
      self.left_listbox.configure(highlightcolor = highlightcolor)

  def left_setselectbackground(self, selectbackground):
    if selectbackground != None:
      self.left_listbox.configure(selectbackground = selectbackground)
    
  def right_listvariable(self, item_list):
    self.right_listbox.configure(listvariable=item_list)

  def right_setbackground(self, bg):
    self.right_listbox.configure(bg = bg)

  def right_setforeground(self, fg):
    if fg != None:
      self.right_listbox.configure(fg = fg)
          
  def right_sethighlight(self, highlightcolor):
    if highlightcolor != None:
      self.right_listbox.configure(highlightcolor = highlightcolor)

  def right_setselectbackground(self, selectbackground):
    if selectbackground != None:
      self.right_listbox.configure(selectbackground = selectbackground)

  def nav_button_setbackground(self, bg):
    self.all_left_move.config(bg = bg)
    self.left_move.config(bg = bg)
    self.right_move.config(bg = bg)
    self.all_right_move.config(bg = bg)

  def nav_button_setforeground(self, fg):
    self.all_left_move.config(fg = fg)
    self.left_move.config(fg = fg)
    self.right_move.config(fg = fg)
    self.all_right_move.config(fg = fg)
  
  def place(self, x, **kwargs):
    if len(kwargs) > 0:
      y = kwargs.get('y')
      height =  kwargs.get('height')
      width =  kwargs.get('width')
      if width <= 400:
        self.frame.place(x=x,y=y,width=400,height=height)
      else:
        self.frame.place(x=x,y=y,width=width,height=height)

  def OnResize(self, event, all_left_move, left_move, right_move, all_right_move):
    #print ('Onsize')
    #print (event.width)
    #print (event.height)
    if event.width <= 400:
      all_left_move.place(x=185, y=50)
      left_move.place(x=187, y=75)
      right_move.place(x=187, y=100)
      all_right_move.place(x=185, y=125)
    else:
      new_loc = (event.width - 400) / 2
      all_left_move.place(x=185 + new_loc, y=50)
      left_move.place(x=187 + new_loc, y=75)
      right_move.place(x=187 + new_loc, y=100)
      all_right_move.place(x=185 + new_loc, y=125)
      
  def move_all_right(self, event):
    r_size = self.right_listbox.size()
    for i in range(self.left_listbox.size()):
      self.right_listbox.insert(r_size + 1, self.left_listbox.get(i))
      r_size += 1
    self.left_listbox.delete(0, self.left_listbox.size())

  def move_right_move(self, event):
    r_size = self.right_listbox.size()
    for i in self.left_listbox.curselection():
        self.right_listbox.insert(r_size + 1, self.left_listbox.get(i))
        r_size += 1
    self.left_listbox.delete_selected()

  def move_all_left(self, event):
    r_size = self.left_listbox.size()
    for i in range(self.right_listbox.size()):
      self.left_listbox.insert(r_size + 1, self.right_listbox.get(i))
      r_size += 1
    self.right_listbox.delete(0, self.right_listbox.size())

  def move_left_move(self, event):
    r_size = self.left_listbox.size()
    for i in self.right_listbox.curselection():
        self.left_listbox.insert(r_size + 1, self.right_listbox.get(i))
        r_size += 1
    self.right_listbox.delete_selected()


if __name__ == '__main__':
    
    gui = Tk()
    list_values = ['Test1','Test2','Test3','Test4','Test5','Test6','Test7']
    list_values2 = ['Test8','Test9','Test10','Test11','Test12','Test13','Test14']
    mutual_listbox = Mutually_Exlusive_left_listbox(gui, selectmode=MULTIPLE)
    #scrolled_left_listbox2 = Mutually_Exlusive_left_listbox(gui, selectmode=MULTIPLE)
    #scrolled_left_listbox3 = Mutually_Exlusive_left_listbox(gui, selectmode=MULTIPLE)
    mutual_listbox.configure(left_listvariable=list_values)
    mutual_listbox.configure(right_listvariable=list_values2)
    #mutual_listbox.configure(left_bg='yellow')
    #mutual_listbox.configure(right_bg='yellow')
    #mutual_listbox.configure(left_selectbackground='red')
    #utual_listbox.configure(right_selectbackground='green')
    #mutual_listbox.configure(nav_button_bg='blue')
    #mutual_listbox.configure(nav_button_fg='red')
    mutual_listbox.place(x=20, y=20, height=200, width=200)
    #scrolled_left_listbox2.place(x=20, y=220, height=200, width=200)
    #scrolled_left_listbox3.place(x=20, y=420, height=200, width=400)
    
    gui.geometry("800x700+450+162")
    gui.mainloop()