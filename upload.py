from ftplib import FTP

ftp_ip = "192.168.100.17"
ftp_usr = "testuser"
ftp_pwd = ""

# Create a client using defined ip address
ftp_client = FTP(ftp_ip)

# Connect with FileZilla server
ftp_client.login(user= ftp_usr, passwd = ftp_pwd)

# Listing all files in shared folder
print(ftp_client.retrlines('LIST'))

# UPLOADING PART

# read file to send to byte
file_stream = open("test_upload.txt","rb") 

# send the file       
ftp_client.storbinary("{CMD} {FileName}".
               format(CMD="STOR",FileName="test_upload.txt"),
               file_stream)     
file_stream.close()                     
print("after upload\n", ftp_client.retrlines("LIST"))
ftp_client.close