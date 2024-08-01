# SMS_Backup_to_text
## A program to convert sms backup to readable text documents

A short script that allows you to get all of your DMs from your phone and place them on a folder as text files containing whole conversations with every number you ever talked to. 
It requires an .xml file you get from third party app [**SMS Backup & Restore**](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=pl)

## How does it work?
1.  Download [**SMS Backup & Restore**](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=pl) on your phone and make an SMS backup .xml file, then put this file on your PC, preferably through Google Drive.
2.  Next change the following lines in main script to reflect your file names and folders
```python
  INPUT_FILE_PATH = "./input.xml" 
  OUTPUT_FOLDER = "./messages_out"
  PHONE_OWNER = "MyNameHere"
```
* **INPUT_FILE_PATH** - backup file you got from [**SMS Backup & Restore**](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=pl), it has to be in xml format  
* **OUTPUT_FOLDER** - folder where program will generate text files  
* **PHONE_OWNER** - only used for SMS display, helps determine who is talking to who
3. Execute the script with the command `python ./main.py`. Your messages will be saved in the **OUTPUT_FOLDER** and named according to your contact names.
  

  
