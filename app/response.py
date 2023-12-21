from flask import jsonify , make_response

def success_response(values,message):
    res ={
        'values':values,
        'message':message,
    }

    return make_response(jsonify(res),200)

def not_found_response(values,message):
    res ={
        'values':values,
        'message':message,
    }

    return make_response(jsonify(res),404)

def bad_request_response(values,message):
    res ={
        'values':values,
        'message':message,
    }

    return make_response(jsonify(res),400)
    