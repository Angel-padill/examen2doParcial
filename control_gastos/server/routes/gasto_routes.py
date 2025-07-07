from flask import Blueprint, request, jsonify
from models.gasto import Gasto
from database import db
from datetime import datetime

gasto_bp = Blueprint('gasto', __name__)

@gasto_bp.route('/gastos', methods=['POST'])
def create_gasto():
    data = request.json
    gasto = Gasto(
        categoria=data['categoria'],
        descripcion=data.get('descripcion'),
        monto=data['monto'],
        fecha=datetime.strptime(data['fecha'], '%Y-%m-%d')
    )
    db.session.add(gasto)
    db.session.commit()
    return jsonify({'message': 'Gasto creado correctamente'}), 201

@gasto_bp.route('/gastos', methods=['GET'])
def get_gastos():
    gastos = Gasto.query.all()
    return jsonify([{
        'id': g.id,
        'categoria': g.categoria,
        'descripcion': g.descripcion,
        'monto': g.monto,
        'fecha': g.fecha.isoformat()
    } for g in gastos]), 200

@gasto_bp.route('/gastos/<int:id>', methods=['PUT'])
def update_gasto(id):
    data = request.json
    gasto = Gasto.query.get_or_404(id)
    gasto.categoria = data['categoria']
    gasto.descripcion = data.get('descripcion')
    gasto.monto = data['monto']
    gasto.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d')
    db.session.commit()
    return jsonify({'message': 'Gasto actualizado'}), 200

@gasto_bp.route('/gastos/<int:id>', methods=['DELETE'])
def delete_gasto(id):
    gasto = Gasto.query.get_or_404(id)
    db.session.delete(gasto)
    db.session.commit()
    return jsonify({'message': 'Gasto eliminado'}), 200
