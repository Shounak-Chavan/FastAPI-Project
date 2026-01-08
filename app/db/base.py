from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Inheriting from Base tells SQLAlchemy:
# This class represents a table that can be created in the database
