import os

from pyramid.paster import get_app
from pyramid.paster import get_appsettings


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(here, 'production.ini')

    app = get_app(config, 'main')
    settings = get_appsettings(config, 'main')

    if 'OPENSHIFT_PYTHON_IP' in os.environ:
        ip = os.environ['OPENSHIFT_PYTHON_IP']
        port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
    else:
        ip = '0.0.0.0'                                          #localhost
        port = 6543


# Waitress (remember to include the waitress server in "install_requires" in the setup.py)
    from waitress import serve
    print("Starting Waitress Server on http://{0}:{1}".format(ip, port))
    serve(app, host=ip, port=port, threads=50)

#Simple Server
    # from wsgiref.simple_server import make_server
    # print("Starting Simple Server on http://{0}:{1}".format(ip, port))
    # server = make_server(ip, port, app)
    # server.serve_forever()

# Cherrypy server (remember to include the cherrypy server in "install_requires" in the setup.py)
#     from cherrypy import wsgiserver
#     print("Starting Cherrypy Server on http://{0}:{1}".format(ip, port))
#     server = wsgiserver.CherryPyWSGIServer((ip, port), app, server_name='Server')
#     server.start()


#Running 'production.ini' method manually.  I find this method the least compatible with Openshift since you can't
#easily start/stop/restart your app with the 'rhc' commands. Mabye somebody can suggest a better way :)

# #Don't forget to set the Host IP in 'production.ini'.  Use 8080 for the port for Openshift
# You will need to use the 'pre_build' action hook(pkill python) so it stops the existing running instance of the server on OS
# You also will have to set up another custom action hook so rhc app-restart, stop works.
# See Openshifts Origin User's Guide  ( I have not tried this yet)

#        print('Running pserve production.ini')
#        os.system("pserve production.ini &")

#this method works also.
    #import subprocess
    #subprocess.Popen(['pserve', 'production.ini &'])