# Libs import 
from ftplib import FTP as ftp
import ftplib
from re import L
from rich.console import Console
from rich.table import Table

# Define local attributes
# ftp_ip still hardcode tho
# ftp_ip = "192.168.100.5"
def connect():
    ftp_usr = "testuser"
    ftp_pwd = ""
    # login_token = False
    while(True):
        ftp_ip = input("Nhập địa chỉ ip host: ")
        # connect to local FTP server
        try:
            ftp_client = ftp(ftp_ip)
            ftp_client.login(user= ftp_usr, passwd = ftp_pwd)
            print("Đăng nhập thành công!")
            command(ftp_client)
            break
            # login_token = True
        except ftplib.all_errors as e:
            print("Lỗi kết nối! Kiểm tra lại địa chỉ host",e)


def uploadFile(file,ftp_client):
    """
        Uploading the file to local FPT server
        Input: file - address of the file
        Output: Notification that file uploading successfully or not
    """

    # read file to send to byte
    file_stream = open(file,"rb") 

    # uploading the file     
    try:
        ftp_client.storbinary("{CMD} {FileName}".
                format(CMD="STOR",FileName=file),
                file_stream)     
        file_stream.close()                     
        print("After upload\n", ftp_client.retrlines("LIST"))
        ftp_client.close
    except  ftplib.all_errors as e:
        errorcode_string = str(e).split(None, 1)
        if errorcode_string[0] == "550":
            print(errorcode_string[1], "Sai tên file hoặc file không tồn tại trong thư mục")
        else: print("Lỗi upload: ",e)

def downloadFile(file,ftp_client):        
    """
        Downloading the file to local FPT server
        Input: file - address of the file
        Output: Notification that file downloading successfully or not
    """
    # file =input("Nhập tên file cần download: ")

    file_path = file
    file_name = file
    file_stream = open(file_path,"wb")   
        
    # read file to send to byte
    ftp_client.retrbinary('RETR {}'.format(file_name),
                file_stream.write, 1024)
    file_stream.close()                     
    print("Download OK")
    ftp_client.close

def command(ftp_client):
    """ Main entry point of the app """
    table = Table("Hãy chọn 1 chức năng sau")
    table.add_column("Chức năng", justify="justify", style="bright_yellow", no_wrap=True)
    
    table.add_row("Ví dụ bạn muốn upload file, ", "1. Hiển thị file trong server")
    table.add_row("nhập 1 vào console và Enter để tiếp tục", "2. Upload file lên server")
    table.add_row("", "3. Download file từ server")
    table.add_row("", "4. Thoát khỏi chương trình")
    
    console = Console()
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
                """
                Uploading the file to local FPT server
                Input: file - address of the file
                Output: Notification that file uploading successfully or not
                """
                file = input("Nhập tên file bạn muốn upload: ")
                uploadFile(file,ftp_client)
                command_numb = True

            elif(int(command_numb) == 3):

                file =input("Nhập tên file cần download: ")
                downloadFile(file,ftp_client)
                command_numb = True
                
            elif(int(command_numb) == 4):
                exit_code = True
                console.print("Chào tạm biệt và hẹn gặp lại!", style="cyan2")
                exit()

def main():
    connect()
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()