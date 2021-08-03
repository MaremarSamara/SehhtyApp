from flask import Flask , render_template 
from flask_mail import Mail, Message 
from random import *  
from flask import request 



app = Flask(__name__)  
mail = Mail(app)  
  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465     
app.config["MAIL_USERNAME"] = 'username@gmail.com'  
app.config['MAIL_PASSWORD'] = '*************'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
mail = Mail(app)  
otp = randint(000000,999999)  

@app.route('/')  
def home():  
    return render_template('home.html');  
    
@app.route('/verify',methods = ["POST"])  
def verify():  
    email = request.form["email"]  
      
    msg = Message('OTP',sender = 'username@gmail.com', recipients = [email])  
    msg.body = str(otp)  
    mail.send(msg)  
    return render_template('verify.html')  
 
@app.route('/validate',methods=["POST"])  
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return "<h3>Email verified successfully</h3>"  
    return "<h3>failure</h3>"
        
@app.route('/mainPage')  
def mainPage():  
    return render_template('mainPage.html');


@app.route('/mainPage/vitamins')  
def vitamins():  
    return render_template('vitamins.html');

@app.route('/mainPage/Tips')  
def tips():  
    return render_template('Tips.html');

@app.route('/mainPage/healthyRecipes')  
def healthyRecipes():  
    return render_template('healthyRecipes.html');

  
   

if __name__ =="__main__":  
    app.run(debug = True)  