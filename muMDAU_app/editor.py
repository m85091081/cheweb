from flask import request , session , Response , render_template , Blueprint , url_for 
import os , hashlib , subprocess

peditor = Blueprint('peditor',__name__)
markdown = Blueprint('markdown',__name__)
@peditor.route('/')
def edit(username=None):
    if 'username' in session:
        return render_template('redit.html', username = session['username'])

@markdown.route('/submit' , methods=['GET','POST'])
def save():
    if request.method == "POST":
        argment = request.form['content']
        fil =  request.form['title']
        import datetime
        now = datetime.datetime.now()
        filen = now.strftime("%Y-%m-%d")+"-"+fil

        if not fil.strip():
            return "打標題啦,e04!"
        else:
            f = open('_posts/'+ filen  +'.markdown', 'wb+') 
            f.write(argment.encode('UTF-8'))
            f.close()
            ans = "file open"
            return "文章已經存在本地的_posts,重新整理即可在佇列中看到"

        
@markdown.route('/list/<listmd>', methods=['GET','POST'])
def markdownr(listmd):
    if request.method == "POST":
        f = open('./_posts/' + listmd)
        return f.read()
    else:
        return "你怎摸不去吃大便"


@peditor.route('/<lists>')
def jsonlist(lists):
    if 'username' in session:
        postpath = "./_posts"
            
        if os.path.exists(postpath) == True:
            directory = os.path.expanduser(postpath)
            data = []
            i = 0
            if os.listdir(directory) ==None:
                return("[""]")
            else:
                for f in os.listdir(directory):
                    if os.path.isfile(os.path.join(directory, f)):
                        i = i + 1
                        data.insert(i,f)
                    import json
                    jsondump = json.dumps(data,separators=( ',' , ':'))
                    resp = Response(response=jsondump,status=200, mimetype="application/json")
                    return(resp)
        else:
            os.makedirs(postpath)
        return 'OK'
    else:
        return redirect(ur_for(loginp))

