from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

# nuestra ruta de índice manejará la representación de nuestro formulari
@app.route('/')
def index():
	return render_template("index.html")


@app.route('/process', methods=['POST'])
def create_user():
	print("Got Post Info")
	# aquí agregamos propiedades a la sesión
	session['username'] = request.form['name']
	session['userlocation'] = request.form['location']
	session['userlanguage'] = request.form['language']
	session['usercomment'] = request.form['comment']
	return redirect('/result')	 

"""@app.route('/result')
def result_user():
	return render_template('result.html', name_on_template=session['username'], location_on_template=session['userlocation'], language_on_template=session['userlanguage'], comment_on_template=session['usercomment'])
"""
@app.route('/result')
def result_user():
	return render_template('result.html')

if __name__ == "__main__":
	app.run(debug=True)