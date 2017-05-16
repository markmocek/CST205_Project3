'''
CST205 - Project 3 - Justin Hines, Francisco Hernandez, Mark Mocek - 5/16/17

Justin - Created crypt.py file. It takes user input and encrypts or decrypts it with
a given key and the cipher library.
Francisco - Created the facedetect.py file. It takes the image captured and compares it
to the face on file for the user.
Mark - Created the main.py file. The file supplies the user with a GUI to operate with and 
calls the functions from the crypt.py and facedetect.py files.
'''

import cv2
import tkinter
from tkinter import *
from crypt import encryption, decryption
from facedetect import face_recognition


# image capture for face recognition
def image_capture():
    # Camera port 0 is the laptop webcam
    camera_port = 0

    # Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = 30

    # Index to a camera port.
    camera = cv2.VideoCapture(camera_port)

    # Captures image from the camera and returns it in PIL format
    def get_image():
        # read to get a full image out of a VideoCapture object
        retval, im = camera.read()
        return im

    # Ramp the camera - these frames will be discarded
    for i in xrange(ramp_frames):
        temp = get_image()

    print("Taking image...")

    # Take the actual image we want to keep
    camera_capture = get_image()
    file = "scott.jpeg"

    # correct format based on the file extension you provide
    cv2.imwrite(file, camera_capture)

    print("Complete")

    # Release the camera
    del (camera)


# GUI for program
class TheGUI:
    LABEL_TEXT = [
        "The program uses face recognition as a security measure when encrypting and decrypting. Click for more info..",
        "Program starts under the assumption that you are logged in as the current user. 1/4",
        "Once the 'Encrypt' or 'Decrypt' button is chosen, the program takes and image from the web cam. 2/4",
        "The face recognition then determines if the face is that of the user. 3/4",
        "If it is the user, the program does as asked. If it is not he user, the program ends. 4/4"
    ]

    def __init__(self, master, toencode):
        self.master = master
        master.title("Face Recognition Encryption and Decryption")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        Label(master, text="Enter String:").grid(row=0)

        e1 = Entry(master)

        e1.grid(row=0, column=1)

        self.greet_button = Button(master, text="Encrypt", command=self.encrpt(e1))
        self.greet_button.pack()

        self.greet_button = Button(master, text="Decrypt", command=self.decrypt(e1))
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def encrpt(self, e1):
        image_capture()
        if(face_recognition()):
            encryption(e1)

    def decrypt(self, e1):
        image_capture()
        if (face_recognition()):
            decryption(e1)

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT)
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = TheGUI(root)
root.mainloop()
