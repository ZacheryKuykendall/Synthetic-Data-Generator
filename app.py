from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from generate import generate_dataset

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    rows = int(request.form.get('rows', 200))
    filename = request.form.get('filename', 'dataset.csv')
    output_path = generate_dataset(num_rows=rows, output_file=filename)
    return redirect(url_for('view_dataset', filename=os.path.basename(output_path)))

@app.route('/view/<filename>')
def view_dataset(filename):
    if not os.path.exists(filename):
        return 'File not found', 404
    df = pd.read_csv(filename)
    table = df.to_html(classes='table')
    return render_template('view.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)
