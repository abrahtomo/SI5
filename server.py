from flask import Flask, render_template, request, redirect, session, url_for
import datahandler
import user_query

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your_secret_string'
app.secret_key = 'my_secret_key'


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = user_query.check_user(request.form['register'])
        if len(user) == 0:
            password = user_query.hash_password(request.form['password'])
            register = request.form['register']

            user_query.register(register, password)
            return redirect('/')
        else:
            return render_template('wrong.html')
    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']

        data = user_query.login(user_name)
        if not data:
            return redirect(url_for('/login', log=False))
        user_id = user_query.get_id_by_user_name(user_name)['id']
        session['username'] = user_name
        session['id'] = user_id
        print(data[0]['password'])
        log = user_query.verify_password(request.form.to_dict()['password'], data[0]['password'])
        if log:

            return redirect('/')
        else:
            session.pop('username', None)
            session.pop('id', None)
            log = False
            return redirect(url_for('/login', log=False))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True)