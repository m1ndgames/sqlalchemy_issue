from .config import Config
from flask_sqlalchemy import SQLAlchemy  # noqa
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker


engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, pool_recycle=3600
)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


class CustomBase:
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()


Base = declarative_base(
    metadata=MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    ),
    cls=CustomBase,
)


def init_db():
    import apps.models  # noqa

    Base.metadata.create_all(bind=engine, checkfirst=True)


def update(self, data):
    # Update an object with the data provided
    for key, value in data.items():
        if hasattr(self, key) and value is not None:
            setattr(self, key, value)


Base.query = db_session.query_property()
Base.update = update
