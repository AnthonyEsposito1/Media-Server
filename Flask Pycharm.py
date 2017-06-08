import mimetypes
import sys, os
import re

from flask import Flask, render_template, request, send_file, Response
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('base.html')


@app.route('/test2')
def test2():
    return render_template('indextest.html')


@app.route('/media2/<name>/<episode>')
def test5(episode, name):
    return render_template('videojs.html', episode=episode, name=name)

@app.route('/media2')
def media():
    title_dir = os.path.join(os.path.dirname(__file__), 'static/media')
    media = next(os.walk(title_dir))[1]
    return render_template('media.html', media=media)


@app.route('/media2/<name>')
def episodes(name):
    episodes=[]
    title_dir = os.path.join(os.path.dirname(__file__), "static/media/" + name)
    p = os.listdir(title_dir)
    for file in p:
        if file.endswith((".mkv",".mp4")):
            episodes.append(file)
    return render_template('episode.html', episodes=episodes, name=name)


if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)
