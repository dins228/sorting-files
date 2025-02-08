import os  
import shutil 

def organize_files(directory):
    
    os.chdir(directory)
    cwd = os.getcwd()

    l = [f for f in os.listdir(cwd) if os.path.isfile(f)]
    l2 = []

    for value in l:
        if '.' in value:
            s = value.split('.')[-1]  
            l2.append(s)

    print(l, l2)

    for extension in set(l2):
        dirname = os.path.join(cwd, extension)  
        if not os.path.exists(dirname):
            os.makedirs(dirname)


    for files, extension in zip(l, l2):
        if extension in files:
            destination = os.path.join(cwd, extension, files) 
            if not os.path.exists(destination):
                shutil.move(os.path.join(cwd, files), os.path.join(cwd, extension))  
            print(extension, files)
        else:
            print('error')


directory_path = r'your path'  # Укажите путь к вашей директории|Specify the path to your directory
organize_files(directory_path)
