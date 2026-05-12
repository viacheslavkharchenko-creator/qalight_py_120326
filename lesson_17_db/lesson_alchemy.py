from sqlalchemy import (
    Column, 
    Integer, 
    String,  
    DateTime, 
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Відношення до User
    author = relationship("User", back_populates="posts")
    
    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}')>"
    
User.posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    
engine = create_engine('sqlite:///test_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Створення одного об'єкта
# new_user = User(username='john_doe_111', email='john111@example.com', age=11)
# session.add(new_user)
# session.commit()

# Отримати всіх користувачів
all_users = session.query(User).all()
print(all_users)

# Отримати першого користувача
first_user = session.query(User).first()
print(first_user)

# Отримати користувача за ID
user = session.query(User).filter_by(id=2).first()
print(user)
# або
user = session.get(User, 3)
print(user)

# Фільтрація
young_users = session.query(User).filter(User.age < 30).all()
print(young_users)

