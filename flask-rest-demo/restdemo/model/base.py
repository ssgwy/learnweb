from restdemo import db


class Base(db.Model):

    __abstract__ = True     #提示系统：这不是真正db.Model，不必创建数据库

    def as_dict(self):
        return {c.name:getattr(self, c.name) for c in self.__table__.columns}

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
