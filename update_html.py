#Testable and working, editable HTML page using Python 3.9.1
#Created by Nick Pranno, a student at the Tech Academy

#Import all tkinter modules
import tkinter as tk     
from tkinter import ttk
from tkinter import messagebox

#Import webbrowser module
import webbrowser


 
#Main class to pass functions, create widgits and styles, used to pass information from functions to classes
class MainApp:          
    def __init__(self, master):
        master.title('Update your HTML web page!')
        
#Allows GUI to be resized, if set to False, it would not be reziable (boolean)
        master.resizable(True, True)             
        self.style = ttk.Style()
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

#LABEL widget
        ttk.Label(self.frame_header, wraplength=500,                                       
            text=("Please enter some text in the field below to update your page."),
            justify='center').pack() #centers above text

        self.frame_content = ttk.Frame(master)
#TEXT ENTRY widget        
        self.html_body = tk.Text(self.frame_content,width=40, height=15, font=('Helvetica', 12))                           
        self.html_body.pack()
        self.frame_content.pack()

# UPDATE & CLEAR buttons
        ttk.Button(self.frame_content, text='UPDATE', command=self.update).pack(expand='True', side='left')
        ttk.Button(self.frame_content, text='CLEAR', command=self.clear).pack(expand='True', side='right')

#Creates HTML Function used to pass text variable to the opening of a new web browser in a new tab
    def Create_html(self, text):  
        f=open("update.html","w") #opens test html while using 'w' to be able to write it, {} is the variable that will be written and passed into the page
        html_string="\
            <html>\n\
                <body>\n\
                    <h1>\n\
                        {}\n\
                    <h1>\n\
                </body>\n\
            </html>".format(text)
        f.write(html_string)
        f.close()
        url ='update.html'
        webbrowser.open_new_tab(url)

#Updates information by creating a new html page while clearing the old information and displaying a message box notifying that the information has been updated
    def update(self):                                                  
        self.Create_html(self.html_body.get(1.0, 'end'))
        self.clear()
        messagebox.showinfo(title='UPDATED', message='HTML body text successfully updated.')

    def clear(self):
        self.html_body.delete(1.0, 'end')

       

 

if __name__ == '__main__':
    root = tk.Tk() #use tkinter module for this program
    MainApp = MainApp(root) #calls MainApp function
    root.mainloop() #keeps window open (loops) until user closes the program
