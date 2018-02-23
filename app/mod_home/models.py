from app import db


# Base model
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Result(Base):
    __tablename__ = 'result'

    password        = db.Column(db.String(256), nullable=True)
    length          = db.Column(db.SmallInteger(), nullable=True)
    letters         = db.Column(db.SmallInteger(), nullable=True)
    digits          = db.Column(db.SmallInteger(), nullable=True)
    uppercase       = db.Column(db.SmallInteger(), nullable=True)
    lowercase       = db.Column(db.SmallInteger(), nullable=True)
    symbols         = db.Column(db.SmallInteger(), nullable=True)
    position        = db.Column(db.Integer(), nullable=True)
    guesses         = db.Column(db.String(256), nullable=True)
    score           = db.Column(db.SmallInteger(), nullable=True)
    online_time_1   = db.Column(db.String(256), nullable=True)
    online_time_2   = db.Column(db.String(256), nullable=True)
    offline_time_1  = db.Column(db.String(256), nullable=True)
    offline_time_2  = db.Column(db.String(256), nullable=True)


class TopPassword(Base):
    __tablename__ = 'top_password'

    password = db.Column(db.String(256), nullable=True)


class Ref(Base):
    __tablename__ = 'ref'

    ref_uri = db.Column(db.String(32), nullable=True)
    status  = db.Column(db.SmallInteger(), nullable=True)


class Password(Base):
    __tablename__ = 'password'

    password = db.Column(db.String(256))


class Page(Base):
    __tablename__ = 'page'

    link    = db.Column(db.String(32), nullable=True)
    title   = db.Column(db.String(64), nullable=True)
    content = db.Column(db.Text(), nullable=True)