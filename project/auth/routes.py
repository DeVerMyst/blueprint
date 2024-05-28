from . import auth

@auth.route('/login')
def login():
    return 'login.html'

@auth.route('/signup')
def signup():
    return 'signup'

@auth.route('/logout')
def logout():    
    return "logout"