# Flask + ezcv

This project is an ezcv project integrated with Flask.

## Getting started

There are a few things you will want to do to get started

1. Add your name to the `config.yml` file
2. install all prerequisites using `pip install -r requirements.txt` or install `flask` and `ezcv` manually through pip using `pip install flask` and `pip install ezcv`
3. Create your content, you can see the [ezcv documentation](https://ezcv.readthedocs.io/en/latest/usage/) for details
4. Run `python routes.py` and go to [http://localhost:5000](http://localhost:5000) in your browser

## Additional notes

There are **no security features enabled**, this is **not production ready** and nor do I intend to make it. It just gives you the barebones you need to build an app using `ezcv` as a backend for the html. Getting the site to production readyness is **your responsibility** and I am not responsible for any issues you incur while using this.

The flask setup is incredibly basic and all it does by default is:
1. Proxy the homepage (`index.html`) to [http://localhost:5000](http://localhost:5000)
2. Take any paths and try to proxy them to webpages in `/site` (so [http://localhost:5000/test](http://localhost:5000/test) would look for a file called `test.html` in the `/site` folder and proxy that at [http://localhost:5000/test](http://localhost:5000/test))

This means that flask operates on **the built html files, not the jinja source files** since they have already been processed by `ezcv`.
