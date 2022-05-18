from bll.SharesBasicBll import SharesBasicBll
from bll.SharesPriceBll import SharesPriceBll
from bll.SnowballBll import SnowballBll

if __name__ == '__main__':
    # 插入股票数据
    # SharesBasicBll.insert_shares_data()

    shares_nos = SharesBasicBll.select_available_no()
    for item in shares_nos:
        shares_quote_data = SnowballBll.quotec(item)
        SharesPriceBll.insert_price_data(shares_quote_data)

# sql_1 = "SELECT * from sa_price LIMIT 10;"
# sql_2 = "SELECT * from sa_price WHERE shares_no = %s LIMIT 0,3;"
# dao_helper = DaoHelper()
# print(dao_helper.select(sql=sql_1, is_more=True))
# print(dao_helper.select(sql=sql_2, arg=(600,), is_more=True))
