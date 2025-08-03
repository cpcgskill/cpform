# -*-coding:utf-8 -*-
"""
:创建时间: 2022/8/1 23:41
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division

import os
try:
    import maya
    def runtime():
        return 'maya'
except ImportError:
    try:
        import pymxs
        def runtime():
            return '3dsMax'
    except ImportError:
        try:
            import MaxPlus
            def runtime():
                return '3dsMax-OLD'
        except ImportError:
            def runtime():
                return 'standalone'

if runtime() == 'maya':
    import maya.cmds as mc
    import cpform._lib.maya_utils as maya_utils

    from maya.OpenMaya import MGlobal as MGlobal_api1

    def runtime_version():
        return int(eval(mc.about(lu=True))[1])

    def simple_output_exception_type_manager(typ):
        maya_utils.simple_output_ex_types.append(typ)
        return typ


    if MGlobal_api1.mayaState() == MGlobal_api1.kInteractive:
        def call_block(fn):
            if fn is None:
                raise ValueError('fn is not a callable object')
            return maya_utils.execute_deferred(maya_utils.call_block(fn))
    else:
        def call_block(fn):
            if fn is None:
                raise ValueError('fn is not a callable object')
            return fn
else:
    def runtime_version():
        return None


    def simple_output_exception_type_manager(typ):
        return typ
    def call_block(fn):
        if fn is None:
            raise ValueError('fn is not a callable object')
        return fn

_bytes_t = type(b'')
_unicode_t = type('')

def decode_string(s):
    u"""
    字符串解码函数

    :param s:
    :return:
    """
    if isinstance(s, _unicode_t):
        return s
    elif isinstance(s, _bytes_t):
        try:
            return s.decode("utf-8")
        except UnicodeDecodeError:
            try:
                return s.decode("GB18030")
            except UnicodeDecodeError:
                try:
                    return s.decode("Shift-JIS")
                except UnicodeDecodeError:
                    try:
                        return s.decode("EUC-KR")
                    except UnicodeDecodeError:
                        return _unicode_t(s)
    else:
        raise TypeError

__all__ = ['simple_output_exception_type_manager', 'call_block', 'decode_string', 'runtime', 'runtime_version']






