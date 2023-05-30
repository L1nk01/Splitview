import ttkbootstrap as ttk

'''
Splitview

Authors: L1nk01 and XanAether
Creation date: 05/29/2023

Here goes the description...
'''

'''
TODO:
    - Project description
'''

# Main window parameters
root = ttk.Window()
root.geometry('1280x720')
root.state('zoomed')

# Sections
windows_apps = ttk.Frame(root, bootstyle='primary', padding='0')
google_calendar = ttk.Frame(root, bootstyle='success', padding='0')
google_keep = ttk.Frame(root, bootstyle='danger', padding='0')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure((0, 1, 2), weight=1)

windows_apps.grid(row=0, column=0, sticky='nsew')
google_calendar.grid(row=0, column=1, sticky='nsew')
google_keep.grid(row=0, column=2, sticky='nsew')

root.mainloop() 

# class Main(ttk.Window):
#     def __init__(self):
#         super().__init__()
        
#         self.title('Splitview')
#         self.geometry('1280x720')
#         self.state('zoomed') # Defaults window as full window when opened
#         # self.resizable(False, False) # Avoids the window to be resized
        
# class Frame(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)

# if __name__ == '__main__':
#     root = Main()
#     applications = Frame(root)
#     applications.pack()
#     root.mainloop()