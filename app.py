from flask import Flask,render_template,request,url_for,redirect
import controllers.prediction as pre
import migrations.prediction_migration as mig


app=Flask(__name__)

@app.route('/')
def index():
    values=mig.select_all()
    
    return render_template('index.html',columns=pre.columns(), values=values)

@app.route('/about')
def about():
    return 

@app.route('/predictions',methods=['POST','GET'])
def predictions():
    if request.method =='GET':

        return render_template('form.html')
    elif request.method =="POST":
        #toutes les valeurs du formulaire
        values=request.form
        fname=values.get('firstName')
        lname=values.get('lastName')
        #prediction du resultat
        result=pre.predict(pre.form2data(values))

        #insertion des données
        mig.insert_to_database(fname,lname,pre.form_util_values(values),result)

        
        return render_template('about.html',values=values, result=result)
          


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050,debug=True)