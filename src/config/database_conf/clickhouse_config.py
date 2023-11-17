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
            f"clickhouse+native://{self.CLICKHOUSE_USER}:{self.CLICKHOUSE_PASSWORD}@"
            f"{self.CLICKHOUSE_HOST}:{self.CLICKHOUSE_PORT}/{self.CLICKHOUSE_DBNAME}"
        )


settings_db = ClickHouseConfig()
