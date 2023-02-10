from flask import Flask, request, render_template, url_for, redirect


app = Flask(__name__)
app.app_context().push()


@app.route('/')
def index():
	return render_template('form.html')


@app.route('/execute', methods=['GET', 'POST'])
def execute():
	*********************************************


if __name__ == '__main__':
	app.run(debug=True)



