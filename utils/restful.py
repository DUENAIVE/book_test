from django.http import JsonResponse


class HttpCode(object):
    ok = 200
    pageerror = 404
    methoderror = 405
    servererror = 500


def result(code, count, data=None,**kwargs):
    json_dict = {"code": 0, "count": count, "data": data,'msg':'success'}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict, json_dumps_params={'ensure_ascii': False})


def response_succeed(count, data=None):
    return result(code=0, count=count, data=data,status = 200)


def response_error(count, data=None):
    return result(code=0, count=count, data=data,status = 400)

