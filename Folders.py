import os
from shutil import copytree

def copyFolders(): # копируем папку 
    folders = ["Temp","AVZ","ZD"] # как назвать копии?
    source = r"C:\Users\kochkin.ao\Desktop\Temp — копия"# откуда копировать
    for i in folders:
        main_table =f"C:/Users/kochkin.ao/Desktop/{i}"# куда копировать
        copytree(source, main_table)# команда 


copyFolders()
