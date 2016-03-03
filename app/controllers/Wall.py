"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Wall(Controller):
    def __init__(self, action):
        super(Wall, self).__init__(action)
        self.load_model('Walls')

    def index(self):
        return self.load_view('login.html')

    def login(self):
        user_id = request.form['user']
        session['user'] = self.models['Walls'].get_user(user_id)[0]
        return redirect('/wall')

    def wall(self):
        try:
            session['user']
        except:
            return redirect('/')
        messages = self.models['Walls'].get_all_messages()
        comments = self.models['Walls'].get_all_comments()
        return self.load_view('index.html', messages=messages, comments=comments)

    def create_message(self):
        message = {
            'content': request.form['new_message'],
            'user_id': session['user']['id']
        }
        self.models['Walls'].create_message(message)
        return redirect('/wall')

    def create_comment(self):
        comment = {
            'content': request.form['new_comment'],
            'message_id': request.form['message_id'],
            'user_id': session['user']['id']
        }
        self.models['Walls'].create_comment(comment)
        return redirect('/wall')

    def logout(self):
        session.clear()
        return redirect('/')
