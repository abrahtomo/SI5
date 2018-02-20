from flask import Flask, render_template, request, redirect
import datahandler

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/first-page')
def show_first_page():
    planets = datahandler.get_first_page()
    for planet in planets:
        if planet['surface_water'] != 'unknown':
            planet['surface_water'] = planet['surface_water'] + '%'
        if planet['diameter'] != 'unknown':
            planet['diameter'] = planet['diameter'] + 'km'
        if planet['population'] != 'unknown':
            planet['population'] = planet['population'] + ' people'
        if planet['residents'] == []:
            planet['residents'] = 'No known residents'
        else:
            planet['residents'] = str(len(planet['residents'])) + ' resident(s)'

    return render_template("first_page.html", planets=planets)


@app.route('/second-page', methods=['GET', 'POST'])
def show_second_page():
    planets = datahandler.get_second_page()
    for planet in planets:
        if planet['surface_water'] != 'unknown':
            planet['surface_water'] = planet['surface_water'] + '%'
        if planet['diameter'] != 'unknown':
            planet['diameter'] = planet['diameter'] + 'km'
        if planet['population'] != 'unknown':
            planet['population'] = planet['population'] + ' people'
        if planet['residents'] == []:
            planet['residents'] = 'No known residents'
        else:
            planet['residents'] = str(len(planet['residents'])) + ' resident(s)'
    return render_template('second_page.html', planets=planets)


@app.route('/third-page', methods=['GET', 'POST'])
def show_third_page():
    planets = datahandler.get_third_page()
    for planet in planets:
        if planet['surface_water'] != 'unknown':
            planet['surface_water'] = planet['surface_water'] + '%'
        if planet['diameter'] != 'unknown':
            planet['diameter'] = planet['diameter'] + 'km'
        if planet['population'] != 'unknown':
            planet['population'] = planet['population'] + ' people'
        if planet['residents'] == []:
            planet['residents'] = 'No known residents'
        else:
            planet['residents'] = str(len(planet['residents'])) + ' resident(s)'
    return render_template('third_page.html', planets=planets)


@app.route('/fourth-page', methods=['GET', 'POST'])
def show_fourth_page():
    planets = datahandler.get_fourth_page()
    for planet in planets:
        if planet['surface_water'] != 'unknown':
            planet['surface_water'] = planet['surface_water'] + '%'
        if planet['diameter'] != 'unknown':
            planet['diameter'] = planet['diameter'] + 'km'
        if planet['population'] != 'unknown':
            planet['population'] = planet['population'] + ' people'
        if planet['residents'] == []:
            planet['residents'] = 'No known residents'
        else:
            planet['residents'] = str(len(planet['residents'])) + ' resident(s)'
    return render_template('fourth_page.html', planets=planets)


@app.route('/fifth-page', methods=['GET', 'POST'])
def show_fifth_page():
    planets = datahandler.get_fifth_page()
    for planet in planets:
        if planet['surface_water'] != 'unknown':
            planet['surface_water'] = planet['surface_water'] + '%'
        if planet['diameter'] != 'unknown':
            planet['diameter'] = planet['diameter'] + 'km'
        if planet['population'] != 'unknown':
            planet['population'] = planet['population'] + ' people'
        if planet['residents'] == []:
            planet['residents'] = 'No known residents'
        else:
            planet['residents'] = str(len(planet['residents'])) + ' resident(s)'
    return render_template('fifth_page.html', planets=planets)


@app.route('/sixth-page', methods=['GET', 'POST'])
def show_sixth_page():
    planets = datahandler.get_sixth_page()
    for planet in planets:
        if planet['surface_water'] != 'unknown':
            planet['surface_water'] = planet['surface_water'] + '%'
        if planet['diameter'] != 'unknown':
            planet['diameter'] = planet['diameter'] + 'km'
        if planet['population'] != 'unknown':
            planet['population'] = planet['population'] + ' people'
        if planet['residents'] == []:
            planet['residents'] = 'No known residents'
        else:
            planet['residents'] = str(len(planet['residents'])) + ' resident(s)'
    return render_template('sixth_page.html', planets=planets)


@app.route('/seventh-page', methods=['GET', 'POST'])
def show_seventh_page():
    planets = datahandler.get_seventh_page()
    for planet in planets:
        if planet['surface_water'] != 'unknown':
            planet['surface_water'] = planet['surface_water'] + '%'
        if planet['diameter'] != 'unknown':
            planet['diameter'] = planet['diameter'] + 'km'
        if planet['population'] != 'unknown':
            planet['population'] = planet['population'] + ' people'
        if planet['residents'] == []:
            planet['residents'] = 'No known residents'
        else:
            planet['residents'] = str(len(planet['residents'])) + ' resident(s)'
    return render_template('seventh_page.html', planets=planets)


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True)