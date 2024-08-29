from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import QRcodeReader
import reader


def get_button(window, text, color, command, fg='white'):
    button = ttk.Button(window,
                        text=text,
                        activebackground= 'black',
                        activeforeground='white',
                        fg= fg,
                        bg=color,
                        command=command,
                        height=2,
                        width=20,

                        )
    return button

def get_img_label(window):
    label = ttk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label(window, text):
    label=ttk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify="left")
    return label
def get_entry_text(window):
    inputtxt = ttk.Text(window,
                        height=2,
                        width=15,
                        font=("Arial", 32))
    return inputtxt

def msg_box(title, description):
    messagebox.showinfo(title, description)

class App:
    def __init__(self):
        self.main_window =ttk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = get_button(self.main_window, 'Manually Login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=300)

        self.register_new_user_main_window = get_button(self.main_window, 'register', 'green', self.register_new_user)
        self.register_new_user_main_window.place(x=750 , y=400)

        self.webcam_label = get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700,  height=500)

        self.add_webcam(self.webcam_label)
        print('app.__init__')

    def add_webcam(self,label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()
        print('app.addwebcam')

    def process_webcam(self):
        ret, frame = self.cap.read()
        decoded_frame =reader.decoder(frame)
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

        self._label.imgtk = imgtk
        self._label.configure(image =imgtk)

        self._label.after(2, self.process_webcam)
        print('app.process_webcam')

    def login(self):
        self.login_button_main_window = ttk.Toplevel(self.main_window)
        self.login_button_main_window.geometry("1200x520+350+100")

        self.label_SSID = get_text_label(self.login_button_main_window, text="SSID")
        self.label_SSID.place(x=100 , y= 200)
        self.input_SSID = get_entry_text(self.login_button_main_window)
        self.input_SSID.place(x=100, y=250)
        self.label_password = get_text_label(self.login_button_main_window, text="Password")
        self.label_password.place(x=200, y=200)
        self.input_password = get_entry_text(self.login_button_main_window)
        self.input_password.place(x=200 , y=250)
        print('app.login')
        try:
            output = QRcodeReader.createNewConnection(self.input_SSID,self.input_SSID, self.input_password)
        except:
            output ='Failed'


    def register_new_user(self):
        self.register_new_user_main_window =ttk.Toplevel(self.main_window)
        self.register_new_user_main_window.geometry("1200x520+350+100")


if __name__ =='__main__':
    App()