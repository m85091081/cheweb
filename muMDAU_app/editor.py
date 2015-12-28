from flask import request , session , Response , render_template , Blueprint , redirect , url_for
import os 

peditor = Blueprint('peditor',__name__)
markdown = Blueprint('markdown',__name__)
@peditor.route('/')
def edit(username=None):
    if 'username' in session:
        return render_template('redit.html', username = session['username'])

@markdown.route('/save' , methods=['GET','POST'])
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
            return "文章已經存在本地的_posts,重新整理即可在佇列中看到"

        
@markdown.route('/list/<listmd>', methods=['GET','POST'])
def markdownr(listmd):
    if request.method == "POST":
        f = open('./markdown/' + listmd)
        return f.read()
    else:
        return "你怎摸不去吃大便"


@markdown.route('/del/posts/<listmd>', methods=['GET','POST'])
def delposts(listmd):
    if request.method == "POST":
        filepath = './_posts/' + str(listmd)
        os.remove(filepath)
        return "OK"
    else:
        return "你怎摸不去吃大便"


@markdown.route('/listed/<listposed>', methods=['GET','POST'])
def markdownrp(listposed):
    if request.method == "POST":
        f = open('./blog/_posts/'+ listposed)
        return f.read()
    else:
        return "在try我的後台嘛？你怎摸不去吃大便"

@peditor.route('/<lists>')
def jsonlist(lists):
    if 'username' in session:
        if lists == "page" :
            postpath = "./markdown"
        else:
            postpath = "./blog/_posts"
            
        if os.path.exists(postpath) == True:
            directory = os.path.expanduser(postpath)
            data = []
            i = 0
            if os.listdir(directory) ==None:
                return("[""]")
            else:
                print(len(os.listdir(directory)))
                for f in os.listdir(directory):
                    if os.path.isfile(os.path.join(directory, f)):
                        i = i + 1
                        data.insert(i,f)
                        print()
                    import json
                    jsondump = json.dumps(data,separators=( ',' , ':'))
                    resp = Response(response=jsondump,status=200, mimetype="application/json")
                return(resp)
        else:
            os.makedirs(postpath)
        return 'OK'
    else:
        return redirect(url_for("loginp"))

