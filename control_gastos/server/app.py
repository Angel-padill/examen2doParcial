from flask import Flask, request, jsonify
from models import db, Gasto
from config import Config
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/gastos', methods=['POST'])
def crear_gasto():
    data = request.json
    try:
        descripcion = data['descripcion']
        monto = float(data['monto'])
        fecha = datetime.fromisoformat(data['fecha']).date()
    except (KeyError, ValueError):
        return jsonify({'error': 'Datos inválidos'}), 400

    gasto = Gasto(descripcion=descripcion, monto=monto, fecha=fecha)
    db.session.add(gasto)
    db.session.commit()
    return jsonify(gasto.to_dict()), 201

@app.route('/gastos', methods=['GET'])
def obtener_gastos():
    gastos = Gasto.query.all()
    return jsonify([gasto.to_dict() for gasto in gastos]), 200

@app.route('/gastos/<int:id>', methods=['PUT'])
def actualizar_gasto(id):
    gasto = Gasto.query.get(id)
    if not gasto:
        return jsonify({'error': 'Gasto no encontrado'}), 404

    data = request.json
    if 'descripcion' in data:
        gasto.descripcion = data['descripcion']
    if 'monto' in data:
        gasto.monto = float(data['monto'])
    if 'fecha' in data:
        gasto.fecha = datetime.fromisoformat(data['fecha']).date()

    db.session.commit()
    return jsonify(gasto.to_dict()), 200

@app.route('/gastos/<int:id>', methods=['DELETE'])
def eliminar_gasto(id):
    gasto = Gasto.query.get(id)
    if not gasto:
        return jsonify({'error': 'Gasto no encontrado'}), 404

    db.session.delete(gasto)
    db.session.commit()
    return jsonify({'mensaje': 'Gasto eliminado'}), 200

if __name__ == '__main__':
    app.run(debug=True)
