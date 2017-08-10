#!/usr/bin/env python
# coding:utf8

from bottle import route, run, request, get, static_file
import uuid
import os
import os.path


UPLOAD_PATH_ROOT = os.path.join(os.getcwd(), 'files')


@route('/')
def index():
    return 'hello world'


@get('/files/<filepath:re:.+>')
def files(filepath):
    return static_file(filepath, root=UPLOAD_PATH_ROOT)


@get('/echo/<msg:re:.+>')
def echo(msg):
    return msg


@route('/remote', method='POST')
def do_remote_pic():
    head_url = request.params.get('head_url')
    face_url = request.params.get('face_url')
    print head_url, face_url
    dir_name = str(uuid.uuid1())
    full_path = os.path.join(UPLOAD_PATH_ROOT, dir_name)
    os.makedirs(full_path)
    head_path = os.path.join(full_path, 'head.jpg')
    face_path = os.path.join(full_path, 'face.jpg')
    os.popen('wget %s -o %s' % (head_url, face_path)).read()
    os.popen('wget %s -p %s' % (face_url, face_path)).read()
    os.popen('python faceswap.py %s' % (full_path)).read()
    return '/files/' + dir_name + '/output.jpg'


@route('/upload', method='POST')
def do_upload():
    head = request.files.get('head')
    face = request.files.get('face')
    print head, face
    if head and face:
        dir_name = str(uuid.uuid1())
        full_path = os.path.join(UPLOAD_PATH_ROOT, dir_name)
        os.makedirs(full_path)
        head.save(full_path + '/' + 'head.jpg')
        face.save(full_path + '/' + 'face.jpg')
        os.popen('python faceswap.py %s' % (full_path)).read()
        return '/files/' + dir_name + '/output.jpg'
    else:
        return 'no head or face'


run(host='127.0.0.1', port=8080, debug=True)
