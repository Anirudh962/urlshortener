import tkinter
import pyshorteners

gui = tkinter.Tk()
gui.title("URL shortener")
gui.geometry("500x300")
def shorten():
    shortener = pyshorteners. Shortener()
    short_url = shortener.tinyurl.short (longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))
    
longurl_label = tkinter.Label(gui, text="Enter long URL:")
longurl_entry = tkinter.Entry(gui)
shorten_button = tkinter.Button(gui, text="Shorten URL", command=shorten)
shorturl_label = tkinter.Label(gui, text="Your Shortened URL:")
shorturl_entry = tkinter.Entry(gui) 


longurl_label.pack()
longurl_entry.pack()
shorten_button.pack()
shorturl_label.pack()
shorturl_entry.pack()

gui.mainloop()