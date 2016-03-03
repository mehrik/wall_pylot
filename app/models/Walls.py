""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Walls(Model):
    def __init__(self):
        super(Walls, self).__init__()

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        data = [user_id]
        return self.db.query_db(query, data)

    def get_all_messages(self):
        query = "SELECT users.name, messages.content, messages.created_at, messages.id \
                 FROM messages\
                 JOIN users ON users.id = messages.user_id\
                 ORDER BY messages.created_at ASC"
        return self.db.query_db(query)

    def get_all_comments(self):
        query = "SELECT comments.id, users.name, comments.content, comments.created_at, comments.message_id\
                 FROM comments\
                 JOIN users ON users.id = comments.user_id \
                 ORDER BY comments.created_at ASC"
        return self.db.query_db(query)

    def create_message(self, message):
        query = "INSERT INTO messages (content, created_at, updated_at, user_id) \
                 VALUES (%s, NOW(), NOW(), %s)"
        data = [message['content'], message['user_id']]
        return self.db.query_db(query, data)

    def create_comment(self, comment):
        query = "INSERT INTO comments (content, created_at, updated_at, message_id, user_id) \
                 VALUES (%s, NOW(), NOW(), %s, %s)"
        data = [comment['content'], comment['message_id'], comment['user_id']]
        return self.db.query_db(query, data)

