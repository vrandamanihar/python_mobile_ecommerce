#enhancement
def toplevel2():
            root1=tkinter.Toplevel()
            root1.title("MI_10")
            def close_window1():
                 
                 root1.destroy()
                 
            root1.geometry("800x800")
            tkinter.Button(root1,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()
            
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image1 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_132535.png")
                    self.img_copy1= self.image1.copy()


                    self.background_image1 = ImageTk.PhotoImage(self.image1)

                    self.background1 = Label(self, image=self.background_image1)
                    self.background1.pack(fill=BOTH, expand=YES)
                    self.background1.bind('<Configure>', self._resize_image1)

                 def _resize_image1(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image1= self.img_copy1.resize((new_width, new_height))

                    self.background_image1 = ImageTk.PhotoImage(self.image1)
                    self.background1.configure(image =  self.background_image1)
            e = Example(root1)
            e.pack(fill=BOTH, expand=YES)
            
####################################################################################################################################
            root2 =tkinter.Toplevel()
            root2.title("REDMI_NOTE_8")
            def close_window1():
                 
                 root2.destroy()
                 
            root2.geometry("800x800")
            tkinter.Button(root2,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image3 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_134535.png")
                    self.img_copy3= self.image3.copy()


                    self.background_image3 = ImageTk.PhotoImage(self.image3)

                    self.background3 = Label(self, image=self.background_image3)
                    self.background3.pack(fill=BOTH, expand=YES)
                    self.background3.bind('<Configure>', self._resize_image3)

                 def _resize_image3(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image3 = self.img_copy3.resize((new_width, new_height))

                    self.background_image3 = ImageTk.PhotoImage(self.image3)
                    self.background3.configure(image =  self.background_image3)
            e = Example(root2)
            e.pack(fill=BOTH, expand=YES)
            


      ##################################################################################################################################

            root3 =tkinter.Toplevel()
            root3.title("POCO_F1")
            def close_window1():
                 
                 root3.destroy()
                 
            root3.geometry("800x800")
            tkinter.Button(root3,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()



            
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image4 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_132959.png")
                    self.img_copy4= self.image4.copy()


                    self.background_image4 = ImageTk.PhotoImage(self.image4)

                    self.background4 = Label(self, image=self.background_image4)
                    self.background4.pack(fill=BOTH, expand=YES)
                    self.background4.bind('<Configure>', self._resize_image4)

                 def _resize_image4(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image4 = self.img_copy4.resize((new_width, new_height))

                    self.background_image4 = ImageTk.PhotoImage(self.image4)
                    self.background4.configure(image =  self.background_image4)
            e = Example(root3)
            e.pack(fill=BOTH, expand=YES)
            
####################################################################################################################################
            root4 =tkinter.Toplevel()
            root4.title("SAMSUNG GALAXY A_30s ")
            def close_window1():
                 
                 root4.destroy()
                 
            root4.geometry("800x800")
            tkinter.Button(root4,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()


            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image5 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_133103.png")
                    self.img_copy5= self.image5.copy()


                    self.background_image5 = ImageTk.PhotoImage(self.image5)

                    self.background5 = Label(self, image=self.background_image5)
                    self.background5.pack(fill=BOTH, expand=YES)
                    self.background5.bind('<Configure>', self._resize_image5)

                 def _resize_image5(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image5 = self.img_copy5.resize((new_width, new_height))

                    self.background_image5 = ImageTk.PhotoImage(self.image5)
                    self.background5.configure(image =  self.background_image5)
            e = Example(root4)
            e.pack(fill=BOTH, expand=YES)
            
#####################################################################################################################################
            root5 =tkinter.Toplevel()
            root5.title("SAMSUNG GALAXY A_51 ")
            def close_window1():
                 
                 root5.destroy()
                 
            root5.geometry("800x800")
            tkinter.Button(root5,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image6 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_134231.png")
                    self.img_copy6= self.image6.copy()


                    self.background_image6= ImageTk.PhotoImage(self.image6)

                    self.background6 = Label(self, image=self.background_image6)
                    self.background6.pack(fill=BOTH, expand=YES)
                    self.background6.bind('<Configure>', self._resize_image6)

                 def _resize_image6(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image6 = self.img_copy6.resize((new_width, new_height))

                    self.background_image6 = ImageTk.PhotoImage(self.image6)
                    self.background6.configure(image =  self.background_image6)
            e = Example(root5)
            e.pack(fill=BOTH, expand=YES)
            
############################################################################################################
            root6 =tkinter.Toplevel()
            root6.title("SAMSUNG GALAXY s_20 ULTRA ")
            def close_window1():
                 
                 root6.destroy()
                 
            root6.geometry("700x850")
            tkinter.Button(root6,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image7 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_134118.png")
                    self.img_copy7= self.image7.copy()


                    self.background_image7 = ImageTk.PhotoImage(self.image7)

                    self.background7 = Label(self, image=self.background_image7)
                    self.background7.pack(fill=BOTH, expand=YES)
                    self.background7.bind('<Configure>', self._resize_image7)

                 def _resize_image7(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image7 = self.img_copy7.resize((new_width, new_height))

                    self.background_image7 = ImageTk.PhotoImage(self.image7)
                    self.background7.configure(image =  self.background_image7)
            e = Example(root6)
            e.pack(fill=BOTH, expand=YES)
            
######################################################################################################################################
            root7=tkinter.Toplevel()
            root7.title("VIVO_VY91 ")
            def close_window1():
                 
                 root7.destroy()
                 
            root7.geometry("800x800")
            tkinter.Button(root7,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image8 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_133405.png")
                    self.img_copy8= self.image8.copy()


                    self.background_image8 = ImageTk.PhotoImage(self.image8)

                    self.background8 = Label(self, image=self.background_image8)
                    self.background8.pack(fill=BOTH, expand=YES)
                    self.background8.bind('<Configure>', self._resize_image8)

                 def _resize_image8(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image8 = self.img_copy8.resize((new_width, new_height))

                    self.background_image8 = ImageTk.PhotoImage(self.image8)
                    self.background8.configure(image =  self.background_image8)
            e = Example(root7)
            e.pack(fill=BOTH, expand=YES)
        
#####################################################################################################################3
            root8 =tkinter.Toplevel()
            root8.title("VIVO_V17")
            def close_window1():
                 
                 root8.destroy()
                 
            root8.geometry("700x850")
            tkinter.Button(root8,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image9 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_133458.png")
                    self.img_copy9= self.image9.copy()


                    self.background_image9 = ImageTk.PhotoImage(self.image9)

                    self.background9 = Label(self, image=self.background_image9)
                    self.background9.pack(fill=BOTH, expand=YES)
                    self.background9.bind('<Configure>', self._resize_image9)

                 def _resize_image9(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image9 = self.img_copy9.resize((new_width, new_height))

                    self.background_image9 = ImageTk.PhotoImage(self.image9)
                    self.background9.configure(image =  self.background_image9)
            e = Example(root8)
            e.pack(fill=BOTH, expand=YES)
            
############################################################################################################################
            root9=tkinter.Toplevel()
            root9.title("OPPO_A11K")
            def close_window1():
                 
                 root9.destroy()
                 
            root9.geometry("700x850")
            tkinter.Button(root9,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image10= Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_133731.png")
                    self.img_copy10= self.image10.copy()


                    self.background_image10 = ImageTk.PhotoImage(self.image10)

                    self.background10 = Label(self, image=self.background_image10)
                    self.background10.pack(fill=BOTH, expand=YES)
                    self.background10.bind('<Configure>', self._resize_image10)

                 def _resize_image10(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image10 = self.img_copy10.resize((new_width, new_height))

                    self.background_image10 = ImageTk.PhotoImage(self.image10)
                    self.background10.configure(image =  self.background_image10)
            e = Example(root9)
            e.pack(fill=BOTH, expand=YES)
            
###############################################################################################################################
            root10 =tkinter.Toplevel()
            root10.title("OPPO_RENO3")
            def close_window1():
                 
                 root10.destroy()
                 
            root10.geometry("700x850")
            tkinter.Button(root10,text="click here to VEIW NEXT MOBILE ",command=close_window1).pack()
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image11 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_133845.png")
                    self.img_copy11= self.image11.copy()


                    self.background_image11 = ImageTk.PhotoImage(self.image11)

                    self.background11= Label(self, image=self.background_image11)
                    self.background11.pack(fill=BOTH, expand=YES)
                    self.background11.bind('<Configure>', self._resize_image11)

                 def _resize_image11(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image11 = self.img_copy11.resize((new_width, new_height))

                    self.background_image11 = ImageTk.PhotoImage(self.image11)
                    self.background11.configure(image =  self.background_image11)
            e = Example(root10)
            e.pack(fill=BOTH, expand=YES)
            
#################################################################################################################################
            root11 =tkinter.Toplevel()
            root11.title("IPHONE_XS ")
            def close_window1():
                 
                 root11.destroy()
                 
            root11.geometry("700x850")
            tkinter.Button(root11,text="CLOSE THE  main PHONE TABLES WINDOW TO PROCEED ",command=close_window1).pack()
            class Example(Frame):
                 def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)



                    self.image12 = Image.open("C:/Users/Owner/CS PROJECT/Screenshot_2020_0917_133941.png")
                    self.img_copy12= self.image12.copy()


                    self.background_image12 = ImageTk.PhotoImage(self.image12)

                    self.background12 = Label(self, image=self.background_image12)
                    self.background12.pack(fill=BOTH, expand=YES)
                    self.background12.bind('<Configure>', self._resize_image12)

                 def _resize_image12(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image12 = self.img_copy12.resize((new_width, new_height))

                    self.background_image12 = ImageTk.PhotoImage(self.image12)
                    self.background12.configure(image =  self.background_image12)
            e = Example(root11)
            e.pack(fill=BOTH, expand=YES)
            root11.mainloop()

