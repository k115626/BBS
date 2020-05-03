from flask import jsonify


class HttpCode():
    ok = 200
    parameserror = 400
    servererror = 500


def restful_result(code, message, data):
    return jsonify({'code': code, 'message': message, 'data': data or {}})


def restful_success(message='', data=None):
    return restful_result(code=HttpCode.ok, message=message, data=data)


def restful_parameserror(message=''):
    return restful_result(code=HttpCode.parameserror, message=message, data=None)


def restful_servererror(message=''):
    return restful_result(code=HttpCode.servererror, message=message, data=None)


