import os



def create_file(filename):
    try:
            file = open(filename, "w")
            file.write("This is the write command")
            print("File" + filename +"created successfully")
    except:
        print("Error :could not create file" + filename)


def read_file(filename):
    file =open(filename,'r')
    f = file.read()
    print("Contents of file",f,"\n\n")
          


def append_file(filename,new_example):
    try:
        file =open(filename,'a')
        file.write(new_example)
        print("Appended the data")
    except:
        print("Error : could not append the data")


def read_file(filename):
    file =open(filename,'r')
    f = file.read()
    print("Contents of file",f,"\n\n")
   


def rename_file(filename,new_example):
    os.rename(filename,new_example)
    print("Filename",filename,"changes to",new_example)
    
def read_file(new_filename):
    file =open(new_filename,'r')
    f= file.read()
    print("Contents of file",f,"\n\n")
def delete_file(filename):
    try:
        os.remove(filename)
        print("File"+filename+"deleted successfully")
    except:
        print("error:could not delete the file")
    




if __name__=='__main__':
    filename = "asch.txt"
    new_filename = "new_example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename,"This is some additional text.\n")
    read_file(filename)
    rename_file(filename,new_filename)
    read_file(new_filename)
    delete_file(new_filename)
         





