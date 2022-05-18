from utils.DaoHelper import DaoHelper


class SharesBasicDao:
    """
    获取所有的证券
    """

    @staticmethod
    def select_all_shares():
        dao_helper = DaoHelper()
        ret = dao_helper.select("select * from sa_shares_basic", is_more=True)
        dao_helper.close()
        return ret
