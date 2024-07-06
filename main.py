import xml.etree.ElementTree as ET

INPUT_FILE_PATH = "./input.xml"
OUTPUT_FOLDER = "./smsy"
PHONE_OWNER = "Maciej" # used only to display proper message sender in text files

class Contact():
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Message():
    def __init__(self, date, readable_date, type, text):
        self.date = date
        self.readable_date = readable_date
        self.type = type
        self.text = text

def get_data_from_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    return root

def get_contacts(data):
    contacts = {}
    for sms in data.findall('sms'):
        number = sms.get('address')
        name = sms.get('contact_name')
        if number[0] == "+": number = number[3:]
        contact = Contact(name, number)
        contacts[contact] = 1
    return contacts

def get_messages_form_contact(data, contact):
    messages = []
    for sms in data.findall('sms'):
        address = sms.get('address')
        if address[0] == "+": address = address[3:]
        if address == contact.number:
            date = sms.get('date')
            readable_date = sms.get('readable_date')
            text = sms.get('body')
            type = sms.get("type")
            message = Message(date, readable_date, type, text)
            messages.append(message)
    return sorted(messages, key=lambda msg: msg.date)

def save_messages_to_file(output_folder, messages, contact, owner):
    file_name = f"{contact.number}_{contact.name}".replace("/", "_")
    file_path = f"{output_folder}/{file_name}.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        last_date = 0
        for message in messages:
            day = message.readable_date[:8]
            if last_date != day:
                file.write(f"\t---({day})---\n\n")
                last_date = day
            if message.type == '2':
                file.write(f"{owner} ({message.readable_date})\n {message.text}\n\n")
            else:
                file.write(f"{contact.name} ({message.readable_date})\n {message.text}\n\n")

if __name__ == "__main__":
    data = get_data_from_xml(INPUT_FILE_PATH)
    contacts_list = get_contacts(data)
    for contact in contacts_list:
        messages = get_messages_form_contact(data, contact)
        save_messages_to_file(OUTPUT_FOLDER, messages, contact, PHONE_OWNER)