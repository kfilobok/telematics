from flask import Flask, render_template, request
from ATM_algo import mini_ATM

app = Flask(__name__)
x = 8


@app.route('/', methods=['POST', 'GET'])
def index() -> int:
    global x
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        request.method = 'GET'
        x = int(request.form['amount_of_cassettes'])
        return result()


@app.route("/ATMcassettes", methods=['POST', 'GET'])
def result():
    global x
    sp1 = ["form.html", "one.html", "two.html", "three.html", "four.html",
           "five.html", "six.html", "seven.html", "eight.html", ]
    if request.method == 'GET':
        return render_template(sp1[x])
    elif request.method == 'POST':
        dano = []
        for i in range(1, x + 1):
            state = request.form.get(f'state{i}')[0]
            nam = int(request.form.get(f'denomination{i}').split('_')[0])
            amount = request.form.get(f'remainder{i}', type=int)
            if state == 'a':
                dano += [nam] * amount

        dano.sort(reverse=True)
        input_sum = request.form.get('input_sum', type=int)  # input_sum
        possibility, s, time = mini_ATM(dano, input_sum)
        if possibility:
            return render_template(sp1[x], entry='ДА', time=time, listik=s)
        else:
            return render_template(sp1[x], entry='НЕТ', time=time)


if __name__ == '__main__':
    app.run(debug=True)
