from pyramid.config import Configurator
import logging

log = logging.getLogger(__name__)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """


    config_logging()

    log.debug("This is a log.debug test")
    log.info("This is a log.info test")
    log.warn("This is a log.warn test")
    log.error("This is a log.error test")
    log.critical("This is a log.critical test")

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
        "disable_existing_loggers": True,
        "formatters": {
            "simple": {
                "format": "%(asctime)s [%(levelname)-8s] %(name)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
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



