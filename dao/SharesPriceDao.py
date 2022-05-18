from utils.DaoHelper import DaoHelper


class SharesPriceDao:
    """
    获取所有的证券
    """

    @staticmethod
    def select_by_no_and_dt(share_no, dt):
        dao_helper = DaoHelper()
        ret = dao_helper.select(sql="select * from sa_shares_price where shares_no = %s and dt = %s",
                                arg=(share_no, dt),
                                is_more=False)
        dao_helper.close()
        return ret
