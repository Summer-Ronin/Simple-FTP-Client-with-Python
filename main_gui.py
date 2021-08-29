# Libs import 
from ftplib import FTP as ftp
from tkinter import *

# Define local attributes
# ftp_ip still hardcode tho
ftp_ip = "192.168.100.17"
ftp_usr = "testuser"
ftp_pwd = ""

# connect to local FTP server
ftp_client = ftp(ftp_ip)

def serverConnect():
    """
        Connect to local FPT server
    """

    ftp_client.login(user= ftp_usr, passwd = ftp_pwd)


def uploadFile(file):
    """
        Uploading the file to local FPT server
        Input: file - address of the file
        Output: Notification that file uploading successfully or not
    """

    # read file to send to byte
    file_stream = open(file,"rb") 

    # uploading the file       
    ftp_client.storbinary("{CMD} {FileName}".
                format(CMD="STOR",FileName=file),
                file_stream)     
    file_stream.close()                     
    print("After upload\n", ftp_client.retrlines("LIST"))
    ftp_client.close

def downloadFile(file):        
    """
        Downloading the file to local FPT server
        Input: file - address of the file
        Output: Notification that file downloading successfully or not
    """

    file_path = file
    file_name = file
    file_stream = open(file_path,"wb")   
        
    # read file to send to byte
    ftp_client.retrbinary('RETR {}'.format(file_name),
                file_stream.write, 1024)
    file_stream.close()                     
    print("Download OK")
    ftp_client.close

def gui_main():
    """
        GUI main config runs here
    """

    top = Tk()  
    # Change favicon
    photo = top.iconbitmap("assets/favicon.ico")

    # Setup gui title
    top.title("Simple Python FTP Client")

    # Menu bar config
    menubar = Menu(top)  
    file = Menu(menubar, tearoff=0)  
    file.add_command(label="New")  
    file.add_command(label="Close", command=top.quit)  
    
    file.add_separator()  
    
    file.add_command(label="Exit", command=top.quit)  
    
    menubar.add_cascade(label="File", menu=file)  
    edit = Menu(menubar, tearoff=0)  
    edit.add_command(label="Undo")  
    
    edit.add_separator()  
    
    edit.add_command(label="Cut")  
    edit.add_command(label="Copy")  
    edit.add_command(label="Paste")  
    edit.add_command(label="Delete")  
    edit.add_command(label="Select All")  
    
    menubar.add_cascade(label="Edit", menu=edit)  
    help = Menu(menubar, tearoff=0)  
    help.add_command(label="About")  
    menubar.add_cascade(label="Help", menu=help)  
    
    top.config(menu=menubar)  
    top.mainloop()  

def main():
    """ Main entry point of the app """
    serverConnect()

    # Display GUI
    gui_main()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()