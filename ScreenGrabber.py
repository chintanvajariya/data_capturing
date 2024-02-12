import tkinter as DataCollection # fullscreen window
import pyautogui # screenshot service
import pytesseract # image to text
import csv # make and write to .csv file
from datetime import datetime # date and time information
import os # filepaths

class ScreenCapture:
    
    # initializing all the capture details
    def __init__(self):
        self.root = DataCollection.Tk()
        self.selections = []
        self.canvas = None
        self.running = False

        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)
        self.root.bind('<ButtonPress-1>', self.on_button_press)
        self.root.bind('<B1-Motion>', self.on_move_press)
        self.root.bind('<ButtonRelease-1>', self.on_button_release)

        self.canvas = DataCollection.Canvas(self.root, cursor='cross')
        self.root.config(cursor='cross')
        self.canvas.pack(fill=DataCollection.BOTH, expand=True)

    # determining starting selection position
    def on_button_press(self, event):
        self.start_x = self.canvas.winfo_pointerx()
        self.start_y = self.canvas.winfo_pointery()
        self.root.config(cursor='cross')
        
    def on_move_press(self, event): {
        self.root.config(cursor='cross')
    }
        
    # determining ending position
    def on_button_release(self, event):
        end_x = self.canvas.winfo_pointerx()
        end_y = self.canvas.winfo_pointery()
        # storing the positions
        self.selections.append((min(self.start_x, end_x), min(self.start_y, end_y), abs(end_x - self.start_x), abs(end_y - self.start_y)))
        self.running = True
        self.root.config(cursor='')
        # only stops after two selections have been made
        if len(self.selections) == 2:
            self.root.quit()

    
    def capture(self):
        self.root.mainloop()
        self.root.destroy()

        # only starts after two selections
        if self.running and len(self.selections) == 2:
            t0 = datetime.now()

            save_folder = '/Users/chintanvajariya/research'  # Replace with the data folder path

            #formatting file title and data
            current_date = datetime.now().strftime("%Y%m%d")
            current_time = datetime.now().strftime("%H-%M-%S")

            file_paths = [
                os.path.join(save_folder, f'NewDataCollection-Region1-{current_date}-{current_time}.csv'),
                os.path.join(save_folder, f'NewDataCollection-Region2-{current_date}-{current_time}.csv')
            ]

            # make two new files for writing
            files = [open(file_path, 'a', newline='') for file_path in file_paths]
            writers = [csv.writer(file) for file in files]
            
            # initialize .csv file with titles
            one = True
            for writer in writers:
                writer.writerow(['Central Time', ' Local Time', ' Elapsed Time']) if one else writer.writerow(['Eastern Time', ' Local Time', ' Elapsed Time'])
                one = False

            # loop this forever (until you decide to stop the program)
            while True:
                for i, (left, top, width, height) in enumerate(self.selections):
                    screenshot = pyautogui.screenshot(region=(left, top, width, height)) # take the screenshot
                    text = pytesseract.image_to_string(screenshot) # read the text in screenshot
                    text = text.replace("\n", " ").strip()
                    
                    current_time = datetime.now().strftime("%H:%M:%S") # determine current time
                    elapsed_time = datetime.now() - t0 # and elapsed time

                    writers[i].writerow([text, current_time, elapsed_time]) # write data to .csv
                    files[i].flush() # send data straight after writing

                    print(f"Region {i+1}", text, current_time, elapsed_time) # print to terminal for easy error check

#run our program
capture_tool = ScreenCapture()
capture_tool.capture()