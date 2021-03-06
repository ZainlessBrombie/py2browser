import base64
import datetime
import hashlib
import json
import socket
import threading
from collections import OrderedDict
from decimal import Decimal
import http.server as server_class
import inspect
import os
pd = None
pd_series_type = None
pd_data_frame_type = None

try:
    import pandas as pd
    pd_series_type = pd.Series
    pd_data_frame_type = pd.DataFrame
except ModuleNotFoundError:
    pass

builtin_names = {'__name__', '__main__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__cached__', '__file__'}

stuff = "test123sjdbjhvdbfjhvdjvhsjhffff ffffffffffffffffffffffff ffffffffffffffffffvtes t123sjdbjhvdbfjhvdjvhsjhfffffffffffffffffffff fffffffffffffffffffffffffvtest123s jdbjhvdbfjhvdjvhsjhffffffffffffffff ffffffffffffffffffffffffffffffv test123sjdbjhvdbfjhvdjvhsjhfffffffffffffff fffffffffffffffffffffffffffffffvtest123sjdbjhvdbfjhvdjvhsjh ffffffffffffffffffffffffffffffffffffffffffffffv"
array_example = [1, [2, [3, [4, [5, [6, [7]]]]]]]
byte_test = b'abckgsnjn'
multilist_tets = [{'other': [], 'working': {'testvalue': {'still': 'ok', 'this': {'is': 'not', 'wait': {'what': '?'}}}}, 'dofj': 'gdfj'},{'jkdkgfb': 'dgfjh', 'dofj': 'gdfj'},{'jkdkgfb': 'dgfjh', 'dofj': 'gdfj'},{'jkdkgfb': 'dgfjh', 'dofj': 'gdfj'}]
f = open('/home/mathis/examples.desktop')
n = None


def test():
    series = pd.Series(['entry '+str(x) for x in range(0,100)])
    a = 'a'
    b = {'a': 2, 's': series}
    c = [1, 2, {"x": "y"}]
    mirror(wait_input=True)


def mirror(scope=None, **options):
    captured_scope = scope
    if captured_scope is None:
        frame = inspect.currentframe().f_back
        captured_scope = {**frame.f_globals, **frame.f_locals}

    def run():
        port = 8081
        if 'port' in options:
            port = int(options['port'])
        local_server = server_class.HTTPServer(('localhost', port), instance_for(captured_scope))
        print('Serving on http://localhost:8081')
        local_server.serve_forever(0.1)
    thread = threading.Thread(target=run)
    thread.setDaemon(True)
    thread.start()
    if 'wait_input' in options and options['wait_input']:
        print('Press enter to continue')
        input()


class _CachingToJson:
    cache = {}

    def to_json(self, value):
        new_cache = {}
        _to_json(value, None, new_cache)
        self.cache = new_cache

    def re_obtain(self, object_id):
        if object_id in self.cache:
            return self.cache[object_id]
        return None

    def get_range(self, object_id, start, end):
        if object_id not in self.cache:
            return None
        o = self.cache[object_id]
        if type(o) is pd_series_type:
            pass # TODO


def _to_json(value, visited=None, id_map=None):
    if id_map is not None and value is not None:
        id_map[id(value)] = value
    if visited is None:
        visited = []
    else:
        visited = [*visited]
    if id(value) in visited:
        return {'type': 'recursion', 'id': id(value), 'data': {'value': -(len(visited) - visited.index(id(value)))}}
    visited.append(id(value))
    if value is None:
        return {'type': 'none', 'data': {}, 'id': 0}
    if type(value) is str:
        return {'type': 'string', 'id': id(value), 'data': {'value': value}}
    if type(value) is int or type(value) is float:
        return {'type': 'number', 'id': id(value), 'data': {'value': str(value), 'subtype': ('int' if (type(value) is int) else 'float')}}
    if type(value) in {list, set, tuple}:
        type_map = {list: 'list', set: 'set', tuple: 'tuple'}
        return {'type': 'collection',
                'id': id(value),
                'data': {
                    'subtype': type_map[type(value)],
                    'value': list(map(lambda entry: _to_json(entry, visited, id_map), list(value)))}}
    if type(value) is pd_series_type:
        return {'type': 'pandas_series', 'id': id(value), 'data':
            {'value': list(map(lambda entry: _to_json(entry, visited, id_map), list(value[:1000]))), 'dtype': str(value.dtype), 'full_length': len(value)}}
    if type(value) is Decimal:
        return {'type': 'number', 'id': id(value), 'data': {'value': str(value), 'subtype': 'decimal'}}
    if value is None:
        return {'type': 'number', 'id': id(value), 'data': {}}
    if type(value) is bool:
        return {'type': 'boolean', 'id': id(value), 'data': {'value': str(value)}}
    if type(value) is dict or type(value) is OrderedDict:
        append = []
        for key in value:
            append.append({
                'key': _to_json(key, visited, id_map),
                'value': _to_json(value[key], visited, id_map)
            })
        return {'type': 'map', 'id': id(value), 'data': {'subtype': ('dict' if (type(value) is dict) else 'ordered_dict'), 'value': append}}
    if type(value) is type:
        return {'type': 'type', 'id': id(value), 'data': {'value': str(value)[slice(len('<class \''), -len('\'>'))]}}
    if str(type(value)) == '<class \'function\'>':
        return {'type': 'function', 'id': id(value), 'data': {'to_string': str(value), 'module': str(value.__module__), 'filename': str(value.__code__.co_filename), 'arg_count': int(value.__code__.co_argcount)}}
    if type(value) is datetime.date:
        return {'type': 'datetime', 'id': id(value), 'data': {'value': value.isoformat(), 'zoned': False, 'subtype': 'date'}}
    if type(value) is datetime.time:
        return {'type': 'datetime', 'id': id(value), 'data': {'value': value.isoformat(), 'zoned': False, 'subtype': 'time'}}
    if type(value) is datetime.datetime:
        return {'type': 'datetime', 'id': id(value), 'data': {'value': value.isoformat(), 'zoned': False, 'subtype': 'datetime'}}
    if str(type(value)) == '<class \'module\'>':
        return {'type': 'module', 'id': id(value), 'data': {'to_string': str(value), 'name': value.__name__}}
    if type(value) is bytes:
        return {'type': 'bytes', 'id': id(value), 'data': {'value': base64.b64encode(value).decode('utf-8'), 'len': len(value)}}
    import _io
    if type(value) is _io.TextIOWrapper:
        return {'type': 'stream', 'id': id(value), 'data': {'name': value.name, 'mode': value.mode, 'encoding': value.encoding, 'closed': value.closed}}

    return {'type': 'unsupported', 'id': id(value), 'data': {'type': str(type(value)), 'to_string': str(value)}}


