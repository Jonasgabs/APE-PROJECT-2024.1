from PIL import Image
from customtkinter import *

janela = CTk()
janela.geometry("400x500")


image = Image.open('img/Tribunal_Superior_Eleitoral.png')
img = CTkImage(light_image = image, dark_image = image, size = (275, 75))
logo_label = CTkLabel(master = janela, image = img)
logo_label.pack(pady = (20, 10))

janela.mainloop()