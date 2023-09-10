from flask import Flask, render_template, request, redirect
import math
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        option = request.form['option']
        return redirect('/result/' + option)
    return render_template('index.html')

@app.route('/result/<option>', methods=['GET', 'POST'])
def result(option):
    
        if option == "option1":
            return render_template('results_a_gymn.html')
        elif option == "option2":
            return render_template('results_b_gymnasioy.html' )
        elif option == "option3":
            return render_template('result.html' )
    
    
if __name__ == '__main__':
    app.run(debug=True)
