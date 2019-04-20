from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('home.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template('timer.html')

@app.route('/result',methods=['GET','POST'])
def result():
    Patient_Name=request.form['pname']
    Phone=request.form['phone']
    Email=request.form['email']
    Password=request.form['passw']
    log_message = "{0}|{1}|{2}|{3}\n".format(Patient_Name,Phone,Email,Password)
    screen_message = "Entry saved"
    save(log_message)
    return screen_message


def save(text, filepath='patient.txt'):
    with open("patient.txt", "a") as f:
        f.write(text)

@app.route('/read',methods=['GET','POST'])
def content():
	text = open('patient.txt', 'r+')
	content = text.read()
	text.close()
	return render_template('content.html', text=content)

@app.route('/links', methods=['POST'])
def get_links():
    search_line= "Water"
    try:
        for line in fileinput.input(os.path.join(APP_STATIC, u'patient.txt'),inplace=1):
            #Search line
            if search_line in line:
                    #If yes Modify it
                    x = line.replace(search_line,search_line+"A" + request.form.get(u'query'))
                    #Write to file
                    print (x)
            else:
                #Write as it is
                print (x)

    except BaseException as e:
        print (e)

    return render_template('content.html')

if __name__ == '__main__':
    app.run(debug=True)
