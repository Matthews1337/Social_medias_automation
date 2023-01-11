import pyautogui as pg
import pyperclip
import time

# Little automation that i made for testing! :)

# Abrir o navegador Chrome e abrir uma nova aba
pg.hotkey("win", "s")
time.sleep(2)
pg.write("browser")
pg.press("enter")
pg.hotkey("ctrl", "t")
time.sleep(2)



# digitar o site do Linkedin
pyperclip.copy("https://www.linkedin.com/in/matheus-fonseca-20270823a/")
pg.hotkey("ctrl", "v")
pg.press("enter")
time.sleep(2)

# abrir o instagram
pg.hotkey("ctrl", "t")
time.sleep(2)
pyperclip.copy("https://www.instagram.com/matheussf_97/")
pg.hotkey("ctrl", "v")
pg.press("enter")
time.sleep(2)

# Abrir o GitHub
pg.hotkey("ctrl", "t")
time.sleep(2)
pyperclip.copy("https://github.com/Matthews1337")
pg.hotkey("ctrl", "v")
pg.press("enter")
time.sleep(2)


# abrir o bloco de notas
pg.hotkey("win", "s")
time.sleep(1)
pg.write("note pad")
pg.press("enter")
time.sleep(2)

# Falar pra seguir nas redes sociais :)

pg.write("PT: Me Siga Nas Redes Sociais! :) \n")
pg.write("EN: Follow Me On Social Medias! :)")




