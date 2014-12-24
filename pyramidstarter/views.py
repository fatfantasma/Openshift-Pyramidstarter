from pyramid.view import view_config

import logging
log = logging.getLogger(__name__)

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):

    log.debug("This is a log.debug test")
    log.info("This is a log.info test")
    log.warn("This is a log.warn test")
    log.error("This is a log.error test")
    log.critical("This is a log.critical test")

    return {'project': 'Pyramidstarter'}
