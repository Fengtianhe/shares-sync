import time

from dao.SharesBasicDao import SharesBasicDao
from dao.SharesPriceDao import SharesPriceDao
from utils.DaoHelper import DaoHelper
import logging

from utils.DateUtil import DateUtil
from utils.TimeUtil import TimeUtil

dt = time.strftime('%Y%m%d', time.localtime())
logging.basicConfig(filename='run_' + str(dt) + '.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class SharesPriceBll:
    @staticmethod
    def insert_price_data(quotac_data):
        dt = DateUtil.today()
        shares_no = quotac_data['symbol']
        try:
            if TimeUtil.is_close_time():
                if SharesPriceDao.select_by_no_and_dt(shares_no, dt) is None:
                    logger.info("代码%s 在 %s 无数据，新增", shares_no, dt)
                    sql = "insert into sa_shares_price (shares_no, open_price, close_price, `range`, high_price, low_price, dt) value (%s ,%s, %s, %s, %s, %s, %s)"
                    dao_helper = DaoHelper()
                    dao_helper.execute(sql, arg=(shares_no, quotac_data['open'], quotac_data['current'],
                                                 quotac_data['percent'], quotac_data['high'], quotac_data['low'], dt))
                    dao_helper.close()
                else:
                    logger.info("代码%s 在 %s 有数据，更新", shares_no, dt)
                    sql = "update sa_shares_price set open_price = %s, close_price = %s, `range` = %s, high_price = %s, low_price = %s where shares_no = %s and dt = %s"
                    dao_helper = DaoHelper()
                    dao_helper.execute(sql, arg=(quotac_data['open'], quotac_data['current'],
                                                 quotac_data['percent'], quotac_data['high'], quotac_data['low'],
                                                 shares_no,
                                                 dt))
                    dao_helper.close()
        except Exception as e:
            logger.info("保存价格数据异常 入参 = %s, e = %s", quotac_data, e)
