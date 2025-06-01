from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine("sqlite:///test.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Сохраняем запись
new_user = User(name="Аня")
session.add(new_user)
session.commit()

# Извлекаем запись
user = session.query(User).filter_by(name="Аня").first()
print(f"ID: {user.id}, Name: {user.name}")
