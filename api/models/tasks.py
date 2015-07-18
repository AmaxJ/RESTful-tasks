from api import db
from datetime import datetime 
from api.models.groups import Group


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    createdOn = db.Column(db.DateTime, default=datetime.now)
    completedOn = db.Column(db.DateTime)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    complete = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return "{}: {}".format(self.group_id, self.title)

    def toggleComplete(self, boolean=True):
        if boolean:
            self.complete = True
        else:
            self.complete = False

            
