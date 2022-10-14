from flask import Flask, render_template
import json

app = Flask(__name__)

with open('data.json', 'r') as data:
    data = json.load(data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<username>')
def landingPage(username):

    try:
        userData = data[username]

        return render_template(
            'index.html',
            username = username,
            profile_pic = userData['profile_pic'],
            github = userData['github'],
            whatsapp = userData['whatsapp'],
            instagram = userData['instagram'],
            twitter = userData['twitter'],
            spotify = userData['spotify'],
            facebook = userData['facebook'],
            telegram = userData['telegram'],
            linkedin = userData['linkedin']
        )
        
    except:
        return '<h2> Data not submitted in the repository or invalid username! <a href = "https://github.com/abhilashmnair/aboutme">Click here for instructions.</a><h2>'

if __name__ == '__main__':
    app.run(threaded = True, debug = True)