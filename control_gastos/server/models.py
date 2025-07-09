from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gasto(db.Model):
    __tablename__ = 'gastos'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'monto': self.monto,
            'fecha': self.fecha.isoformat()
        }
