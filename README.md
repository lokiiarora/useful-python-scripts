## Some useful python scripts

### Google Sheets to be used as a database

Head over to your Google API Console from <a href="https://console.developers.google.com" target="_blank">here</a>
Create a Project and switch to the project and head over to the Google APIs library and enable Google Drive API. 

You should have something like this : 
![Screenshot1][ss1]

Click on create Credentials and select Web Server and check on Application Data and create a service account name and click on continue to select role , which would be as an editor and then you will get a generated JSON, which is your secret file , place it in your app directory.

Now , go to your google sheet click on share and go back to your client secret , and copy the client email and give **edit permissions to this email address only !**

You are good to go !

[ss1]: https://lh6.googleusercontent.com/KNQmQchFesJHR8TAvZufq5H6zNhoQEvTUxb36J0bYu-wsYHRLfgJ2TZzHU9eQ-siFvLSx77SQszUsOg=w1306-h717-rw "Screenshot1"
