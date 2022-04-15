# Internal dependencies (should ship with python)
from typing import Callable         # Used to type hint function objects

# third party dependencies (need to be installed via pip)
import werkzeug.serving             # Used to setup the wsgi serving
from ezcv.core import generate_site # Used to generate the static html pages

def wsgi_app(environ:dict, start_response:Callable) -> list[str]:
    """The definition of what the wsgi app should do
    in this case it simply serves the files in /site

    Parameters
    ----------
    environ : dict
        The content of the request/environment

    start_response : Callable
        The function used to start the HTTP response

    Returns
    -------
    list[str]
        Return a list of a string that will be sent to the client that is the content of the http response
    """
    # Response/environ variables: https://www.toptal.com/python/pythons-wsgi-server-application-interface
    # http headers: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
    try:
        if environ["PATH_INFO"] == "/":
            start_response('200 OK', [('Content-Type', 'text/html')])
            with open("site/index.html", "r") as f:
                return [f.read().encode()]

        # CSS/JS/HTML
        elif environ["PATH_INFO"].endswith(".html"):
            start_response('200 OK', [('Content-Type', 'text/html')])
            with open("site" + environ["PATH_INFO"], "r") as f:
                return [f.read().encode()]
        
        elif environ["PATH_INFO"].endswith(".css"):
            start_response('200 OK', [('Content-Type', 'text/css')])
            with open("site" + environ["PATH_INFO"], "r") as f:
                return [f.read().encode()]
        elif environ["PATH_INFO"].endswith(".js"):
            start_response('200 OK', [('Content-Type', 'text/js')])
            with open("site" + environ["PATH_INFO"], "r") as f:
                return [f.read().encode()]

        # Images
        elif environ["PATH_INFO"].endswith(".jpg") or environ["PATH_INFO"].endswith(".jpeg"):
            start_response('200 OK', [('Content-Type', 'image/jpeg')])
            with open("site" + environ["PATH_INFO"], "rb") as f:
                return [f.read()]

        elif environ["PATH_INFO"].endswith(".png"):
            start_response('200 OK', [('Content-Type', 'image/png')])
            with open("site" + environ["PATH_INFO"], "rb") as f:
                return [f.read()]

        #fonts

        elif environ["PATH_INFO"].endswith(".woff2") or environ["PATH_INFO"].endswith(".woff") or environ["PATH_INFO"].endswith(".ttf"):
            start_response('200 OK', [('Content-Type', 'image/png')])
            with open("site" + environ["PATH_INFO"], "rb") as f:
                return [f.read()]

        # Assume html
        else:
            print(environ['PATH_INFO'])
            start_response('200 OK', [('Content-Type', 'text/html')])
            with open(f"/site{environ['PATH_INFO']}.html", "r") as f:
                return [f.read().encode()]
    except:
        # When things can't be found
        start_response('404 Not Found', [('Content-Type', 'text/text')])
        return ["404 Not Found".encode()]


if __name__ == "__main__":
    generate_site("site") # Generate site
    werkzeug.serving.run_simple('localhost', 8080, wsgi_app, use_reloader=True, extra_files=["*.yml", "content/*/*.md"]) # Run server

