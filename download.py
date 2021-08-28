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

#DONNLOAD PART

file_path = "sample.txt"
file_name = "sample.txt"
file_stream = open(file_path,"wb")   
     
 # read file to send to byte
ftp_client.retrbinary('RETR {}'.format(file_name),
               file_stream.write, 1024)
file_stream.close()                     
print("Download OK")
ftp_client.close