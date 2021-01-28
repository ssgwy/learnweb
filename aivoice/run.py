from flask import Flask,render_template
import tts_app,att_app,eva_app,age_app

app = Flask(__name__)

app.register_blueprint(tts_app.b_tts,url_prefix="/tts")
app.register_blueprint(att_app.b_att,url_prefix="/att")
app.register_blueprint(eva_app.b_eva,url_prefix="/eva")
app.register_blueprint(age_app.b_age,url_prefix="/age")

@app.route('/',methods=["GET","POST"])
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
