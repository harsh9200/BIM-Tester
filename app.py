from formatter import Formatter
from utils import create_requirements
from features.steps import project_setup
from flask import Flask, render_template, request, send_file

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def base():
    Format = Formatter(filename=project_setup)
    if request.method == 'GET':
        return render_template("index.html", F=Format)
    
    else:
        create_requirements(Format, request.form)
        return send_file('features/project_setup.feature',
                            mimetype='text/csv',
                            attachment_filename=f'project_setup.feature',
                            as_attachment=True)


if __name__ == '__main__':
    app.run()
