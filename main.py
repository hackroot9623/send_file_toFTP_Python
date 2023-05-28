import os
from ftplib import FTP
import subprocess

# FTP server credentials
ftp_host = 'HOST'
ftp_user = 'username'
ftp_pass = 'pass'


# Local directory containing files to upload
local_dir = '/home/localusername/local_folder'

# Remote directory to upload files to
remote_dir = '/FTP_DIR/'

# Connect to FTP server
ftp = FTP(ftp_host)
ftp.login(user=ftp_user, passwd=ftp_pass)

# Navigate to remote directory
ftp.cwd(remote_dir)

# Upload files from local directory
uploaded_files = []
for file_name in os.listdir(local_dir):
    file_path = os.path.join(local_dir, file_name)
    with open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {file_name}', file)
        uploaded_files.append(file_name)


# Close FTP connection
ftp.quit()

# Check if all files were uploaded successfully
if len(os.listdir(local_dir)) == len(uploaded_files):
    print("Los archivos se enviaron correctamente")
    # Create system prompt
    subprocess.call(['cmd.exe', '/c', 'echo Los archivos se enviaron correctamente.'])
else:
    print("No todos los archivos se enviaron correctamente")
