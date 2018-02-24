from flask import Blueprint, request, render_template
from app import db
from app.mod_home.models import Result, TopPassword, Page, Password
from app.mod_home.forms import CheckPassword
from app.helpers import password, time_convert, ref
from zxcvbn import zxcvbn

mod_home = Blueprint('home', __name__, url_prefix='/')


@mod_home.route('')
def home():
    # Provjeriti affilate linkove
    ref.check(request)

    # Broj provjera
    result = db.engine.execute("SELECT COUNT(`id`) FROM `password`").first()

    return render_template('home/index.html', num_checks=result[0])


@mod_home.route('lozinka/', methods=['POST', 'GET'])
def lozinka():
    # Provjeriti affilate linkove
    ref.check(request)

    form = CheckPassword(request.form)

    if form.validate_on_submit():
        password_data = Password(password=form.password.data)
        db.session.add(password_data)

        result = db.engine.execute("SELECT * FROM `result` WHERE BINARY `password` = '%s'" % form.password.data).first()

        if not result:
            strength = password.password_strength(form.password.data)
            zxcvb = zxcvbn(form.password.data)
            position = TopPassword.query.filter_by(password=form.password.data).first()

            data = {
                'password': form.password.data,
                'length' : strength['length'],
                'letters': strength['letters'],
                'digits': strength['digits'],
                'uppercase': strength['uppercase'],
                'lowercase': strength['lowercase'],
                'symbols':  strength['symbols'],
                'position': position.id if position else 0,
                'guesses': int(zxcvb['guesses']),
                'score': zxcvb['score'],
                'online_time_1': int(zxcvb['guesses'] * 36),
                'online_time_2': int(zxcvb['guesses'] / 10),
                'offline_time_1': int(zxcvb['guesses'] / 100),
                'offline_time_2': int(zxcvb['guesses'] / 200000)
            }

            result = Result(**data)
            db.session.add(result)

        db.session.commit()

        time_string = {
            'online_time_1': time_convert.convert_to_str(int(result.online_time_1)),
            'online_time_2': time_convert.convert_to_str(int(result.online_time_2)),
            'offline_time_1': time_convert.convert_to_str(int(result.offline_time_1)),
            'offline_time_2': time_convert.convert_to_str(int(result.offline_time_2))
        }

        return render_template('home/lozinka.html', form=form, result=result, time_string=time_string)

    return render_template('home/lozinka.html', form=form)


@mod_home.route('<string:link>/')
def page(link):
    # Provjeriti affilate linkove
    ref.check(request)

    page = Page.query.filter_by(link=link).first_or_404()

    return render_template('page/index.html', page=page)