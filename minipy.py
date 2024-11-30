from tkinter import * 
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox ,filedialog
import tkinter as tk

import speech_recognition as sr 


import PyPDF2
import pyttsx3
import os

import googletrans
from googletrans import Translator

import datetime

from gtts import gTTS
from playsound import playsound


root=Tk()
root.title("Text to speech")
root.geometry("1030x570")
root.resizable(False,False)
root.config(bg="#161d3f")

engine = pyttsx3.init()


def pdfreading(gender ,text,v):

    path = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)
    total_pages= pdfReader.numPages
    from_page = pdfReader.getPage(total_pages-1)
          

    text= from_page.extractText()
          
    texttospeech(gender ,text,v)



def texttospeech(gender,text,v):
    if (gender == 'Male'):
        engine.setProperty('voice', v[0].id)
        speech(text)

    else:
        engine.setProperty('voice', v[0].id)
        speech(text)


def speech(text):
    engine.setProperty('rate', current_value.get())
    engine.say(text)
    engine.runAndWait()



def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    v = engine.getProperty('voices')
    print(choice)


    if choice=="Text":
        texttospeech(gender ,text,v)
    

    else:
        try:
            pdfreading(gender ,text,v)

        except:
            messagebox.showerror("Invalid!","Please upload pdf !")
#############################################################################

def pdfreading2(gender ,text,v):

    path = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)
    total_pages= pdfReader.numPages
    from_page = pdfReader.getPage(total_pages-1)
          

    text= from_page.extractText()
          
    texttospeech2(gender ,text,v)



def texttospeech2(gender,text,v):
    if (gender == 'Male'):
        engine.setProperty('voice', v[0].id)
        download(text)

    else:
        engine.setProperty('voice', v[0].id)
        download(text)


def download(text):
    engine.setProperty('rate', current_value.get())
    path=filedialog.askdirectory()
    os.chdir(path)
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    engine.save_to_file(text,f'TextToSpeech{now.strftime("%Y %m %d %H %M %S")}.mp3')
    engine.runAndWait()
            

def select_file(gender,text,v):

    if choice=="Text":
        texttospeech2(gender ,text,v)
    

    else:
        try:
            pdfreading2(gender ,text,v)

        except:
            messagebox.showerror("Invalid!","Please upload pdf !")
    
def speech_download():

    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    v = engine.getProperty('voices')

    select_file(gender,text,v)

    

  

def Upload():
    global filename
  
    try:
        
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='Select Image File',
                                            filetype=(('PDF File','*.pdf'),('all files','*.*'))) # type: ignore
        messagebox.showinfo("info","Pdf Uploaded Sucessfully! ")
    except:
        messagebox.showerror("Invalid","Corrupted file!!!")



def translate(text_,trans_to):

    # # print(text_)
##    text_="how are you "

    
    t1=Translator()
    trans_text=t1.translate(text_,src='en',dest=trans_to)
    trans_text=trans_text.text

    return trans_text

    
  

    
def Listen():

    language_to=combo.get()

    engine_source=pyttsx3.init()
    voices=engine_source.getProperty('voices')
    engine_source.setProperty('voice',voices[0].id)
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Clearing background noises...Pleasw wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)
    try:
        
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

        text_area.delete(1.0,END)

        text_area.insert(END,text)

    except Exception as ex:
        print(ex)
    
    a='Tranlating..'
    engine_source.say(a)
    engine_source.runAndWait()


    text_area2.delete(1.0,END)


    

    tranlated_text=translate(text,combo.get())
    # print(tranlated_text)


    text_area2.insert(END,tranlated_text)


def trans_text():
    text1_=text_area.get(1.0,END)
    tranlated_text=translate(text1_,combo.get())

    text_area2.delete(1.0,END)
    text_area2.insert(END,tranlated_text)


def translatedtext():

    print(combo.get())
    mytext=text_area2.get(1.0,END)

    for key,value in googletrans.LANGUAGES.items():
        if str(value).startswith(combo.get()):
            language=key 

    try:
        
        myobj=gTTS(text=mytext,lang=language,slow=True)
        print(myobj)
        myobj. save("welcome1.mp3")
        playsound("welcome1.mp3")
    except:
        myobj=gTTS(text=mytext,lang='en',slow=True)
        print(myobj)
        myobj. save("welcome1.mp3")
        playsound("welcome1.mp3")


