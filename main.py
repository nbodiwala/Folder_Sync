import csv
from subprocess import call
from config import csv_path, recipient_list_path
import win32com.client
import psutil


def generate_recipient_list():
    txt = open(recipient_list_path, 'r')
    lines = txt.readlines()

    recipients = ''
    for line in lines:
            line = line.rstrip()
            recipients += line + '; '

    return recipients

def is_program_running(program):
    if program in (i.name() for i in psutil.process_iter()):
        return True

with open(csv_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        source = line['Source']
        destination = line['Destination']

        call(['robocopy', source, destination, '/MIR', '/S', '/XD', '/XO', '*_archive'])

# Create and send Folder Sync Status Email
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = generate_recipient_list()
mail.To = 'nirav.bodiwala@femoran.com'
mail.Subject = 'Folder Sync Process Has Successfully Run'
if not is_program_running('Dropbox.exe'):
     mail.Body = 'Warning: Dropbox.exe is not running. Verify files are being synced with the cloud'
mail.Send()
