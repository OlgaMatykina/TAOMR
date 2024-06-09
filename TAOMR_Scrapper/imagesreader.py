import tkinter as tk
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import os
import sys
class ImagesReader:

    def __init__ (self, images_path , csv = None):
        
        self.csv = csv
        self.images_path = images_path
        self.root = tk.Tk()
        self.i = 0
        self.listdir = sorted(os.listdir(self.images_path))
        self.length = len(self.listdir)
        self.img_name = self.listdir[self.i]
        self.data = {"filename" : images_path,
                    "break_road": 0 if "Breakroad" not in images_path else self.length,
                     "firehose": 0  if "Firehose" not in images_path else self.length,
                     "ground": 0 if "Ground" not in images_path else self.length,
                     "hoses": 0 if "Hoses" not in images_path else self.length,
                     "roads": 0 if "Roads" not in images_path else self.length,
                     "sidewalk": 0 if "Sidewalk" not in images_path else self.length,
                     "wastes": 0 if "Wastes" not in images_path else self.length,
                     "wires": 0 if "Wires" not in images_path else self.length,
                     "puddles": 0 if "Puddles" not in images_path else self.length}
        self.break_road_enable = BooleanVar()
        self.break_road_enable.set(False)

        self.firehose_enable = BooleanVar()
        self.firehose_enable.set(False)

        self.ground_enable = BooleanVar()
        self.ground_enable.set(False)

        self.hoses_enable = BooleanVar()
        self.hoses_enable.set(False)

        self.roads_enable = BooleanVar()
        self.roads_enable.set(False)

        self.sidewalk_enable = BooleanVar()
        self.sidewalk_enable.set(False)

        self.wastes_enable = BooleanVar()
        self.wastes_enable.set(False)
        
        self.wires_enable = BooleanVar()
        self.wires_enable.set(False)

        self.puddles_enable = BooleanVar()
        self.puddles_enable.set(False)

        self.break_road_checkbutton = tk.Checkbutton(self.root,text = "breakroad", variable = self.break_road_enable)
        self.break_road_checkbutton.pack()
        self.firehose_checkbutton = tk.Checkbutton(self.root, text = "firehose", variable = self.firehose_enable)
        self.firehose_checkbutton.pack()
        self.ground_checkbutton = tk.Checkbutton(self.root,text = "ground", variable = self.ground_enable)
        self.ground_checkbutton.pack()
        self.hoses_checkbutton = tk.Checkbutton(self.root,text = "hoses", variable = self.hoses_enable)
        self.hoses_checkbutton.pack()
        self.roads_checkbutton = tk.Checkbutton(self.root,text = "roads", variable = self.roads_enable)
        self.roads_checkbutton.pack()
        self.sidewalk_checkbutton = tk.Checkbutton(self.root,text = "sidewalk", variable = self.sidewalk_enable)
        self.sidewalk_checkbutton.pack()
        self.wastes_checkbutton = tk.Checkbutton(self.root,text = "wastes", variable = self.wastes_enable)
        self.wastes_checkbutton.pack()
        self.wires_checkbutton = tk.Checkbutton(self.root,text = "wires", variable = self.wires_enable)
        self.wires_checkbutton.pack()
        self.puddles_checkbutton = tk.Checkbutton(self.root,text = "puddles", variable = self.puddles_enable)
        self.puddles_checkbutton.pack()
        self.button = tk.Button(self.root, text = "next image" , command= self.check_categories)
        self.button.pack()

        self.img = ImageTk.PhotoImage(Image.open(self.images_path + '/' + self.img_name).resize((1024,1024), Image.LANCZOS))
        self.imglabel = Label(self.root, image = self.img)
        self.imglabel.pack()

        #self.root.bind("<space>", self.check_categories)

        self.root.mainloop()
    def check_categories(self):
        if self.break_road_enable.get() and "Breakroad" not in self.images_path :
            self.data['break_road'] += 1
        if self.firehose_enable.get() and "Firehose" not in self.images_path :
            self.data['firehose'] += 1
        if self.ground_enable.get() and "Ground" not in self.images_path:
            self.data['ground'] += 1
        if self.hoses_enable.get() and "Hoses" not in self.images_path:
            self.data['hoses'] += 1
        if self.roads_enable.get() and "Roads" not in self.images_path:
            self.data['roads'] += 1
        if self.sidewalk_enable.get() and "Sidewalk" not in self.images_path:
            self.data['sidewalk'] += 1
        if self.wastes_enable.get() and "Wastes" not in self.images_path:
            self.data['wastes'] += 1
        if self.wires_enable.get() and "Wires" not in self.images_path:
            self.data['wires'] += 1
        if self.puddles_enable.get() and "Puddles" not in self.images_path:
            self.data['puddles'] += 1
        self.clear()
        self.i += 1
        if self.i == self.length:
            self.create_csv()
            sys.exit()
        self.img_name = self.listdir[self.i]
        self.img = ImageTk.PhotoImage(Image.open(self.images_path + '/' + self.img_name).resize((1024,1024), Image.LANCZOS))
        self.imglabel.config(image = self.img)
    def clear(self):
        self.break_road_enable.set(False)
        self.firehose_enable.set(False)
        self.ground_enable.set(False)
        self.hoses_enable.set(False)
        self.roads_enable.set(False)
        self.sidewalk_enable.set(False)
        self.wastes_enable.set(False)
        self.wires_enable.set(False)
        self.puddles_enable.set(False)
    def create_csv(self):
        if self.csv == None:
            dataframe = pd.DataFrame([self.data])
            dataframe.to_csv('D:/MIPT_Internship/ImageScrapper/' + self.images_path[8:] + '.csv',index=False)
        else:
            dataframe1 = pd.DataFrame([self.data])
            dataframe2 = pd.read_csv(self.csv)
            dataframe = pd.concat([dataframe2, dataframe1])
            dataframe.to_csv('D:/MIPT_Internship/ImageScrapper/' + self.images_path[8:] + '.csv',index=False)
        return
if __name__ == '__main__':
    
    images_path = input("Input Imagespath: ")
    csv_path = input ("Input csv path: ")
    if csv_path == '':
        csv_path = None
    image_reader = ImagesReader(images_path = images_path, csv = csv_path)