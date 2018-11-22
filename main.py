#!/bin/env python3

import difflib
import requests_html
import datetime

from os import listdir
from os.path import isfile, join

from utils.mail import send_mail
from utils.make_html import make_html
from utils.page_handling import *
from utils.helper_functions import *

SITES_PATH = os.path.dirname(__file__) + "/sites"
LOG_PATH = os.path.dirname(__file__) + "/log.txt"

def get_diff(old_text, new_text, site_url):
    """
    Return HTML of the diffs between the old_text and new_text.
    """
    print ("Get diff...")
    
    all_lines = []
    for line in difflib.unified_diff(old_text.splitlines(), new_text.splitlines(), n=0):
        all_lines.append(line)

    if all_lines == []:
        return None

    html = make_html(all_lines, site_url)
    return html

def main():

    check_if_directory_exists(SITES_PATH)

    all_courses_list = get_all_files(SITES_PATH)
    courses = get_links()
    
    for course in courses:
        #! IMPORTANT: .rstrip must be used, otherwise some sites won't display properly
        course_url = course["url"].rstrip()
        course_name = course["name"]
        
        if (course_name + ".html") in all_courses_list:
            path = os.path.join(SITES_PATH, course_name + ".html")
            
            old_text = open(path, "r").read()
            new_text = get_data(course_name, course_url)

            html = get_diff(old_text, new_text, course_url)
    
            if html is None:
                print(course_name, ": No changes for target file, aborting...")
            
            else:
                print(course_name, ": file changed")
                send_mail(html, "aleksatesicteske@gmail.com", course_name)
                
                #update target file in /sites folder
                path = os.path.join(SITES_PATH, course_name + ".html")
                write_to_file(path, new_text)
    
    print("Finished successfully,  wrapping up...")

if __name__ == "__main__":        

    with open(LOG_PATH, "w") as log:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write("Program started at: " + time + "\n")

    init_sites_folder()
    main()
    
