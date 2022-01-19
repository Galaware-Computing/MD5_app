# Module importation
import tkinter as tk 
#from tk import ttk
from tkinter import Menu
import logging as lg
import hashlib
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename

from md5 import MD5

class Application(tk.Tk):
    """
    
    The main class for my MD5 program
    
    """
    def __init__(self):
        """
        the main view function for my interface
        """
        tk.Tk.__init__(self)
        # Add a title
        self.title("MD5 Algorithm")
        # windows size
        self.minsize(480,240)
        # Disable resizing the GUI
        self.resizable(False, False) 
        # Change the main windows icon
        self.iconbitmap('md5_icon.ico') 
        self.create_widgets()       
        
    def create_widgets(self):
        """ 
        Run necessary view and widget configuration methods.
        """
        self.menuBar()
        self.main_frame()
        self.banner()
        self.inputs()
        self.outputs()
        self.configure_buttons()
    
#===========================================Interface_function====================================================================================      
    # Create the frame
    def main_frame(self):
        lg.info(" The main frame configuration")
        self.mainframe = tk.Frame(self, background='gray')   
        self.mainframe.grid(column=0, row=0, sticky=('N','S','E','W'))
        
    # Create the banner  
    def banner(self):
        """
        Configure the header banner for the app with a simple tkinter label.
        """
        lg.info("We are in the banner method")
        banner = tk.Label(self.mainframe, background='gray', text="MD5 Hash", font=('Futura', 28), fg='white')
        banner.grid(row=0, column=0, sticky=('N', 'S', 'E', 'W'), padx=150, pady=15)    
    
    # Configure the inputs buttons
    def inputs(self):
        """
        Configure app input objects: file path, hash value, radio buttons.
        """
        lg.info("We're in the configure_inputs method")
        inputs_frame = tk.Frame(self.mainframe, borderwidth=2, relief='flat')
        inputs_frame.grid(row=1, column=0, sticky=('N', 'S', 'E', 'W'))
      
        message_label = tk.Label(inputs_frame, text=" Message :", font=('Futura', 10))
        message_label.grid(row=0, column=1, sticky='N', pady=10)
        
        self.message_entry = tk.Entry(inputs_frame, width=60)
        self.message_entry.grid(row=0, column=2, sticky=('E', 'W'))
      
        filepath_label = tk.Label(inputs_frame, text="File Name :", font=('Futura', 10))
        filepath_label.grid(row=1, column=1, sticky='N', pady=10)
        
        self.file_entry = tk.Entry(inputs_frame, width=60)
        self.file_entry.bind("<Button-1>", self.input_file)
        self.file_entry.grid(row=1, column=2, sticky=('E', 'W'))

       
    
    # Configure the outputs buttons
    def outputs(self):
        """
        Configure output widgets: hash value, match value.
        """
        lg.info("We're in the configure_outputs method")
        outputs_frame = tk.Frame(self.mainframe, borderwidth=2, relief='flat')
        outputs_frame.grid(row=2, column=0, sticky=('N', 'S', 'E', 'W'))   
        #=========== Message value
        hash_value_label = tk.Label(outputs_frame, text="Message Hash Value :", font=('Futura', 10))
        hash_value_label.grid(row=0, column=1, sticky='E', pady=10)

        self.hash_value = tk.StringVar()
        self.hash_value.set("")

        self.hash_value_entry = tk.Entry(outputs_frame, state='readonly', readonlybackground='white', fg='black', width=50)
        self.hash_value_entry.config(textvariable=self.hash_value, relief='flat', highlightthickness=0)
        self.hash_value_entry.grid(row=0, column=2, columnspan=2, sticky=('W', 'E'))
        
        #============ File value
        hash_value_label2 = tk.Label(outputs_frame, text="File Hash Value :", font=('Futura', 10))
        hash_value_label2.grid(row=1, column=1, sticky='E', pady=10)

        self.hash_value2 = tk.StringVar()
        self.hash_value2.set("")

        self.hash_value_entry2 = tk.Entry(outputs_frame, state='readonly', readonlybackground='white', fg='black', width=50)
        self.hash_value_entry2.config(textvariable=self.hash_value2, relief='flat', highlightthickness=0)
        self.hash_value_entry2.grid(row=1, column=2, columnspan=2, sticky=('W', 'E')) 
        
        #========== Result value
        result_label = tk.Label(outputs_frame, text="Result :", font=('Futura', 10))
        result_label.grid(row=2, column=1, sticky='E', pady=10)

        self.result_var = tk.StringVar()
        self.result_var.set("")

        result_display_label = tk.Label(outputs_frame, textvariable=self.result_var)
        result_display_label.grid(row=2, column=2, sticky=('W'))
        
    # Define the configuration of all buttons   
    def configure_buttons(self):
        """
        Configure button frame and two buttons: hash and clear.
        """
        lg.info("We're in the configure buttons method.")
        buttons_frame = tk.Frame(self.mainframe, borderwidth=2, relief='flat')
        buttons_frame.grid(row=3, column=0,  sticky=('N', 'S', 'E', 'W'))
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.rowconfigure(0, weight=1)
        buttons_frame.rowconfigure(1, weight=1)

        hash_button = tk.Button(buttons_frame, text='Hash', relief='raised', command=self.runHash)
        hash_button.grid(row=0, column=0, sticky=('N', 'S', 'E', 'W'))

        clear_button = tk.Button(buttons_frame, text='Clear', relief='raised', command=self.clear)
        clear_button.grid(row=1, column=0, sticky=('N', 'S', 'E', 'W'))
    
    # Create the menu bar  
    def menuBar(self):  
        """ Configure the menu bar and sub-menu
        """
        lg.info(" we're in the menu bar configuration method.")    
        # Creating a menu bar
        menu_bar=Menu(self)
        # Create menu and add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
               
        # Add another Menu to the menu bar and an item
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.msgBox)
        menu_bar.add_cascade(label="Help",menu = help_menu)
        self.config(menu=menu_bar)    
        
