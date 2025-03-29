from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, ShortenedURL
from utils import generate_short_code
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')

# Configuração do banco de dados SQLite3 local
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'urls.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    urls = ShortenedURL.query.order_by(ShortenedURL.created_at.desc()).all()
    return render_template('index.html', urls=urls)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('url')
    if not original_url:
        flash('Por favor, insira uma URL válida', 'error')
        return redirect(url_for('index'))
    
    short_code = generate_short_code()
    while ShortenedURL.query.filter_by(short_code=short_code).first():
        short_code = generate_short_code()
    
    new_url = ShortenedURL(original_url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()
    
    flash('URL encurtada com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = ShortenedURL.query.filter_by(short_code=short_code).first_or_404()
    url.clicks += 1
    db.session.commit()
    return redirect(url.original_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 