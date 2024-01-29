from flask import jsonify, make_response


def success(values, message):
    res = {"data": values, "message": message}

    return make_response(jsonify(res)), 200


def badRequest(values, message):
    res = {"data": values, "message": message}

    return make_response(jsonify(res)), 400


def internal_server_error(
    message="Sorry, seems like your input is not in right format",
):
    res = {
        "message": message,
    }

    return make_response(jsonify(res), 500)
