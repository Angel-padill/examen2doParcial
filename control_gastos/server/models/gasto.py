from database import db
from datetime import datetime

class Gasto(db.Model):
    __tablename__ = 'gastos'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False, default=datetime.utcnow)
