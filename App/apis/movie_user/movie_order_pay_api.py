from flask_restful import Resource
from alipay import AliPay
from alipay.utils import AliPayConfig

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user.utils import login_required

app_private_key_string = open("/path/to/your/private/key.pem").read()
alipay_public_key_string = open("/path/to/alipay/public/key.pem").read()

app_private_key_string == """
    -----BEGIN RSA PRIVATE KEY-----
    base64 encoded content
    -----END RSA PRIVATE KEY-----
"""

alipay_public_key_string == """
    -----BEGIN PUBLIC KEY-----
    base64 encoded content
    -----END PUBLIC KEY-----
"""


class MovieOrderPayResource(Resource):
    @login_required
    def get(self, order_id):
        alipay = AliPay(
            appid="",
            app_notify_url=None,  # 默认回调 url
            app_private_key_string=app_private_key_string,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=alipay_public_key_string,
            sign_type="RSA",  # RSA 或者 RSA2
            debug=False,  # 默认 False
            verbose=False,  # 输出调试数据
            config=AliPayConfig(timeout=15)  # 可选，请求超时时间
        )

        # 如果你是 Python3 的用户，使用默认的字符串即可
        subject = "测试订单"

        # 电脑网站支付，需要跳转到：https://openapi.alipay.com/gateway.do? + order_string
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no="20161112",
            total_amount=0.01,
            subject=subject,
            return_url="https://example.com",
            notify_url="https://example.com/notify"  # 可选，不填则使用默认 notify url
        )
        pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string
        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": {
                "pay_url": pay_url,
                "order_id": order_id
            }
        }
        return data
