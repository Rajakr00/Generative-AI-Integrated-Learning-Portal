from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app,supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = 'jdhfhufhuishuhuihufhu'
app.config['SECURITY_TOKEN_AUTHENTICATION_KEY']="myauthkey"
app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER']="myauthtoken"

app.app_context().push()
db = SQLAlchemy(app)

app = Flask(__name__)

#----database models---
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name= db.Column(db.String,nullable=False)
    email = db.Column(db.String, nullable=False,unique=True)
    password= db.Column(db.String,nullable=False)
    role = db.Column(db.String, nullable=False)
    enrolled_courses = db.relationship('Enrollment', backref='user', lazy='subquery',cascade='all, delete-orphan')

class Course(db.Model):
    __tablename__="course"
    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name=db.Column(db.String,nullable=False)
    description=db.Column(db.String, nullable=False)
    enrolled_students = db.relationship('Enrollment', backref='course', lazy='subquery',cascade='all, delete-orphan')
    weeks = db.relationship('Week', backref='course', lazy='subquery', cascade='all, delete-orphan')

class Enrollment(db.Model):
    __tablename__="enrollment"
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    __table_args__ = (db.PrimaryKeyConstraint('user_id', 'course_id'),)

class Week(db.Model):
    __tablename__="week"
    week_id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    week_no=db.Column(db.Integer,nullable=False)
    links = db.relationship('Link', backref='week', lazy='subquery', cascade='all, delete-orphan')

class Link(db.Model):
    __tablename__='link'
    link_id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    week_id=db.Column(db.Integer, db.ForeignKey('week.week_id'), nullable=False)
    link_order=db.Column(db.Integer,nullable=False)
    url=db.Column(db.String,nullable=False)

# db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, Team 12!</p>"


if __name__ == "__main__":
    app.run()