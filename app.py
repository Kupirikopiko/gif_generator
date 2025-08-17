import os

import imageio as iio
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def show_gif():
    filenames = ["./images/team-pic1.png", "./images/team-pic2.png"]
    images = []

    for file in filenames:
        img = iio.v3.imread(file)
        images.append(img)
        iio.mimsave("static/team.gif", images, duration=500, loop=0)

    return render_template_string("""
        <html>
        <body style="text-align:center; margin-top:50px;">
            <h1>Generated GIF</h1>
            <img src="{{ url_for('static', filename='team.gif') }}"  alt="team gif">
        </body>
    </html>
    """)

if __name__ == "__main__":
    os.makedirs(".venv/static", exist_ok=True)
    app.run(debug=True)