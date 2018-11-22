# Notify me

Simple program to let me know if something has been added on websites of 
my courses in college.

## Dependencies
- [requests_html](https://html.python-requests.org/) library for Python 3

# Usage

## Data for scraping

Course names and urls are kept in *urls.json* file. Current versions of html pages are kept in *sites* folder. 

If you don't have either *urls.json* file or *sites* folder you will get the proper message.

### **Sites folder**
Keeps the current versions of the sites, whenever the site info is changed, target file in the folder is updated accordingly.

### Urls file
Keeps the info about the course (course name and course url), it's used for scraping and making files in *sites* folder. File is in JSON format.

## Running the program
If you want to manually run the program, you should do that by executing *run_script.sh* file.  
Recommended usage of the program is to put it into the [cron task scheduler](https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/) to run on the given interval, so you don't have to run it manually.

### **Important**

You must enter your mail credentials in *utils/mail.py* file in order to run the program. For security, it's encouraged that you use mail made only for this.  

**Program is tested only with gmail accounts.**