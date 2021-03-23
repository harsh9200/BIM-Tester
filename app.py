from utils import Formatter
from geolocation import GeoLocation 
from project_setup import ProjectSetup
from flask import Flask, render_template, request

app = Flask(__name__)
formatter = Formatter()

@app.route('/', methods=['GET', 'POST'])
def base():
    if request.method == 'GET':
        return render_template("index.html", Data=[])
    else:
        print(request.form)
        if request.form.get('micromvd') == 'geolocation':
            Data = formatter.format(GeoLocation)
        else:
            Data = formatter.format(ProjectSetup)
        return render_template("index.html", Data=Data)


if __name__ == '__main__':
    app.run()