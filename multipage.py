import Tkinter as tk
# import tkFont as tkfont

class SampleApp(tk.TK):
	def __init__ (self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title_font = tkfont.FOnt(family='helvetica', size=18,weight='bold',slant='italic')

		container = tk.Frame(self)
		container.pack(side='top',fills='both',expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.frames = {}
		for F in (StartPage,PageOne, PageTwo):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

		self.show_frame('StartPage')

	def show_frame(self , page_name):
		frame = self.frames[page_name]
		frame.tkraise()

class StartPage(tk.Frame):
	def __init__ (self,parent,controller):
		tk.Frame.__init__(self,parent)
		self.controller = controller
		label = tk.Label(self, text='start page', font=controller.title_font)
		label.pack(side='top', fill='x', pady = 10)
		button1 = tk.Button(self, text = 'go to page one',command=lambda: controller.show_frame('PageOne'))
		button2 = tk.Button(self, text = 'go to page 2',command=lambda: controller.show_frame('PageTwo'))
		button1.pack()
		button2.pack()

class PageOne(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self,text ='page1',font=controller.title_font)
		label.pack(side='top',fill='x',pady=10)
		button = tk.Button(self,text='go start page',command=lambda: controller.show_frame('StartPage'))
		button.pack()

class PageTwo(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self,text ='page2',font=controller.title_font)
		label.pack(side='top',fill='x',pady=10)
		button = tk.Button(self,text='go start page',command=lambda: controller.show_frame('StartPage'))
		button.pack()

if __name__ == '__main__':
	app = SampleApp()
	app.mainloop()