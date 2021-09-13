from flask import Flask,render_template,request,url_for,redirect
import controllers.prediction as pre


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',columns=pre.columns(), values="")

@app.route('/about')
def about():
    return 

@app.route('/predictions',methods=['POST','GET'])
def predictions():
    if request.method =='GET':

        return render_template('form.html')
    elif request.method =="POST":

        values=request.form
        result=pre.predict(pre.form2data(values))

        
        return render_template('about.html',values=values, result=result)
          


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050,debug=True)