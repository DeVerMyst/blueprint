from . import main

@main.route('/')
def index():
    return "index"

@main.route('/profile')
def profile():
    return "profile"