def instance_for(scope):
    class HttpHandler(server_class.BaseHTTPRequestHandler):
        _header_buf = []

        def _header(self, key, value):
            self._header_buf.append((key, value))

        def _finish(self, code, content):
            if type(content) is str:
                content = content.encode('utf-8')
            self.wfile.write(b'HTTP/1.0 '+str(code).encode('utf-8')+b' STATUS_NYI\r\n')
            self.wfile.write(b'content-length: '+str(len(content)).encode('utf-8')+b'\r\n')
            for header in self._header_buf:
                self.wfile.write(header[0].encode('utf-8') + b': ' + header[1].encode('utf-8'))
                self.wfile.write(b'\r\n')
            self._header_buf.clear()
            self.wfile.write(b'\r\n')

            self.wfile.write(content)
            self.wfile.flush()

        def _verify_local(self):
            self._header('access-control-allow-origin', '*')
            if self.client_address[0] != 'localhost' and self.client_address[0][:3] != '127':
                self._finish(401, 'You are not recognized as localhost/127. Requests need to be made from the same computer, towards localhost.')
                return True
            return False

        def _get_data(self):
            content_length = int(self.headers['Content-Length'])
            return self.rfile.read(content_length)

        def do_OPTIONS(self):
            if self._verify_local():
                return
            self._header('allow', 'OPTIONS, GET, POST')
            self._header('Access-Control-Allow-Headers', 'Content-Type, Content-Length')
            self._finish(200, '')

        def do_GET(self):
            if self._verify_local():
                return
            if self.path == '/api/v1/variables':
                ret = {}
                for var in scope:
                    if var not in builtin_names:
                        ret[var] = _to_json(scope[var])
                self._finish(200, json.dumps({'vars': ret, 'hash': hashlib.md5(json.dumps(ret).encode('utf-8')).hexdigest()}))
                return
            if self.path.startswith('/api'):
                self._finish(404, '{"message": "That path could not be found"}')
                return
            dir_name = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # script directory
            if dir_name[-1] == '/':
                dir_name = dir_name[:-1]
            path_part = self.path[:self.path.index('?')] if '?' in self.path else self.path
            try:
                try:
                    f = open(dir_name + '/dist/' + path_part.replace('..', ''))
                    content = f.read()
                    f.close()
                except IsADirectoryError:
                    f = open(dir_name + '/dist/' + path_part.replace('..', '') + '/index.html')
                    path_part = path_part.replace('..', '') + '/index.html'
                    content = f.read()
                    f.close()
            except FileNotFoundError:
                self._header('content-type', 'application/json')
                self._finish(404, '{"message": "Could not find file"}')
                return
            except IsADirectoryError:
                self._header('content-type', 'application/json')
                self._finish(404, '{"message": "That\'s a directory. No."}')
                return
            if '.png' in path_part:
                self._header('content-type', 'image/png')
            elif '.jpg' in path_part or '.jpeg' in path_part:
                self._header('content-type', 'image/jpeg')
            elif '.html' in path_part or '.htm' in path_part:
                self._header('content-type', 'text/html')
            elif '.js' in path_part:
                self._header('content-type', 'application/javascript')
            elif '.css' in path_part:
                self._header('content-type', 'text/css')
            else:
                print('Unknown content type: '+path_part+' from '+self.path)
                self._header('content-type', 'binary/octet-stream')
            self._finish(200, content)
            return

        def do_POST(self):
            print(self._get_data())
    return HttpHandler


test()

