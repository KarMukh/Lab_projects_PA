from flask import Flask, request, render_template, url_for, redirect
import subprocess

app = Flask(__name__)
app.app_context().push()


@app.route('/')
def index():
	return render_template('form.html')


@app.route('/execute', methods=['GET', 'POST'])
def execute():
	code = request.form['code']
	result = subprocess.run(['python', '-c', code], input=code, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	return render_template('result.html', result=result.stdout, error=result.stderr)


if __name__ == '__main__':
	app.run(debug=True)



