from flask import render_template
from blog import apple, db

@apple.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@apple.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500