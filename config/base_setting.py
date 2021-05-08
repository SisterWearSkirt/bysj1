# -*- coding: utf-8 -*-
SERVER_PORT = 80 #8999
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = 'mooc_food'

SEO_TITLE = "Python Flask构建微信小程序订餐系统"
# 过滤url
IGNORE_URLS = {
    "^/user/login"
}

IGNORE_CHECK_LOGIN_URLS = {
    "^/static",
    "^/favicon.ico"
}


API_IGNORE_URLS = [
    "^/api"
]


PAGE_SIZE = 50
PAGE_DISPLAY =10


STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}
UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    'domain':'http://192.168.1.108:8999/user/login'
}


PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}