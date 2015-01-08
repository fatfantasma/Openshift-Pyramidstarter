from pyramid.config import Configurator
import logging


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config_logging()



    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()



def config_logging():
    import logging.config


    log_ini = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s [%(levelname)-8s] %(name)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler(stream=None)",
                "level": "DEBUG",
                "formatter": "simple"                                                   #key name of our formatter
            }
        },
        "loggers": {
            "": {
                "handlers": ["console"],                    #["console", "mail", "standard_file", "rotating_file", etc]
                "level": "DEBUG",
                "propagate": True
            }
        }
    }



    logging.config.dictConfig(log_ini)                       #configure log


    return



