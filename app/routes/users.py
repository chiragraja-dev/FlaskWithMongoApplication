from flask import Blueprint, jsonify, request, current_app
from app.services.user_service import create_user 
# Define the Blueprint
users_bp = Blueprint('users', __name__)

@users_bp.route('/api/create-users', methods=['POST'])
def create_user_route():
    new_user =request.json
    user = create_user(new_user, current_app.db)
    if user is None:
        return jsonify({"error":"Email already existes"}), 400
    user_dict = user.__dict__
    result = current_app.db.users.insert_one(user_dict)
    return jsonify({'_id': str(result.inserted_id)}), 201

@users_bp.route('/api/update-user/<string:email>', methods=['PUT'])
def update_user(email):
    update_data = request.json
    update_data.pop('email', None)
    result = current_app.db.users.update_one(
        {'email':email},
        {'$set':update_data}
    )
    if result.matched_count > 0:
        return jsonify({'message':'User updated'})
    else:
         return jsonify({'message': 'User not found'}),404


@users_bp.route('/api/get-users', methods=['GET'])
def get_users_route():
    users=current_app.db.users.find()
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)
    
@users_bp.route('/api/get-users-by-email', methods=['GET'])
def get_user_by_email():
    email = request.args.get('email') 
    if not email:
        return jsonify({"message": "Email parameter is required"}), 400
    user = current_app.db.users.find_one({"email": email})
    if user:
        user['_id'] = str(user['_id'])  
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404


@users_bp.route('/api/delete-user', methods=['DELETE'])
def delete_users():
    email= request.args.get('email')
    if not email:
        return jsonify({"message": "Email parameter is required"}), 400
    result= current_app.db.users.delete_one({'email':email})
    if result:
        return jsonify({"message":"user deleted successfully"})
    else:
        return jsonify({"message":"something went worng"}),500
        