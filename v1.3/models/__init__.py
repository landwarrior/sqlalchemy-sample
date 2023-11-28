import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_table(engine):
    Base.metadata.create_all(engine)


class Users(Base):
    """users テーブル定義."""

    __tablename__ = "users"

    user_id = sa.Column("user_id", sa.Integer, primary_key=True)
    user_name = sa.Column("user_name", sa.String(32), nullable=False, default="")
    user_kana = sa.Column("user_kana", sa.String(32), nullable=False, server_default="")

    def __init__(self, user_id: int, user_name: str, user_kana: str):
        """コンストラクタ."""
        self.user_id = user_id
        self.user_name = user_name
        self.user_kana = user_kana

    def __repr__(self):
        """文字列置き換え."""
        return "<{}({}, {}, {})>".format(
            self.__tablename__,
            self.user_id,
            self.user_name,
            self.user_kana,
        )
