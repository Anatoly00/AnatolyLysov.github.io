from flask import Flask, render_template, request
import smtplib

OWN_EMAIL = "everybodylimbo123@gmail.com"
OWN_PASSWORD = "boos beaq ppkp srrx"
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["message"])
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)
    #     print(data["name"])
    #     print(data["email"])
    #     print(data["message"])
    #     return render_template("index.html", msg_sent=True)
    # return render_template("index.html", msg_sent=False)

def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
