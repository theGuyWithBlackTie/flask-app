This repository contains flask framework based app which lets user to upload the documents and compute tf-idf on the user's input string. To run this repository code, `Python=3.8.3` is required.

To download all other packages, run `pip install requirements.txt`

### How to use?
Initally, download the code in zip format and extract all the contents. After extracting, the file structure would look like this:
```
root
|- server
   |- templates
      |- file_upload.html
      |- index.html
      |- tf_idf.html
   |- __init__.py
   |- app_config.py
   |- cache.py
   |- config.py
   |- routes.py
   |- tf_idf.py
   |- tfpipeline.py
|- storage
|- test
|- client.py
|- requirements.txt
|- run_server.py
```

**Every command on cmd are supposed to be run from `root` directory only.**

Follow the below given instructions:
1. First install all the required packages by running this on cmd: `pip install requirements.txt`. This will install, `flask`, `pytest`, `nltk`, `html2text` , `werkzeug`.

2. Now, we need to start the server which would accept the file uploads and compute the tf-idf scores. To start the server, run `python run_server.py`. The server will start on `http://127.0.0.1:5000/` by default. Copy this link and open in any of the browser.

3. Home user interface would look like this:
![](https://github.com/theGuyWithBlackTie/flask-app/blob/main/images/home.png)

4. You could upload the images by clicking on **Upload File(s)** button or you can compute theTF-IDF search by clicking on **Compute TF-IDF score**. Important point to note is, no TF-IDF will be computed if files are not present in the server.

5. Files upload UI looks like the following. Click on `Choose Files`, and select one or more files to be uploaded, and click `OK`.  **Server only accepts *.txt* extension files. Files that are not text files (or .txt) will not be uploaded.**
![](https://github.com/theGuyWithBlackTie/flask-app/blob/main/images/file%20upload.png)

6. Files that gets uploaded would be shown as below once upload is complete and you would be returned to homepage:
![](https://github.com/theGuyWithBlackTie/flask-app/blob/main/images/file%20upload%20done.png)

7. Click o `Compute TF-IDF score` button and enter the string and search the documents based on TF-IDF score. The UI would appear like below:
![](https://github.com/theGuyWithBlackTie/flask-app/blob/main/images/tf-idf%20compute.png)
