# Internal dependencies (should ship with python)
import webbrowser                               # Used to open a browser tab

# third party dependencies (need to be installed via pip)
from livereload import Server                   # Used to livereload pages in browser
from ezcv.core import generate_site             # Used to generate the static html pages
from flask import render_template, Flask        # Used to setup a running wsgi/http server
from jinja2.exceptions import TemplateNotFound  # Used to except template errors raised when a page doesn't exist



# Setup global variables
PORT = 5000 # The port to open flask to
template_dir = 'site' # The folder you want to export your site to in this case /site

## Configure the flask app
app = Flask(__name__, static_url_path='', static_folder=template_dir,  template_folder=template_dir) 
### These are a security risk, if you intend to use this server in prod remove the next two lines
app.config["DEBUG"] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    """display the homepage"""
    return render_template("index.html")

@app.route('/<path>')
def static_file(path:str):
    """Takes in a path and tries to return the template file with that title
    So if a user types in /test then it will try to find a template called test.html

    Parameters
    ----------
    path : str
        The path the user puts in the browser
    """
    try: # look for a page
        if not path.endswith(".html"):
            return render_template(f"{path}.html")
        else: # If path ends with .html NOTE: This conditional is also a security risk, remove in production
            return render_template(path)
    except TemplateNotFound:
        try: # Try to look for a 404 page
            return render_template("404.html")
        except TemplateNotFound: # If no 404 page exists, return a generic 404 page
            return """<div style='font-size: XXX-large;text-align: center;'>
            <h1>404 page not found</h1>
            </br>
            <button onclick='history.go(-1)'> Click to go back</button>
            </div>"""

def open_in_browser():
    """Opens localhost:{port} in whichever browser is installed"""
    browser_types = ["chromium-browser", "chromium", "chrome", "google-chrome", "firefox", "mozilla", "opera", "safari"] # A list of all the types of browsers to try
    for browser_name in browser_types:   # Look for which browser is installed
        try:
            webbrowser.get(browser_name) # Search for browser
            break                        # Browser has been found
        except webbrowser.Error:         # Browser wasn't found
            continue
    webbrowser.open(f"http://localhost:{PORT}", new=2) # Open the preview in the browser


if __name__ == '__main__':
    generate_site(output_folder=template_dir)                                         # Generate the site initially
    open_in_browser()                                                                 # Open the browser
    server = Server(app)                                                              # Initialize the livereload server
    server.watch('images/*', lambda: generate_site(output_folder=template_dir))       # Watch for changes in the images folder
    server.watch('*.yml', lambda: generate_site(output_folder=template_dir))          # Watch for changes in the yml files
    server.watch('content/*/*.md', lambda: generate_site(output_folder=template_dir)) # watch for changes in the markdown files
    server.serve(port=PORT)                                                           # Start the server