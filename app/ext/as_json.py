import json
from flask import Response
from functools import wraps

def as_json(f):
    """JSON RESPONSE => UTF-8
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        res = f(*args, **kwargs)
        res = json.dumps(res, ensure_ascii=False).encode('utf8')
        return Response(res, content_type='application/json; charset=utf-8')
    return decorated_function