from flask import Flask, request, render_template, url_for, redirect
# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.formatters import HtmlFormatter
import subprocess

app = Flask(__name__)
app.app_context().push()

# sourcecode = 'print "Hello world Example" '
# print(highlight(sourcecode, PythonLexer(), HtmlFormatter()))


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



