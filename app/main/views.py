from flask import render_template, flash, redirect
from . import main
from .forms import FeedbackForm
from ..email import send_email


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/play.html')
def play():
    return render_template('play/index.html')

@main.route('/play/chess/index.html')
def play_chess():
    return render_template('play/chess/index.html')

@main.route('/play/chess/world_cup_2017/index.html')
def play_chess_world_cup_2017():
    return render_template('/play/chess/world_cup_2017/index.html')

@main.route('/play/chess/world_cup_2017/rules.html')
def play_chess_world_cup_2017_rules():
    return render_template('/play/chess/world_cup_2017/rules.html')

@main.route('/play/chess/world_cup_2017/games.html')
def play_chess_world_cup_2017_games():
    return render_template('/play/chess/world_cup_2017/games.html')

@main.route('/play/chess/world_cup_2017/results.html')
def play_chess_world_cup_2017_results():
    return render_template('play/chess/world_cup_2017/results.html')

@main.route('/play/skating/index.html')
def play_skating():
    return render_template('play/skating/index.html')

@main.route('/play/skating/rostelecom_cup_2017/index.html')
def play_skating_rostelecom_cup_2017():
    return render_template('play/skating/rostelecom_cup_2017/index.html')

@main.route('/play/skating/rostelecom_cup_2017/rules.html')
def play_skating_rostelecom_cup_2017_rules():
    return render_template('play/skating/rostelecom_cup_2017/rules.html')

@main.route('/play/skating/rostelecom_cup_2017/games.html')
def play_skating_rostelecom_cup_2017_games():
    return render_template('play/skating/rostelecom_cup_2017/games.html')

@main.route('/play/volleyball/index.html')
def play_volleyball():
    return render_template('play/volleyball/index.html')

@main.route('/play/volleyball/europe_champ_2017/index.html')
def play_volleyball_europe_champ_2017():
    return render_template('play/volleyball/europe_champ_2017/index.html')

@main.route('/play/volleyball/europe_champ_2017/rules.html')
def play_volleyball_europe_champ_2017_rules():
    return render_template('play/volleyball/europe_champ_2017/rules.html')

@main.route('/play/volleyball/europe_champ_2017/games.html')
def play_volleyball_europe_champ_2017_games():
    return render_template('play/volleyball/europe_champ_2017/games.html')

@main.route('/play/volleyball/europe_champ_2017/results.html')
def play_volleyball_europe_champ_2017_results():
    return render_template('play/volleyball/europe_champ_2017/results.html')

@main.route('/about_us.html')
def about_us():
    return render_template('about_us.html')

@main.route('/download.html')
def download():
    return render_template('download.html')

@main.route('/buy.html')
def buy():
    return render_template('buy.html')

@main.route('/archive/index.html')
def archive():
    return render_template('archive/index.html')

@main.route('/archive/football_europe_champ_2012.html')
def archive_football_europe_champ_2012():
    return render_template('archive/football_europe_champ_2012.html');

@main.route('/archive/hockey_khl_champ_2013.html')
def archive_hockey_khl_champ_2013():
    return render_template('archive/hockey_khl_champ_2013.html')

@main.route('/archive/chess_anand_karlsen.html')
def archive_chess_anand_karlsen():
    return render_template('archive/chess_anand_karlsen.html')

@main.route('/archive/football_conf_cup_2017.html')
def archive_football_conf_cup_2017():
    return render_template('archive/football_conf_cup_2017.html')

@main.route('/feedback.html', methods=['GET', 'POST'])
def feedback_message_submit():
    form = FeedbackForm()
    if form.validate_on_submit():
        print('Name:', form.name.data)
        print('Email:', form.email.data)
        print('Message:', form.message.data)
        send_email('mail/feedback_message',
                   name=form.name.data,
                   email=form.email.data,
                   message_body=form.message.data)
        flash('Ваше сообщение принято.')
        return redirect('/')
    else:
        print('Invalid')
    return render_template('feedback.html', form=form)
