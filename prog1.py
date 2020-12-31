import os
all_files=os.listdir()
for file in all_files:
    if file.endswith('.pdf'):
        # store this file on S3
        print(file)
