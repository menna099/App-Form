from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/') 
def index(): 
    return render_template('home.html') 
 
@app.route('/home') 
def home(): 
    return render_template('home.html') 
 
@app.route('/admin') 
def admin(): 
    return render_template('admin.html') 
 
@app.route('/attachments') 
def attachments(): 
    return render_template('attachments.html') 
 
@app.route('/technicalVisit') 
def technical_visit(): 
    return render_template('technicalVisit.html') 
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5555)