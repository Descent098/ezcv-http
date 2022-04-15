# EZCV HTTP
A repo with the various methods I tested to create several pieces of functionality:

1. Content reloading (update the output when content is changed)
2. An http server into [ezcv](https://github.com/Descent098/ezcv)
3. Live reloading

All of these folders implement some, or all of these peices of functionality. They're documented here for posterity as well as a resource for learning various methods of implementing this functionality.

## Project breakdown

| Project name          | Required libraries                                           | Functionality implemented                      |
| --------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Flask ezcv livereload | [ezcv](https://github.com/Descent098/ezcv), [Flask](https://flask.palletsprojects.com/en/2.1.x/), [livereload](https://github.com/lepture/python-livereload) | Content reloading, http server, live reloading |
| Flask ezcv            | [ezcv,](https://github.com/Descent098/ezcv) [Flask](https://flask.palletsprojects.com/en/2.1.x/) | Content reloading, http server                 |
| Watchdog Generation   | [ezcv](https://github.com/Descent098/ezcv), [watchdog](https://github.com/gorakhargosh/watchdog/) | Content reloading                              |
| WSGI Native Testing   | [ezcv](https://github.com/Descent098/ezcv), [werkzeug](https://werkzeug.palletsprojects.com/en/2.1.x/) | http server                                    |
| Socket Testing        | [ezcv](https://github.com/Descent098/ezcv)                   | http server                                    |

