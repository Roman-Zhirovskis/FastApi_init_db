from typing import Optional

from pydantic_settings import BaseSettings


class ClickHouseConfig(BaseSettings):
    CLICKHOUSE_USER: str
    CLICKHOUSE_HOST: str
    CLICKHOUSE_PASSWORD: str
    CLICKHOUSE_PORT: str 
    CLICKHOUSE_DBNAME: str

    @property
    def database_url(self) -> Optional[str]:
        return (
            f'clickhouse+native://{self.CLICKHOUSE_USER}:{self.CLICKHOUSE_PASSWORD}@'
            f'{self.CLICKHOUSE_HOST}:{self.CLICKHOUSE_PORT}/{self.CLICKHOUSE_DBNAME}'
        )


settings_db = ClickHouseConfig()

# Client(host='xx.xx.xx.xx', port='9000', database='data_name', user='default', password='123456')
# connect('clickhouse://default:123456@xx.xx.xx.xx:9000/data_base_name') "clickhouse+native://{user}:{db_password}@{db_host}:{db_port}/{data_base_name}"
# host – host with running ClickHouse server.

# port – port ClickHouse server is bound to. Defaults to 9000 if connection is not secured and to 9440 if connection is secured.

# database – database connect to. Defaults to 'default'.

# user – database user. Defaults to 'default'.

# password – user’s password. Defaults to '' (no password).
# 
# 
# 
# class ConfigDataBase(BaseSettings):  uri = 'clickhouse+native://default:@localhost/default'
#     POSTGRES_USER: str
#     POSTGRES_PASSWORD: str
#     POSTGRES_HOST: str
#     POSTGRES_PORT: str
#     POSTGRES_DB: str
#     DB_ECHO_LOG: bool

#     @property
#     def database_url(self) -> Optional[PostgresDsn]:
#         return (
#             f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
#             f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
#         )


# settings_db = ConfigDataBase()
