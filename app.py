import os
import json
from utils import create_requirement, Generate_JSON
from flask import Flask, render_template, request, send_file, redirect

app = Flask(__name__)

featuresDict = Generate_JSON().features_dict()

@app.route('/', methods=['GET', 'POST'])
def base():
    file_path = featuresDict[request.args.get('value', 'project_setup')]
    if request.method == 'GET':
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        
        return render_template("index.html", F=data, feat=os.path.basename(os.path.dirname(file_path)))
    else:
        feature_path = file_path.rsplit('.')[0] + '.feature'
        create_requirement(request.form, feature_path)
        return send_file(feature_path,
                         mimetype='text/csv',
                         attachment_filename='Feature.feature',
                         as_attachment=True)

if __name__ == '__main__':
    app.run()
