import os
def rename_files():
    file_list = os.listdir(r'/Users/faezrah/Documents/udacity/ud036/prank')
    print(file_list)
    saved_path = os.getcwd()
    print('Currrent working directory is '+saved_path)
    os.chdir(r'/Users/faezrah/Documents/udacity/ud036/prank')
    for file_name in file_list:
        print ('Old Name - '+file_name)
        print ('New Name - '+file_name.translate(None, '0123456789'))
        os.rename(file_name, file_name.translate(None, '0123456789'))
    os.chdir(saved_path)
rename_files()
