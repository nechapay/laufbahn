from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/tour', methods=['POST', 'GET'])
def tour():
    return render_template('tour.html')

@app.route('/tour1', methods=['POST', 'GET'])
def tour_1():
    return render_template('tour1.html')


@app.route('/tour1/_1', methods=['POST', 'GET'])
def tour_1_1():
    return render_template('example_1_1.html')

@app.route('/tour1/_2', methods=['POST', 'GET'])
def tour_1_2():
    return render_template('example_1_2.html')


@app.route('/tour2/_1', methods=['POST', 'GET'])
def tour_2_1():
    return render_template('example_2_1.html')

@app.route('/tour2/_2', methods=['POST', 'GET'])
def tour_2_2():
    return render_template('example_2_2.html')


@app.route('/tour2/_3', methods=['POST', 'GET'])
def tour_2_3():
    return render_template('example_2_3.html')

@app.route('/tour2/_4', methods=['POST', 'GET'])
def tour_2_4():
    return render_template('example_2_4.html')


@app.route('/tour2', methods=['POST', 'GET'])
def tour_2():
    return render_template('tour2.html')



@app.route('/tour3', methods=['POST', 'GET'])
def tour_3():
    return render_template('tour3.html')


@app.route('/tour3/_1', methods=['POST', 'GET'])
def tour_3_1():
    return render_template('example_3_1.html')

@app.route('/tour3/_2', methods=['POST', 'GET'])
def tour_3_2():
    return render_template('example_3_2.html')


@app.route('/cards', methods=['POST', 'GET'])
def cards():
    return render_template('cards.html')

@app.route('/book', methods=['POST', 'GET'])
def book():
    return render_template('book.html')

@app.route('/comands', methods=['POST', 'GET'])
def comands():
    return render_template('comands.html')

@app.route('/army', methods=['POST', 'GET'])
def army():
    return render_template('army.html')

@app.route('/uniform', methods=['POST', 'GET'])
def uniform():
    return render_template('uniform.html')

@app.route('/book/comands', methods=['POST', 'GET'])
def comands_book():
    return render_template('comands_book.html')

@app.route('/book/army', methods=['POST', 'GET'])
def army_book():
    return render_template('army_book.html')

@app.route('/book/teil', methods=['POST', 'GET'])
def teil_book():
    return render_template('teil_book.html')

@app.route('/book/milit', methods=['POST', 'GET'])
def milit_book():
    return render_template('milit_book.html')

@app.route('/book/uniform', methods=['POST', 'GET'])
def uniform_book():
    return render_template('uniform_book.html')

@app.route('/test', methods=['POST', 'GET'])
def test():
    return render_template('test.html')

@app.route('/win', methods=['POST', 'GET'])
def win():
    return render_template('win.html')
@app.route('/win1', methods=['POST', 'GET'])
def win1():
    return render_template('win1.html')
@app.route('/win2', methods=['POST', 'GET'])
def win2():
    return render_template('win2.html')
@app.route('/win3', methods=['POST', 'GET'])
def win3():
    return render_template('win3.html')

@app.route('/win4', methods=['POST', 'GET'])
def win4():
    return render_template('win4.html')

@app.route('/win5', methods=['POST', 'GET'])
def win5():
    return render_template('win5.html')


@app.route('/cards/comands_cards', methods=['POST', 'GET'])
def car_com():
    return render_template('comands_cards.html')

@app.route('/teil_cards', methods=['POST', 'GET'])
def teil_cards():
    return render_template('teil_cards.html')

@app.route('/milit_cards', methods=['POST', 'GET'])
def milit_cards():
    return render_template('milit_cards.html')

if __name__ == '__main__':
    app.run(debug=True)

