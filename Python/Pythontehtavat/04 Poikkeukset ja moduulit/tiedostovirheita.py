try:
    with open('luku1.txt', encoding='utf-8') as file_in:
        file = file_in.read()
        print(file)
except IOError:
    print("file not found or you dont have permission or you are in the wrong folder")
except: 
    print("Unknown error")
