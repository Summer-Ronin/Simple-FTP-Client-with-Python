# Libs import 
from ftplib import FTP as ftp
import ftplib
from re import L
from rich.console import Console
from rich.table import Table

# Define global attributes
console = Console()

def connect():
    """
        ===================================================
		Connect to server using your Ipv6 address
        - If everything is OK, it will run on with command and its parameter ftp_client
        - ftp_user is user you register in FileZilla 
        - ftp_pwd is optional, if you have password, put it in
		===================================================
    """

    ftp_user = "testuser"
    # ftp_pwd = ""
    # login_token = False
    while(True):
        console.print("Nhập địa chỉ ip host: ", style="#1BFF00")
        ftp_ip = input()
        # connect to local FTP server
        try:
            ftp_client = ftp(ftp_ip)
            ftp_client.login(user= ftp_user)
            print("Đăng nhập thành công!")
            command(ftp_client)
            break
            # login_token = True
        except ftplib.all_errors as e:
            console.print("Lỗi kết nối! Kiểm tra lại địa chỉ host", e, style="red")


def uploadFile(file,ftp_client):
    """
        ===================================================
		Uploading the file to local FPT server
        Input: file - address of the file
        Output: Notification that file uploading successfully or not
		===================================================
    """
    
    try:
        """
            ===================================================
            Trying to open file and bind to file_stream
            Catch error when:
                - File cannot be found
                - File cannot be uploaded
            ===================================================
        """

        file_stream = open(file,"rb") 
    except IOError:
        console.print("Error: Xin lỗi,", file, "không tồn tại.", style="red")

    # uploading the file     
    try:
        ftp_client.storbinary("{CMD} {FileName}".
                format(CMD="STOR",FileName=file),
                file_stream)     
        file_stream.close()      
        console.print("Upload thành công", style="cyan")               
        print("Folder sau khi upload\n", ftp_client.retrlines("LIST"))
        ftp_client.close
    except  ftplib.all_errors as e:
        console.print(e, style="red")

def downloadFile(file,ftp_client):        
    """
        ===================================================
        Downloading the file to local FPT server
        Input: file - address of the file
        Output: Notification that file downloading successfully or not
        ===================================================
        
    """
    # file =input("Nhập tên file cần download: ")

    file_path = file
    file_name = file
    file_stream = open(file_path,"wb")   
        
    # read file to send to byte
    ftp_client.retrbinary('RETR {}'.format(file_name),
                file_stream.write, 1024)
    file_stream.close()                     
    console.print("Download thành công", style="cyan2")
    ftp_client.close

def command(ftp_client):
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
        """
        ===================================================
        COMMAND NUMB INPUT ERROR HANDLING
        - Invalid numbers
        - Invalid input with different types
        ===================================================
        """
        if(int(command_numb) > 4 or int(command_numb) <= 0):
            console.print("Vui lòng chỉ nhập số có trong bảng:", style="spring_green3")
            command_numb = input()
            
        elif(command_numb == True):
            console.print("Nhập vào số bạn muốn thực thi:", style="spring_green3")
            command_numb = input()

        else:
            """
            ===================================================
            ################### CHECK SELECTION ##############
            ===================================================
            """
            if(int(command_numb) == 1):
                # Listing all files in shared folder
                console.print("Chi tiết folder", style="cyan2")
                print(ftp_client.retrlines('LIST'))
                command_numb = True
                         
            elif(int(command_numb) == 2):
                console.print("Nhập tên file bạn muốn upload: ", style="cyan2")
                up_file = input()
                uploadFile(up_file, ftp_client)
                command_numb = True

            elif(int(command_numb) == 3):
                console.print("Nhập tên file bạn muốn download: ", style="cyan2")
                down_file = input()
                downloadFile(down_file, ftp_client)
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