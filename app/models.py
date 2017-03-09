from . import db

class UserProfile(db.Model):
    userid = db.Column(db.Integer, primary_key=True, autoincrement=False)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    biography = db.Column(db.String(255))
    image = db.Column(db.String(255))
    created_on = db.Column(db.DateTime)
    
    def __init__(self, userid, firstname, lastname, username, age, sex, bio, imageFile, createdOn):
        self.userid = userid
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.age = age
        self.gender = sex
        self.biograpgy = bio
        self.image = imageFile
        self.created_on = createdOn
    
    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