#========================================Performed_function==============================================================================    
    # Clear all entry
    def clear(self):
        """
        Clears all input and output fields.
        """
        lg.info("Clear button pressed.")
        self.hash_value.set("")
        self.hash_value2.set("")
        self.result_var.set("")
        self.file_entry.delete(0, 'end')
        self.message_entry.delete(0, 'end')  

    # Choose the file   
    def input_file(self, event):
        """
        Controls file path pop up dialog on click of entry field.
        """
        lg.info("Choose File Name method called.")
        self.input_path = askopenfilename(title="Choose File to Hash")
        lg.info("File path: " + self.input_path)
        self.file_entry.insert(0, self.input_path)

    # Apply hash function   
    def  runHash(self):
        """
        Contains functionality to run the hash function.
        """
        user_input = self.message_entry.get()
        lg.info("Message_entry: {}".format(user_input))
        message_digest = MD5.output(user_input)
        lg.info("Hash message_digest: {}".format(message_digest))
        message_digest2 = self.msg_digest(user_input)
        lg.info("Hash message_digest: {}".format(message_digest2))
              
        if message_digest == message_digest2:
            # Display hash value
            self.hash_value.set(message_digest)
            new_hash_value_entry = self.hash_value_entry.get()
            lg.info("New Hash Value Entry: {}".format(new_hash_value_entry))
            self.result_var.set(" Successful hash ! ")
        else:
            self.result_var.set(" Hash fail ! ")
        
        lg.info("Hash button pressed.")
        # Take values of file path or message input
        path = self.input_path
        lg.info("File path: {}".format(path))   
        
        if path:
            file_digest = self.fileDigest(path)
            lg.info("Hash file_digest: {}".format(file_digest))
            self.hash_value2.set(file_digest)
            new_hash_value_entry2 = self.hash_value_entry2.get()
            lg.info("New Hash Value Entry: {}".format(new_hash_value_entry2))
            self.result_var.set(" Successful hash ! ")
            MD5.write_file(path, file_digest)
        else:
            pass
            
    #Exit GUI cleanly
    def _quit(self):
        """ Control button quit
        """
        lg.info("Button quit pressed")
        App.quit()
        App.destroy()
        exit()
    
    # Display a message box // read chapter 3 p84
    def msgBox(self):
        msg.showinfo("Information", "This is MD5 software realize in 2022 by NEBM.")
                        
    # Hash message with hashlib module
    def msg_digest(self, message):
        """  Run hash function on message. Return digest.
        """
        if message:
            hashFunc = hashlib.md5()
            hashFunc.update(message.encode('utf-8'))
            disgested = hashFunc.hexdigest()
            return disgested
        
    # Hash file with hashlib module
    def fileDigest(self,path):
            """ Run hash function on file path. Return digest.
            """
            if path:          
                hashFunc = hashlib.md5()
                blockSize = 65535
            try:
                with open(path, 'rb') as target:
                    buf = target.read(blockSize)
                    while len(buf) > 0:
                        hashFunc.update(buf)
                        buf = target.read(blockSize)
                digested = hashFunc.hexdigest()
                return digested
            except (IOError, TypeError) as error:
                lg.debug("Error in hash func: {}".format(error))     
            
 
# Create instance
App=Application()  
# start GUI  
App.mainloop()       