def Uploadmusic():

    try:
        
        filename1=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='Select Image File',
                                            filetype=(('*.pdf','*.mp3'),('all files','*.*'))) # type: ignore
        messagebox.showinfo("info","MP3 Uploaded Sucessfully! ")
    except:
        messagebox.showerror("Invalid","Corrupted file!!!")

    r = sr.Recognizer()

    audio_file = sr.AudioFile(filename1)

    with audio_file as source:

        audio = r.record(source)

        text = r.recognize_google(audio)

        text_area.delete(1.0,END)
        text_area.insert(END,text)
            

    
##print(gTTS.lang.tts_langs())   

#icon
image_icon=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\icon.ico")
root.iconphoto(False,image_icon)


#Top Frame
Top_frame=Frame(root,bg="#56aaff",width=1100,height=130)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\icon.ico")
Label(Top_frame,image=Logo,bg="#56aaff").place(x=20,y=20)

Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="#56aaff",fg="#fff").place(x=170,y=50)

#######################################

text_area=Text(root,font="Robote 20",bg="#dddaf5",relief=GROOVE,wrap=WORD)
text_area.place(x=40,y=140,width=600,height=200)

mic_image=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\mic.ico")
mic_button=Button(root,image=mic_image,bg="#dddaf5",command=Listen)
mic_button.place(x=50,y=280)


#####################################

language=googletrans.LANGUAGES
languageV=list(language.values())

lang1=language.keys()




combo=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo.place(x=180,y=100)
combo.set("ENGLISH")


text_area2=Text(root,font="Robote 20",bg="#dddaf5",relief=GROOVE,wrap=WORD)
text_area2.place(x=40,y=360,width=600,height=200)

Label(root,text="VOICE",font="arial 15 bold",bg="#161d3f",fg="white").place(x=700,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#161d3f",fg="white").place(x=700,y=200)

gender_combobox=Combobox(root,values=['Male','Female'],font='arial 14 ',state="r",width=10)
gender_combobox.place(x=800,y=160)
gender_combobox.set("Male")



##############Slider #################################3
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())


#for changing background color of scale 
style = ttk.Style()
style.configure("TScale", background="#161d3f")


##insert >>> style="TScale" inside slider
    
slider = ttk.Scale(root,from_=30,to=250,orient='horizontal',
    command=slider_changed,variable=current_value)

slider.place(x=800,y=200)


# value label
value_label = ttk.Label(root,text=get_current_value())
value_label.place(x=800,y=250)

################################################

imageicon=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\speak.ico")
btn=Button(root,text="Speak",compound=LEFT,image=imageicon,width=130,font="arial 14 bold",command=speaknow)
btn.place(x=700,y=380)

imageicon2=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\download.ico")
save=Button(root,text="Save",compound=LEFT,image=imageicon2,width=130,bg="#39c790",font="arial 20 bold",command=speech_download)
save.place(x=850,y=380)


uploadimage=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\pdfimage.ico")
Upload=Button(root,image=uploadimage,bg="#56aaff",command=Upload) # type: ignore
Upload.place(x=650,y=30)

uploadmusicimage=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\music.ico")
Uploadmusic=Button(root,image=uploadmusicimage,bg="#56aaff",command=Uploadmusic) # type: ignore
Uploadmusic.place(x=530,y=45)

transimage=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\trans.ico")
trans=Button(root,image=transimage,bg="#56aaff",command=trans_text) # type: ignore
trans.place(x=450,y=60)

speakimage=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\otherspeaker.ico")
speak=Button(root,image=speakimage,bg="#dddaf5",command=translatedtext) # type: ignore
speak.place(x=50,y=500)

######pdf and text mode button


button_mode=True
choice="Text"
def changemode():
    global button_mode
    global choice
    
    if button_mode:
       
        choice="PDF"
        mode.config(image=pdfmode,activebackground="white")
        button_mode=False
    else:
        
        choice="Text"
        mode.config(image=textmode,activebackground="white")
        button_mode=True
        
    

textmode=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\modeText.ico")
pdfmode=PhotoImage(file=r"C:\Users\GUNJAN\Desktop\new mini pro\modepdf.ico")
mode=Button(root,image=textmode,bg="#56aaff",bd=0,command=changemode)
mode.place(x=780,y=40)


###########################



root.mainloop()