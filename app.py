import os
import json
from utils import create_requirement, Generate_JSON
from flask import Flask, render_template, request, send_file, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def base():
    global file_path
    if request.method == 'GET':
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        if request.args.get('value'):
            file_path = featuresDict[request.args['value']]
            return redirect(request.path)
        return render_template("index.html", F=data, feat=os.path.basename(os.path.dirname(file_path)))
    else:
        feature_path = file_path.rsplit('.')[0] + '.feature'
        create_requirement(request.form, feature_path)
        return send_file(feature_path,
                         mimetype='text/csv',
                         attachment_filename='Feature.feature',
                         as_attachment=True)

if __name__ == '__main__':
    featuresDict = Generate_JSON().features_dict()
    file_path = featuresDict['project_setup']
    app.run()
