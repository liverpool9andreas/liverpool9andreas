from flask import Flask, render_template , request , redirect , url_for
from classes import mathimata , tajis

app = Flask(__name__)

@app.route('/taji', methods =['POST','GET'])
def index():
    global taji_a
    if request.method=="POST":
        global taji_python
        taji_python = request.form['taji_html']
        if taji_python=="a":
            taji_a = tajis(taji_python)
            #return render_template('index_ypologismos_mesoy_oroy_a.html', taji = taji_python)
            return redirect(url_for('/mesos_oros', taji=taji_a))

        elif taji_python=="c":
            return render_template('index_ypologismos_mesoy_oroy_c.html')
        else:
            return render_template('index_ypologismos_mesoy_oroy_b.html')
    else:
        return render_template('index_epilogi_tajis.html')


@app.route('/mesos_oros', methods=['POST','GET'])
def submit():
    taji = request.args.get('taji')
    
    '''
    if request.method=="POST":
        if 'submit_button' in request.form:
                if request.form['submit_button'] == 'Submit':
                    global  mathimatika_python
                    mathimatika_python = float(request.form['mathimatika_html'])
                    global  fysiki_python
                    fysiki_python = float(request.form['fysiki_html'])
                    mesi_timi =(mathimatika_python + fysiki_python) / 2
                    p1 = mathimata(mathimatika_python,fysiki_python,mesi_timi)
                    return f'h mesi timi einai: {mesi_timi}'

    else:
    '''
    if taji=="a":
            return render_template('index_ypologismos_mesoy_oroy_a.html')
    elif taji=="c":
            return render_template('ypologismos_mesoy_oroy_c.html')
    else:
            return render_template('ypologismos_mesoy_oroy_b.html')

if __name__ == '__main__': app.run(debug=True)
