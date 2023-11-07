from project import db
# from project import bcrypt
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
from flask_login import UserMixin
# from flask_admin.contrib.sqla import ModelView
# from flask_admin.model import BaseModelView
# from flask_admin import Admin



# #######
# #Users#
# #######
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
 
    def __init__(self,id,name,email,img=None,mimetype=None):
        self.id=id
        self.name = name
        self.email = email

    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    # def get_id(self):
    #     return (self.id).encode('utf-8')
    def __repr__(self):
        return '<name {}'.format(self.name)
# #######
# #Posts#
# #######
# # class BlogPost(db.Model):
# #     __tablename__ = "posts"
# #     id = db.Column(db.Integer, primary_key=True)
# #     title = db.Column(db.String, nullable=False)
# #     description = db.Column(db.String, nullable=False)
# #     author_id = db.Column(db.Integer, ForeignKey('users.id'))
# #     def __init__(self,title,description,author_id):
# #         self.title = title
# #         self.description = description
# #         self.author_id = author_id
# #     def __repr__(self):
# #         return '<title {}'.format(self.title)
    
# ##########
# #services#
# ##########
# class Booking(db.Model):
#     __tablename__ = "bookings"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     description = db.Column(db.Text(), nullable=False)
#     phone_number = db.Column(db.String,nullable=True)
#     email = db.Column(db.String,nullable=True)
#     date_return = db.Column(db.Date())
#     date_interview = db.Column(db.Date())
#     user_id = db.Column(db.Integer, ForeignKey('users.id'))
#     technology_id=db.Column(db.Integer, ForeignKey('technologies.id'))
 
#     # def __init__(self,title,description,author_id,date_return,date_interview,devweb_id):
#     #     self.title = title
#     #     self.description = description
#     #     self.author_id = author_id
#     #     self.date_return = date_return
#     #     self.date_interview = date_interview
#     #     self.devweb_id= devweb_id
#     # @property
#     # def date_return(self):
#     #     return self.date_return.strftime("%m/%Y")
#     def __repr__(self):
#         return '<title {}'.format(self.title)
   
# ####################
# # Developpement Web#
# ####################

# # class DeveloppementWeb(db.Model):
# #     __tablename__ = 'developpements'
# #     id = db.Column(db.Integer, primary_key=True)
# #     technology= db.Column(db.String,default='WEB DESIGN')
# #     title = db.Column(db.String, nullable=False)
# #     description = db.Column(db.String, nullable=True)
# #     img = db.Column(db.LargeBinary, nullable=True)
# #     mimetype = db.Column(db.String)
# #     services = relationship('Service', backref="web")
    
# class Technology(db.Model):
#     __tablename__ = 'technologies'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     booking = relationship('Booking', backref="booking_tech")
#     service_id = db.Column(db.Integer, ForeignKey('services.id'))
# #######
# #Cloud#
# #######
# class Service(db.Model):
#     __tablename__ = 'services'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=True)
#     description = db.Column(db.String, nullable=False)
#     technology = relationship('Technology', backref="technology")
#     img = db.Column(db.LargeBinary, nullable=True)

    
    
# ####
# #AI#
# ####
# # class llms(db.Model):
# #     __tablename__ = 'llms'
# #     id = db.Column(db.Integer, primary_key=True)
# #     aillm = db.Column(db.String, nullable=False)
# #     description = db.Column(db.String, nullable=False)
# #     technology= db.Column(db.String,default='AI/LLM')
# #     imgai = db.Column(db.LargeBinary, nullable=False)
# #     mimetype = db.Column(db.String)
# #     services = relationship('Service', backref="llm")
# ##########
# #Blogs#
# ##########
# # class Blog(db.Model):
# #     __tablename__ = "blogs"
# #     id = db.Column(db.Integer, primary_key=True)
# #     title = db.Column(db.String, nullable=False)
# #     article = db.Column(db.Text(), nullable=False)
# #     def __init__(self,title,article):
# #         self.title = title
# #         self.article = article
       
# #     def __repr__(self):
# #         return '<title {}'.format(self.title)
# ##########
# #contacts#
# ##########
# class Message(db.Model):
#     __tablename__ = "messages"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     message = db.Column(db.Text(), nullable=False)
#     sender_id = db.Column(db.Integer,ForeignKey('users.id'))
#     def __init__(self,title,message,sender_id):
#         self.title = title
#         self.message = message
#         self.sender_id = sender_id
       
#     def __repr__(self):
#         return '<title {}'.format(self.title)


# #######
# #Admin#
# #######
# # admin= Admin(app)
# ############
# #Admin form#
# ############



# # admin.add_view(ModelView(Blog,db.session))

#     # def is_authenticated(self):
#     #     return True

#     # def is_active(self):
#     #     return True

#     # def is_anonymous(self):
#     #     return False

#     # def get_id(self):
#     #     return (self.id).encode('utf-8')
    
#     # def __repr__(self):
#     #     return '<name {}'.format(self.name)
