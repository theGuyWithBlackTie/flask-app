import os
import requests
import html2text

while True:
    print("What would you like to do?\n1. Upload file(s) or directory\n2. Compute TF-IDF for string\nEnter 1 or 2.")

    user_input = int(input())

    if user_input == 1: # uploading directory or file
        print('Enter directory path or file path')
        path = str(input())

        if os.path.isdir(path): # entered directory path
            file_list = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
            
            files = []
            for file in file_list:

                if file.split('.')[1] != 'txt':
                    continue

                file_path = os.path.join(path, file)
                file_tuple= ('file', (file, open(file_path, 'rb'), 'text/plain'))
                files.append(file_tuple)

        elif os.path.isfile(path): # entered file path
            file_name = path.split('/')[-1]

            if file_name.split('.')[1] != 'txt':
                continue

            files = {'file': (file_name, open(path, 'rb'), 'text/plain')}
        
        body, content_type = requests.models.RequestEncodingMixin._encode_files(files, {})

        data = body
        headers = {
                    "Content-Type": content_type
                }
        endpoint = "http://localhost:5000/upload"
        response = requests.post(endpoint, data=data, headers=headers)
        print(
                html2text.html2text(response.text).split('\n')[0].strip('# ')
            )
        print('\n\n')


    elif user_input == 2:
        print('Enter the string:')
        input_text = input()

        data = {"text_field": input_text}

        endpoint = "http://localhost:5000/tf-idf"
        response = requests.post(endpoint, data=data)

        print(html2text.html2text(response.text).split('\n'))
        result_text = html2text.html2text(response.text).split('\n')

        to_print_text = result_text[0].strip('# ')
        print('\nFile Name: TF-IDF score')
        for index in range(1, len(result_text)):
            if index%4 == 0:
                print(to_print_text)
                to_print_text = result_text[index].strip('# ')
                continue
            to_print_text = to_print_text+" "+result_text[index].strip('# ')
        print('\n\n')

    else:
        exit()