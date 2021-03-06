from muMDAU_app import app 
import logging,setting
from muMDAU_app.index import main
from muMDAU_app.editor import peditor
from muMDAU_app.editor import markdown
app.secret_key = setting.yourkey
from werkzeug.contrib.fixers import ProxyFix 
app.wsgi_app = ProxyFix(app.wsgi_app)
app.register_blueprint(peditor, url_prefix='/edit')
app.register_blueprint(markdown, url_prefix='/md')
app.register_blueprint(main)


if __name__ == "__main__":
    print("0MuMDAU Server Run on 127.0.0.1:" + str(setting.port))
    if setting.debug == 0:
        debugB = False 
    else:
        debugB = True

    app.run(host="127.0.0.1",port=setting.port , debug=debugB)

