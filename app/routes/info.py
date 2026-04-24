from flask import Blueprint, render_template

info_bp = Blueprint('info', __name__)

@info_bp.route('/release-notes')
def release_notes():
    return render_template('release_notes.html')

@info_bp.route('/about')
def about():
    return render_template('about.html')