import os

def renamer():
    i=0 
    path = "C:\\Users\\HP\\OneDrive\\Desktop\\Renamer6\\img\\"
    for filename in os.listdir(path):
        names = f"pic {i}.jpg"
        src = path + filename
        dest = path + names

        os.rename(src,dest)
        i = i + 1

if __name__ == "__main__":
    renamer()