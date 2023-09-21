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
    n = 15
    n1 = 2
    n2 = 2
    n3 = 2
    n4 = 2
    if request.method == 'POST':
        value1 = float(request.form['value1'])
        if value1 == 0:
            n1 = 1
        value2 = float(request.form['value2'])
        if value2 == 0:
            n1 = 1
        value3 = float(request.form['value3'])
        if value3 == 0:
            n2 = 1
        value4 = float(request.form['value4'])
        if value4 == 0:
            n2 = 1
        value5 = float(request.form['value5'])
        if value5 == 0:
            n3 = 1
        value6 = float(request.form['value6'])
        if value6 == 0:
            n3 = 1
        value7 = float(request.form['value7'])
        if value7 == 0:
            n4 = 1
        value8 = float(request.form['value8'])
        if value8 == 0:
            n4 = 1
        value9 = float(request.form['value9'])
        if value9 == 0:
            n = n - 1
        value10 = float(request.form['value10'])
        if value10 == 0:
            n = n - 1
        value11 = float(request.form['value11'])
        if value11 == 0:
            n = n - 1
        value12 = float(request.form['value12'])
        if value12 == 0:
            n = n - 1
        value13 = float(request.form['value13'])
        if value13 == 0:
            n = n - 1
        value14 = float(request.form['value14'])
        if value14 == 0:
            n = n - 1
        value15 = float(request.form['value15'])
        if value15 == 0:
            n = n - 1
        value16 = float(request.form['value16'])
        if value16 == 0:
            n = n - 1
        value17 = float(request.form['value17'])
        if value17 == 0:
            n = n - 1
        value18 = float(request.form['value18'])
        if value18 == 0:
            n = n - 1
        value19 = float(request.form['value19'])
        if value19 == 0:
            n = n - 1
        mean1 = (value1 + value2) / n1
        if mean1 == 0:
            n = n - 1
        mean2 = (value3 + value4) / n2
        if mean2 == 0:
            n = n - 1
        mean3 = (value5 + value6) / n3
        if mean3 == 0:
            n = n - 1
        mean4 = (value7 + value8) / n4
        if mean4 == 0:
            n = n - 1
        mean = (value9 + value10 + value11 + value12 + value13 + value14 + value15 + value16 + value17 + value18 + value19 + mean1 + mean2 + mean3 + mean4) / n
        mean_se_15= (mean - int(mean)) * n
        import math
        mean_se_15_strog = math.ceil(mean_se_15)
        final_mean = "{} +  {}/{}".format(int(mean) ,mean_se_15_strog ,n)
        if option == "option1":
            return render_template('results_a_gymn.html', final_mean=final_mean )
        elif option == "option2":
            return render_template('results_b_gymn.html', final_mean=final_mean )
        elif option == "option3":
            return render_template('results_g_gymn.html', final_mean=final_mean )
        elif option == "option4":
            return render_template('results_a_lykeiou.html', final_mean=final_mean )
        elif option == "option5":
            return render_template('results_b_lykeiou.html', final_mean=final_mean )
        elif option == "option6":
            return render_template('results_g_lykeiou.html', final_mean=final_mean )
    if option == "option1":
        return render_template('results_a_gymn.html', final_mean=None)
    if option == "option2":
        return render_template('results_b_gymnasioy.html', final_mean=None)
    if option == "option3":
        return render_template('result.html', final_mean=None)
    elif option == "option4":
        return render_template('results_a_lykeioy.html', final_mean=None )
    elif option == "option5":
        return render_template('results_b_lykeiou.html', final_mean=None )
    elif option == "option6":
        return render_template('results_g_lykeiou.html', final_mean=None )
if __name__ == '__main__':
    app.run(debug=True)
