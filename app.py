from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
api = Api(app)
CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})

# Configure SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = 'jdhfhufhuishuhuihufhu'
app.config['SECURITY_TOKEN_AUTHENTICATION_KEY'] = "myauthkey"
app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = "myauthtoken"

# Initialize SQLAlchemy
db = SQLAlchemy(app)

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

#-----------API Controllers-----------

class StudentLogin(Resource):
    def post(self):
        data=request.get_json()
        user=User.query.filter_by(email=data['username']).first()
        if user:
            if user.role == 'student':
                if (user.password == data['password']):
                    response=({
                        'message': 'User login successful',
                        'user_id': user.user_id
                    })
                    message=make_response(response)
                    return message
                else:
                    return {'message':'Invalid password'} , 401 #Forbidden
            else:
                return {'message':'Only users can access this page'} , 403 #Unauthorised 
        else:
            return {'message':'Invalid username'} , 401 #Forbidden

class RegisteredCourses(Resource):
    
    def get(self):
        user_id = request.args.get('user_id')
        user=User.query.filter_by(user_id=int(user_id)).first()
        if user:
            enrolled_courses=Enrollment.query.filter_by(user_id=user_id).all()
            response={'courses':[],'no_of_courses':0}
            if enrolled_courses:
                for course in enrolled_courses:
                    course_details = Course.query.filter_by(course_id=course.course_id).first()
                    course_name = course_details.name
                    course_description = course_details.description
                    response['courses'].append({
                        'name':course_name,
                        'desc':course_description
                    })
                    response['no_of_courses']=response['no_of_courses']+1
                return response, 200
            else:
                return {'message':'No registered courses'} , 201
        else:
            return {'message':'Invalid username'} , 401 #Forbidden

class StudentDashboard(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        if user_id:
            # Fetch courses for the given user_id
            enrollments = Enrollment.query.filter_by(user_id=user_id).all()
            courses = []
            for enrollment in enrollments:
                course = Course.query.get(enrollment.course_id)
                if course:
                    courses.append({
                        "name": course.name,
                        "desc": course.description
                    })
            no_of_courses = len(courses)
            print(courses)
            return jsonify({"courses": courses, "no_of_courses": no_of_courses}),200
        else:
            return jsonify({"message": "User ID is required"}), 400

# Add the resource to the API
# api.add_resource(StudentDashboard, '/api/studentDashboard')
api.add_resource(StudentLogin,'/api/studentLogin') 
api.add_resource(RegisteredCourses,'/api/studentDashboard') 

@app.route("/")
def hello_world():
    return "<p>Hello, Team 12!</p>"


if __name__ == "__main__":
    app.run(debug=True)