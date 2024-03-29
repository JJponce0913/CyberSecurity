import zipfile

# Create a new ZIP file
with zipfile.ZipFile('example.zip', 'w') as zipf:
    # Add the CSRF token file to the ZIP file
    zipf.write('csrf_token.txt')