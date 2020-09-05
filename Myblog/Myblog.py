from blog import apple, db
from blog.models import User, Post

@apple.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}