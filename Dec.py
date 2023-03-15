import os
import requests
from cryptography.fernet import Fernet
import time

# Define the folder to decrypt
folder_to_decrypt = '/path/to/folder'

# Create a Fernet object
f = None

# Loop forever
while True:
    # Send a GET request to the remote server to check for a decryption key
    response = requests.get('https://example.com/decryption_key')

    # If a key was found, decrypt the folder
    if response.status_code == 200:
        # Get the key from the response
        key_bytes = response.content

        # Create a Fernet object with the key
        f = Fernet(key_bytes)

        # Walk through all the files in the folder and decrypt them
        for root, dirs, files in os.walk(folder_to_decrypt):
            for filename in files:
                # Open the file to decrypt
                with open(os.path.join(root, filename), 'rb') as f_in:
                    # Read the contents of the file
                    data = f_in.read()

                # Decrypt the contents of the file
                decrypted_data = f.decrypt(data)

                # Write the decrypted contents back to the file
                with open(os.path.join(root, filename), 'wb') as f_out:
                    f_out.write(decrypted_data)

        # Delete the key file
        os.remove('path/to/decryption_key')

        # Reset the Fernet object
        f = None

    # Sleep for 1 minute before checking again
    time.sleep(60)
