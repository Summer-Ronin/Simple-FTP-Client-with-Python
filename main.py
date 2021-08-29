# Libs import 
from ftplib import FTP as ftp
from re import L
from rich.console import Console
from rich.table import Table

# Define local attributes
# ftp_ip still hardcode tho
ftp_ip = "192.168.100.17"
ftp_usr = "testuser"
ftp_pwd = ""
console = Console()

# connect to local FTP server
ftp_client = ftp(ftp_ip)

ftp_client.login(user= ftp_usr, passwd = ftp_pwd)

def uploadFile(file):
    """
        Uploading the file to local FPT server
        Input: file - address of the file
        Output: Notification that file uploading successfully or not
    """
    
    try:
        """
            Trying to open file and bind to file_stream
            Catch error when:
                - File cannot be found
        """

        file_stream = open(file,"rb") 
    except IOError:
        console.print("Error: Xin lỗi,", file, "không tồn tại.", style="red")
        
        while IOError:
            console.print("Vui lòng nhập lại tên file:", style="cyan2")
            file = input()


    # uploading the file     
    try:
        ftp_client.storbinary("{CMD} {FileName}".
                format(CMD="STOR",FileName=file),
                file_stream)     
        file_stream.close()                     
        print("After upload\n", ftp_client.retrlines("LIST"))
        ftp_client.close
    
    except ftp_client.all_errors:
        console.print(str(e), style="red")

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

def terminalMain():
    table = Table("Hãy chọn 1 chức năng sau")
    table.add_column("Chức năng", justify="justify", style="bright_yellow", no_wrap=True)
    
    table.add_row("Ví dụ bạn muốn upload file, ", "1. Hiển thị file trong server")
    table.add_row("nhập 1 vào console và Enter để tiếp tục", "2. Upload file lên server")
    table.add_row("", "3. Download file từ server")
    table.add_row("", "4. Thoát khỏi chương trình")
    
    console.print(table)
    
    console.print("Nhập vào số bạn muốn thực thi:", style="spring_green3")
    command_numb = input()

    exit_code = False 

    while exit_code == False:
        # input command defined by user
        if(int(command_numb) > 4 or int(command_numb) <= 0):
            console.print("Vui lòng chỉ nhập số có trong bảng:", style="spring_green3")
            command_numb = input()

        elif(command_numb == True):
            console.print("Nhập vào số bạn muốn thực thi:", style="spring_green3")
            command_numb = input()

        else:
            # Check selection
            if(int(command_numb) == 1):
                # Listing all files in shared folder
                print(ftp_client.retrlines('LIST'))
                command_numb = True
                         
            elif(int(command_numb) == 2):
                file = input("Nhập tên file bạn muốn upload: ")
                uploadFile(file)
                command_numb = True

            elif(int(command_numb) == 3):
                downloadFile("sample.txt")
                command_numb = True
                
            elif(int(command_numb) == 4):
                exit_code = True
                console.print("Chào tạm biệt và hẹn gặp lại!", style="cyan2")
                exit()


def main():
    """ Main entry point of the app """
    terminalMain()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()