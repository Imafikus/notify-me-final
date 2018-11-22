def make_html(info, site_url):
    """
    Make HTML with info about the changes and the site_url for accessibility
    """
    html_start = """
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>\n
        """
    html_end = """
        </body>
        </html>
        """
    html_site_url = "<h1> Site URL: " + site_url + "</h1>\n"
    html_start += html_site_url 
    
    for line in info:
        html_start += "<h5>" + line + "</h5>\n" 
    
    html_start +=  html_end

    return html_start
    