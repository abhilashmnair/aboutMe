from flask import Flask, render_template
import json

app = Flask(__name__)

with open('data.json', 'r') as data:
    data = json.load(data)

@app.route('/')
def home():
    return 'Hello'

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
        spotify = userData['spotify'])
        
    except:
        return 'Data Not submitted in the repository! Visit github.com/abhilashmnair/aboutme'

if __name__ == '__main__':
    app.run(threaded = True, debug = True)