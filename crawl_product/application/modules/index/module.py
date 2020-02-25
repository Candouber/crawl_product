from application import db



# api = db.Table(
#     "api",
#     db.Column("name", db.text, nullable=False),
#     db.Column("type1", db.String(40), nullable=False),
#     db.Column("type2", db.String(40), nullable=False),
#     db.Column("type3", db.String(40), nullable=False),
#     db.Column("type4", db.String(40), nullable=False),
#     db.Column("url", db.text, nullable=False),
#     db.Column("sort", db.String(20), nullable=False),
# )

class Api(db.Model):
    """all apis list"""
    __tablename__= "api"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    type1 = db.Column(db.String(40), nullable=False)
    type2 = db.Column(db.String(40), nullable=False)
    type3 = db.Column(db.String(40), nullable=False)
    type4 = db.Column(db.String(40), nullable=False)
    url = db.Column(db.Text, nullable=False)
    sort = db.Column(db.String(20), nullable=False)
    com = db.Column(db.Text, nullable=False)

    @classmethod
    def get_attr(cls, k):
        attr = cls.__dict__.get(k, None)
        if attr: return attr
        raise KeyError("error key '{}' in class '{}'".format(k, cls.__name__))


class Typelist(db.Model):
    '''type match chinese'''
    __tablename__= "typelist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)

    @classmethod
    def get_attr(cls, k):
        attr = cls.__dict__.get(k, None)
        if attr: return attr
        raise KeyError("error key '{}' in class '{}'".format(k, cls.__name__))

