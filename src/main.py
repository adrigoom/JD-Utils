import os
if os.name != 'nt':
    print("Sorry, only windows supported for now :(")
    os._exit(0)
from file.file_select import file_select
from tools.ktape_sort import ktape_sort
from tools.ktape_romanizer import ktape_romanizer

while True:
    os.system('cls') #i know its deprecated idk how the new one works
    print("JD-Utils\n")

    print("1. Sort Ktape")
    print("2. Romanize Ktape (russian only)")
    print("3. Exit")

    o = input("Choose an option:")

    match o: 
        case "1":
            ktape_sort(file_select())
        case "2":
            ktape_romanizer(file_select())
        case "3":
            os.system('cls')
            os._exit(0)
        case _:
            print("unknown")

os.system('pause')
