# -*-coding:utf-8 -*-
"""
:创建时间: 2022/7/28 0:14
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
except ImportError:
    try:
        from PySide2.QtGui import *
        from PySide2.QtCore import *
        from PySide2.QtWidgets import *
    except ImportError:
        from PySide.QtGui import *
        from PySide.QtCore import *

try:
    from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
except:
    from PySide.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from cpform.widget.core import *
from maya_utils import decode_string, call_block

_bytes_t = type(b'')
_unicode_t = type('')


class HttpRequest(Warp):
    def __init__(self, child, url, method='GET', headers=dict(), data=b''):
        if type(method) == _unicode_t:
            method = method.encode('utf-8')
        if type(data) == _unicode_t:
            data = data.encode('utf-8')
        super(HttpRequest, self).__init__(child)
        self.manager = QNetworkAccessManager(self)
        self.manager.finished[QNetworkReply].connect(self.__call)
        request = QNetworkRequest(QUrl(url))
        for k, v in headers.items():
            request.setRawHeader(k, v)
        self.buffer_io = QBuffer()
        # self.buffer_io.setData(data)
        self.buffer_io.open(QBuffer.ReadWrite)
        self.buffer_io.write(data)
        self.buffer_io.seek(0)
        self.reply = self.manager.sendCustomRequest(
            request,
            method,
            self.buffer_io,
        )
        self.buffer_io.setParent(self.reply)

    @call_block
    def __call(self, reply):
        """
        :type reply: QNetworkReply
        :return:
        """
        print('reply:', reply)
        print('code: ', reply.attribute(QNetworkRequest.HttpStatusCodeAttribute))
        print('headers: ', {bytes(i): bytes(reply.rawHeader(i)) for i in reply.rawHeaderList()})
        print('data: ', repr(bytes(reply.readAll())))

    def httpStart(self, http_method, fn, url, headers=None):
        pass

    def httpEnd(self):
        pass

    def get(self, fn, url, headers=None):
        if headers is None:
            headers = dict()
        self.httpStart(u"GET", fn, url, headers)

        manager = QNetworkAccessManager(self)
        manager.finished[QNetworkReply].connect(self.replyWrap(fn))
        request = QNetworkRequest(QUrl(url))
        for k, v in headers.items():
            request.setRawHeader(k, v)
        manager.get(request)

    def post(self, fn, url, headers=None, data=b""):
        if headers is None:
            headers = dict()
        self.httpStart(u"POST", fn, url, headers)

        manager = QNetworkAccessManager(self)
        manager.finished[QNetworkReply].connect(self.replyWrap(fn))
        request = QNetworkRequest(QUrl(url))
        for k, v in headers.items():
            request.setRawHeader(k, v)
        manager.post(request, data)

    def put(self, fn, url, headers=None, data=b""):
        if headers is None:
            headers = dict()
        self.httpStart(u"PUT", fn, url, headers)

        manager = QNetworkAccessManager(self)
        manager.finished[QNetworkReply].connect(self.replyWrap(fn))
        request = QNetworkRequest(QUrl(url))
        for k, v in headers.items():
            request.setRawHeader(k, v)
        manager.put(request, data)

    def replyWrap(self, fn):
        @call_block
        def _(reply):
            try:
                headers = {bytes(i): bytes(reply.rawHeader(i)) for i in reply.rawHeaderList()}
                return fn(reply.attribute(QNetworkRequest.HttpStatusCodeAttribute),
                          headers,
                          bytes(reply.readAll()))
            finally:
                self.httpEnd()

        _.__name__ = fn.__name__
        return _
