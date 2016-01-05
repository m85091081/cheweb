from muMDAU_app import app
from flask import render_template, Markup , Blueprint
import markdown ,time,os

main = Blueprint('main',__name__)

@main.route('/')
def index():
    nowtime = time.strftime('%Y')
    pastime = int(nowtime) - 1
    pastpath = "./markdown/"+str(pastime)
    print(pastpath)
    if os.path.exists(pastpath) == True:
        directory = os.path.expanduser(pastpath)
        data = []
        i=0
        if os.listdir(directory)==None:
            pastdata = " "
        else:
            filel = os.listdir(directory)
            filel.sort(reverse=True)
            for f in filel:
                if os.path.isfile(os.path.join(directory,f)):
                    fstr = str(f).split("-",2)
                    nowm = time.strftime('%m')
                    if int(nowm) - 6 >=  0:
                        if int(fstr[0]) == int(nowtime):
                            if int(fstr[1]) - 6  >= 0:
                                i = i+1
                                with open("./markdown/"+str(pastime)+"/"+str(f),'r') as fil:
                                    content = fil.readline()
                                    content = content.replace("title:","")
                                data.insert(i,content)
                    else:
                        if int(fstr[0]) == int(nowtime):
                            if int(fstr[1]) - 6  >= 0:
                                i = i+1
                                with open("./markdown/"+str(pastime)+"/"+str(f),'r') as fil:
                                    content = fil.readline()
                                    content = content.replace("title:","")
                                data.insert(i,content)
                        elif int(fstr[0]) == int(nowtime)- 1:
                            nowm = time.strftime('%m')
                            if int(fstr[1]) - 6 - int(nowm) > 0 :
                                i = i+1
                                with open("./markdown/"+str(pastime)+"/"+str(f),'r') as fil:
                                    content = fil.readline()
                                    content = content.replace("title:","")
                                    data.insert(i,content)
                            
            pastdata = data
    else:
        os.makedirs(pastpath)

    return render_template('index.html',**locals())

@app.route('/about')
def about():
    with open("./markdown/about.md","r") as f:
        content =  list(f)
        content = ''.join(content)
    content = Markup(markdown.markdown(content))
    return render_template('views.html',**locals())

@app.route('/teach')
def teach():
    return render_template('table.html')
