import os
import dotenv
from sqlalchemy import create_engine, types

envpath = os.path.join(os.path.dirname(__file__), '../.env')
dotenv.load_dotenv(envpath)


class SingletonType(type):
    def __init__(self, *args, **kwargs):
        super(SingletonType, self).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)
        return obj


class Foo(metaclass=SingletonType):

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def eng(self):
        engine = create_engine('oracle://{username}:{password}@{host}:{port}/?service_name={service}'.format(
            username=os.getenv('oracle_username'),
            password=os.getenv('oracle_password'),
            host=os.getenv('oracle_host'),
            port=os.getenv('oracle_port'),
            service=os.getenv('oracle_service'),
            pool_size=os.getenv('oracle_pool_size'),
            max_overflow=os.getenv('oracle_max_overflow'),
            pool_timeout=os.getenv('oracle_pool_timeout')
        ))
        return engine


engine = Foo().eng()


def to_db(df, table_name, conn, chunksize=2000):
    _dtype = {
        c: types.VARCHAR(df[c].str.len().max()) for c in df.columns[df.dtypes == 'object'].to_list()
    }
    schema = os.getenv('oracle_schema')
    df.to_sql(table_name, conn, if_exists="append", chunksize=chunksize, index=False, schema=schema, dtype=_dtype)
