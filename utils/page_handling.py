from requests_html import HTMLSession
import os
import json

from utils.helper_functions import *


SITES_PATH = os.path.dirname(__file__) + "/../sites"
FILE_PATH = os.path.dirname(__file__) + "/../urls.json"

def get_links():
    """
    Get links for the pages from the url file
    """
    print("Get links...")

    check_if_file_exists(FILE_PATH)

    with open(FILE_PATH, encoding = "utf-8") as data_file:
        data = json.load(data_file)
    
    return list(data["sites"])    

def get_data(site_name, site_url, used_for_init = False):
    """
    Sends the request to the site and, if used_for_init is set to True, writes the
    site code into the html file in /sites
    """
    check_if_directory_exists(SITES_PATH)

    print("Get data for", site_name,"...")

    session = HTMLSession()
    res = session.get(site_url)

    #! exception to be added here
    res.encoding = "utf-8"

    data = res.text    

    if used_for_init:
        path = os.path.join(SITES_PATH, site_name+".html")
        file_ = open(path, "w+")
        file_.write(data)

    return data

def init_sites_folder():
    """
    Make a local copy of the current web pages we want to track 
    """
    print("Init sites folder...")
    
    courses = get_links()

    existing_courses = get_all_files(SITES_PATH)

    for course in courses:
        course_name = course["name"]

        if course_name + ".html" in existing_courses:
            print(course_name + ".html", "already exists, aborting...")
        else:    
            #! IMPORTANT: .rstrip must be called, otherwise some sites might not work.
            course_url = course["url"].rstrip()
            get_data(course_name, course_url, used_for_init=True)
