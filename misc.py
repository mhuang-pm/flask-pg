
from flask import Blueprint, jsonify

misc = Blueprint('misc', __name__)


@misc.route('/endpoint4')
def demo4():
    return jsonify({'message': 'You made it'})


@misc.route('/endpoint5')
def demo5():
    return jsonify({'message': 'You made it'})