# -*- coding: utf-8 -*-
"""File Permissions Changer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NZkV8es6mJrZ9jQ-h9pgJh6mWAWSsLFx
"""

import os

# Specify the path to your file
file_path = '/content/file_permissions.py'

# Set permissions to rwxrwxr-x (775)
try:
    os.chmod(file_path, 0o775)
    print(f"Permissions for '{file_path}' have been set to rwxrwxr-x (775) successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")