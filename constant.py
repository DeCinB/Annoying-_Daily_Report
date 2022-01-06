import os

USERS = eval(os.environ['USERS'])
SERVER_KEY = os.environ['SERVER_KEY']


LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login/check'
GET_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'

# 当今日没有填报时，在https://app.bupt.edu.cn/ncov/wap/default/index下进行填报，
# 全部填完，不要提交，f12打开控制台，在Console页面下输入代码 console.log(vm.info) 就会得到以下信息，之后每天就默认填以下信息
INFO = r"""{
        "address": "福建省福州市台江区苍霞街道台江区童乐幼儿园河下社区",
"area": "福建省 福州市 台江区",
"bztcyy": "4",
"city": "福州市",
"created": 1641348656,
"csmjry": "0",
"date": "20220105",
"geo_api_info": "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"fEa\":\"jsonp_793281_\",\"position\":{\"Q\":26.05243,\"R\":119.29818999999998,\"lng\":119.29819,\"lat\":26.05243},\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"0591\",\"adcode\":\"350103\",\"businessAreas\":[{\"name\":\"义洲\",\"id\":\"350103\",\"location\":{\"Q\":26.056271,\"R\":119.29725100000002,\"lng\":119.297251,\"lat\":26.056271}},{\"name\":\"宁化\",\"id\":\"350103\",\"location\":{\"Q\":26.059439,\"R\":119.29292199999998,\"lng\":119.292922,\"lat\":26.059439}},{\"name\":\"中亭街\",\"id\":\"350103\",\"location\":{\"Q\":26.053445,\"R\":119.30942199999998,\"lng\":119.309422,\"lat\":26.053445}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"河下街\",\"streetNumber\":\"24号\",\"country\":\"中国\",\"province\":\"福建省\",\"city\":\"福州市\",\"district\":\"台江区\",\"towncode\":\"350103007000\",\"township\":\"苍霞街道\"},\"formattedAddress\":\"福建省福州市台江区苍霞街道台江区童乐幼儿园河下社区\",\"roads\":[],\"crosses\":[],\"pois\":[]}",
"glksrq": "",
"gllx": "",
"gtjzzfjsj": "",
"gwszdd": "",
"id": 16569857,
"ismoved": 0,
"jcbhlx": "",
"jcbhrq": "",
"jchbryfs": "",
"jcjg": "",
"jcjgqr": "0",
"jcqzrq": "",
"jcwhryfs": "",
"jhfjhbcc": "",
"jhfjjtgj": "",
"jhfjrq": "",
"jrsfqzfy": "",
"jrsfqzys": "",
"mjry": "0",
"province": "福建省",
"qksm": "",
"remark": "",
"sfcxtz": "0",
"sfcxzysx": "0",
"sfcyglq": "0",
"sfjcbh": "0",
"sfjchbry": "0",
"sfjcqz": "",
"sfjcwhry": "0",
"sfjzdezxgym": 1,
"sfjzxgym": 1,
"sfsfbh": 0,
"sfsqhzjkk": 0,
"sftjhb": "0",
"sftjwh": "0",
"sfxk": 0,
"sfygtjzzfj": 0,
"sfyqjzgc": "",
"sfyyjc": "0",
"sfzx": 0,
"sqhzjkkys": "",
"szcs": "",
"szgj": "",
"szsqsfybl": 0,
"tw": "2",
"uid": "79673",
"xjzd": "福建福州",
"xkqq": "",
"xwxgymjzqk": 3,
"ymjzxgqk": "已接种",
"zgfxdq": "0"
        }"""

REASONABLE_LENGTH = 24
TIMEOUT_SECOND = 25

class HEADERS:
    REFERER_LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login'
    REFERER_POST_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
    ORIGIN_BUPTAPP = 'https://app.bupt.edu.cn'

    UA = ('Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
          'Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN')
    ACCEPT_JSON = 'application/json'
    ACCEPT_HTML = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    REQUEST_WITH_XHR = 'XMLHttpRequest'
    ACCEPT_LANG = 'zh-cn'
    CONTENT_TYPE_UTF8 = 'application/x-www-form-urlencoded; charset=UTF-8'

    def __init__(self) -> None:
        raise NotImplementedError

COMMON_HEADERS = {
    'User-Agent': HEADERS.UA,
    'Accept-Language': HEADERS.ACCEPT_LANG,
}
COMMON_POST_HEADERS = {
    'Accept': HEADERS.ACCEPT_JSON,
    'Origin': HEADERS.ORIGIN_BUPTAPP,
    'X-Requested-With': HEADERS.REQUEST_WITH_XHR,
    'Content-Type': HEADERS.CONTENT_TYPE_UTF8,
}

from typing import Optional
from abc import ABCMeta, abstractmethod

class INotifier(metaclass=ABCMeta):
    @property
    @abstractmethod
    def PLATFORM_NAME(self) -> str:
        """
        将 PLATFORM_NAME 设为类的 Class Variable，内容是通知平台的名字（用于打日志）。
        如：PLATFORM_NAME = 'Telegram 机器人'
        :return: 通知平台名
        """
    @abstractmethod
    def notify(self, *, success, msg, data,username, name) -> None:
        """
        通过该平台通知用户操作成功的消息。失败时将抛出各种异常。
        :param success: 表示是否成功
        :param msg: 成功时表示服务器的返回值，失败时表示失败原因；None 表示没有上述内容
        :return: None
        """

