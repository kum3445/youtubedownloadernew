from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from tkinter.filedialog import askopenfile
window = Tk()

window.geometry("700x700")
window.configure(bg="grey")
window.title("YOUTUBE DOWNLOADER")
logo=PhotoImage(file="logo.png")
window.iconphoto(False, logo)

Label(window, text="Video downloader", font="Arial 30 bold").pack(padx=5, pady=50)


video_link= StringVar()
path_link1 = StringVar()
path_link2 = StringVar()

Label(window, text="Enter the link:", font=("Arial",10,"bold")).place(x=15,y=120)
Entry_link=Entry(window, width=50, font=35, textvariable=video_link, bd=4).place(x=180,y=120)
Label(window, text="Enter the video path:", font=("Arial",10,"bold")).place(x=15,y=150)
Entry_link=Entry(window, width=50, font=35, textvariable=path_link1, bd=4).place(x=180,y=150)
Label(window, text="Enter the audio path:", font=("Arial",10,"bold")).place(x=15,y=180)
Entry_link=Entry(window, width=50, font=35, textvariable=path_link2, bd=4).place(x=180,y=180)

def Video_download():
    video_url=YouTube(str(video_link.get()))
    videos = video_url.streams[3]
    
    #print(video_url.streams)
    
    videos.download(str(path_link1.get()))
    
    Label(window, text="Download Completed", font ="Arial 25 bold", bg="white", fg="black").place(x=120,y=450)
    Label(window, text="Check out the file", font="Arial 25 bold ",bg="white" ).place(x=130,y=550)
    
def audio_download():
    video_url=YouTube(str(video_link.get()))
    audios=video_url.streams.get_audio_only()
    audios.download(str(path_link2.get()))
    Label(window, text="Download Completed", font ="Arial 25 bold", bg="white", fg="black").place(x=120,y=450)
    Label(window, text="Check out the file", font="Arial 25 bold ",bg="white" ).place(x=130,y=550)
Button(window, text= "Video Download", font=("Arial",25,"bold"), bg="white", command=Video_download).place(x=150,y=250)
Button(window, text= "Audio Download", font=("Arial",25,"bold"), bg="white", command=audio_download).place(x=150,y=330)    

window.mainloop()