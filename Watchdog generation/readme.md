# Watchdog Generation

This system was an exploration of how you can manually re-generate the static html when content pages change, this does not implement a `http` server or live reloading.

## Getting started

There are a few things you will want to do to get started

1. Add your name to the `config.yml` file
2. install all prerequisites using `pip install -r requirements.txt` or install `ezcv` and `watchdog` manually through pip using `pip install ezcv` and `pip install watchdog`
3. Create your content, you can see the [ezcv documentation](https://ezcv.readthedocs.io/en/latest/usage/) for details
4. Run `python rebuilder.py` and open the file path to the `index.html` in the `/site` folder in your browser

## Additional notes

There are **no security features enabled**, this is **not production ready** and nor do I intend to make it. It just gives you the barebones you need to build an app using `ezcv` as a backend for the html. Getting the site to production readyness is **your responsibility** and I am not responsible for any issues you incur while using this.

The `wsgi` setup is incredibly basic and all it does by default is:

1. Take in a request and return the content of static files with the correct content types for (note any capitalized paths will just break like PNG): 
   - html files
   - image files; jpg, png, jpeg
   - Other web files; css, js
2. If none of the accepted file types are requested a 404 is returned