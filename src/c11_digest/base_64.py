# -*- coding: UTF-8 -*-

import base64

a = base64.encodebytes(bytes("hello world", "utf-8"))
print(a)

a = base64.decodebytes(a)
print(a)
