from muMDAU_app import app
from flask import render_template, Markup , Blueprint
import markdown ,time,os

main = Blueprint('main',__name__)

@main.route('/work')
def work():
    nowtime = time.strftime('%Y')
    pastime = int(nowtime) - 1
    postpath = "./work"
    if os.path.exists(postpath) == True:
        directory = os.path.expanduser(postpath)
        data = []
        content1 = []
        i=0
        a=0
        if os.listdir(directory)==None:
            pastdata = " "
        else:
            filel = os.listdir(directory)
            filel.sort(reverse=True)
            for f in filel:
                if os.path.isfile(os.path.join(directory,f)):
                    with open("./work/"+str(f),'r') as fil:
                        content = fil.readline()
                        content = content.replace("title:","")
                        data.insert(i,content)
                        content1.insert(i,fil.read())
                            
            pastdata = data
            contentdata = content1
    else:
        os.makedirs(postpath)

    return render_template('work.html',**locals())

@main.route('/goals')
def goals():
    nowtime = time.strftime('%Y')
    postpath = "./goals"
    if os.path.exists(postpath) == True:
        directory = os.path.expanduser(postpath)
        data = []
        content1 = []
        i=0
        dataa = []
        contentt1 = []
        a=0
        if os.listdir(directory)==None:
            pastdata = " "
        else:
            filel = os.listdir(directory)
            filel.sort(reverse=True)
            for f in filel:
                if os.path.isfile(os.path.join(directory,f)):
                    fstr = str(f).split("-",2)
                    if int(fstr[0]) == int(nowtime):
                        i = i+1
                        with open("./goals/"+str(f),'r') as fil:
                            content = fil.readline()
                            content = content.replace("title:","")
                            data.insert(i,content)
                            content1.insert(i,fil.read())
                    else:
                        a = a+1
                        with open("./goals/"+str(f),'r') as filipt:
                            contentt = filipt.readline()
                            contentt = contentt.replace("title:","")
                            dataa.insert(i,contentt)
                            contentt1.insert(i,filipt.read())
                            
            pastdata = data
            contentdata = content1
            olddata = dataa
            oldcontent = contentt1
    else:
        os.makedirs(postpath)

    return render_template('goals.html',**locals())

@main.route('/')
def index():
    nowtime = time.strftime('%Y')
    pastime = int(nowtime) - 1
    postpath = "./posts"
    if os.path.exists(postpath) == True:
        directory = os.path.expanduser(postpath)
        data = []
        content1 = []
        dataa = []
        contentt1 = []
        i=0
        a=0
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
                            if int(fstr[1]) - 6  <= 0:
                                i = i+1
                                with open("./posts/"+str(f),'r') as fil:
                                    content = fil.readline()
                                    content = content.replace("title:","")
                                    data.insert(i,content)
                                    content1.insert(i,fil.read())
                            else:
                                a = a+1
                                with open("./posts/"+str(f),'r') as filipt:
                                    contentt = filipt.readline()
                                    contentt = contentt.replace("title:","")
                                    dataa.insert(i,contentt)
                                    contentt1.insert(i,filipt.read())
                    else:
                        if int(fstr[0]) == int(nowtime):
                            if 6 - int(fstr[1]) >= 0:
                                i = i+1
                                with open("./posts/"+str(f),'r') as fil:
                                    content = fil.readline()
                                    content = content.replace("title:","")
                                    data.insert(i,content)
                                    content1.insert(i,fil.read())
                            else:
                                a = a+1
                                with open("./posts/"+str(f),'r') as filipt:
                                    contentt = filipt.readline()
                                    contentt = contentt.replace("title:","")
                                    dataa.insert(i,contentt)
                                    contentt1.insert(i,filipt.read())
                                
                        elif int(fstr[0]) == int(nowtime)- 1:
                            nowm = time.strftime('%m')
                            if int(fstr[1]) - 6 - int(nowm) > 0 :
                                i = i+1
                                with open("./posts/"+str(f),'r') as fil:
                                    content = fil.readline()
                                    content = content.replace("title:","")
                                    data.insert(i,content)
                                    content1.insert(i,fil.read())
                            else:
                                a = a+1
                                with open("./posts/"+str(f),'r') as filipt:
                                    contentt = filipt.readline()
                                    contentt = contentt.replace("title:","")
                                    dataa.insert(i,contentt)
                                    contentt1.insert(i,filipt.read())
                            
            pastdata = data
            contentdata = content1
            olddata = dataa
            oldcontent = contentt1
    else:
        os.makedirs(postpath)

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
@app.route('/lab')
def lab():
    return render_template('lab.html')
@app.route('/teach/<url>')
def teachurl(url):
    return render_template(url)
@app.route('/download')
def download():
    return render_template('download.html')
