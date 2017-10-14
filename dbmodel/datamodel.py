

from dbbase import BaseModel
from sql_tpl import SQL_TPL
from logger import logger


class DataModel(BaseModel):

    def get_data(self, dims=None, args={}):

        sql = SQL_TPL.get(dims, None)

        if not sql:
            logger.warning('Not Found sql')
            return []

        sql = sql % args

        data = self.mysql_db.query_list(sql=sql)
        return data

if __name__ == '__main__':

    db = DataModel()

    params = {
        'sdate': '2017-10-14',
        'edate': '2017-10-14'
    }

    print db.get_data(dims='chart1', args=params)