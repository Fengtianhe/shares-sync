import pysnowball as ball

ball.set_token("xq_a_token=93613ef2dc688245d6f2ef8b913d9525607d4717;")


class SnowballBll:

    @staticmethod
    def quotec(share_no):
        shares_quote_data = ball.quotec(share_no)
        return shares_quote_data['data'][0]
