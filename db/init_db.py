from db.database import engine, Base
from db.models import EmailStore

Base.metadata.create_all(bind=engine)