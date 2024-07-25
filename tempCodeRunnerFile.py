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