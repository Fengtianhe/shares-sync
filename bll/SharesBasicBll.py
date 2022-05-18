from dao.SharesBasicDao import SharesBasicDao
from utils.DaoHelper import DaoHelper
import logging

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class SharesBasicBll:
    """
    获取需要同步的证券编码
    """

    @staticmethod
    def select_available_no():
        shares = SharesBasicDao.select_all_shares()
        logging.info("取出全部股票代码 共%s条", len(shares))
        shares = list(
            filter(lambda item: not (item['name'].startswith("ST") or item['name'].startswith('*ST')), shares))
        logging.info("过滤ST股票代码 共%s条", len(shares))

        shares = list(filter(lambda item: not item['shares_no'].startswith("300", 2, 5), shares))
        logging.info("过滤创业板股票代码 共%s条", len(shares))

        shares = list(filter(lambda item: not item['shares_no'].startswith("688", 2, 5), shares))
        logging.info("过滤科创板股票代码 共%s条", len(shares))

        return [i_item['shares_no'] for i_item in shares]

    """
    写入股票数据
    """

    @staticmethod
    def insert_shares_data():
        dao_helper = DaoHelper()
        with open("resources/data.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                arr = line.split(" ")
                dao_helper.execute(sql="insert into sa_shares_basic value (%s, %s)", arg=(arr[0], arr[1]))
                print(arr[0], arr[1])
