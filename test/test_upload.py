import io
import requests

'''
This test case tests upload functionality with the page content.
'''
def test_upload(test_client, captured_templates):
    file_name = "fake_file.txt"
    data = {
        'file': (io.BytesIO(b'some inital text data'), file_name)
    }
    response = test_client.post('/upload', data=data)
    assert response.status_code == 200

    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == 'index.html'
    assert "info" in context
    assert context["info"] == "Files Uploaded: "+file_name


'''
On uploading two .txt files, it should be uploaded with OK status.
Along with it, it also tests page content that is shown on the page after uploading
'''
def test_multiple_file_upload(test_client, captured_templates):
    first_file_name = "multiple_file_test_one.txt"
    second_file_name= "multiple_file_test_two.txt"

    file_list = []

    file_list.append(('file', (first_file_name, (io.BytesIO(b'First file in multiple file upload test')), 'text/plain')))
    file_list.append(('file', (second_file_name, (io.BytesIO(b'Second file in multiple file upload test')), 'text/plain')))

    body, content_type = requests.models.RequestEncodingMixin._encode_files(file_list, {})
    data = body
    headers = {"Content-Type": content_type}

    response = test_client.post('/upload', data=data, headers=headers)
    assert response.status_code == 200

    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert context["info"] == "Files Uploaded: "+first_file_name+" "+second_file_name

'''
This test case tests uploading multiple files but atleast one of them is not a .txt file.
It should return status code as 207 which states, partial upload was succesfull, that is the file(s) without a .txt extension would not be uploaded.
The page would show only file's name as being uploaded which is .txt file.
'''
def test_mix_files_upload(test_client, captured_templates):
    first_file_name = "mix_file_test_one.txt"
    second_file_name= "mix_file_test_two.jpg"

    file_list = []
    file_list.append(('file', (first_file_name, (io.BytesIO(b'First file in multiple file upload test')), 'text/plain')))
    file_list.append(('file', (second_file_name, (io.BytesIO(b'Second file in multiple file upload test')), 'text/plain')))

    body, content_type = requests.models.RequestEncodingMixin._encode_files(file_list, {})
    data = body
    headers = {"Content-Type": content_type}

    response = test_client.post('/upload', data=data, headers=headers)
    assert response.status_code == 207

    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert "info" in context
    assert context["info"] == "Files Uploaded: "+first_file_name



'''
Both files being uploaded are not .txt files. Hence no files would be uploaded.
The page content would show same information.
'''
def test_no_txt_file_upload(test_client,captured_templates):
    first_file_name = "mix_file_test_one.jpg"
    second_file_name= "mix_file_test_two.jpg"

    file_list = []
    file_list.append(('file', (first_file_name, (io.BytesIO(b'First file in multiple file upload test')), 'text/plain')))
    file_list.append(('file', (second_file_name, (io.BytesIO(b'Second file in multiple file upload test')), 'text/plain')))

    body, content_type = requests.models.RequestEncodingMixin._encode_files(file_list, {})
    data = body
    headers = {"Content-Type": content_type}

    response = test_client.post('/upload', data=data, headers=headers)
    assert response.status_code == 409
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert "info" in context
    assert context["info"] == "No files are uploaded"
