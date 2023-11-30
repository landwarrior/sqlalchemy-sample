import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()


def create_table(engine):
    Base.metadata.create_all(engine)


class Users(Base):
    """users テーブル定義."""

    __tablename__ = "users"

    user_id = sa.Column("user_id", sa.Integer, primary_key=True)
    user_name = sa.Column("user_name", sa.String(32), nullable=False, default="")
    user_kana = sa.Column("user_kana", sa.String(32), nullable=False, server_default="")
    # MySQL 8.0.32 では current_date にカッコを付けないといけない
    birth = sa.Column("birth", sa.Date, nullable=False, server_default=text("(CURRENT_DATE)"))
    # SQLAlchemy の current_date() で入るものはカッコがつかないので、エラーになる
    judgement_day = sa.Column("judgement_day", sa.Date, nullable=False, server_default=text("(CURRENT_DATE)"))
    created_at = sa.Column("created_at", sa.DateTime, nullable=False, server_default=current_timestamp())
    updated_at = sa.Column(
        "updated_at", sa.DateTime, nullable=False, server_detault=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )

    def __init__(
        self,
        user_id: int,
        user_name: str,
        user_kana: str,
        birth: datetime,
        judgement_day: datetime,
        created_at: datetime,
        updated_at: datetime,
    ):
        """コンストラクタ."""
        self.user_id = user_id
        self.user_name = user_name
        self.user_kana = user_kana
        self.birth = birth
        self.judgement_day = judgement_day
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        """文字列置き換え."""
        return "<{}({}, {}, {}, {}, {}, {}, {})>".format(
            self.__tablename__,
            self.user_id,
            self.user_name,
            self.user_kana,
            self.birth,
            self.judgement_day,
            self.created_at,
            self.updated_at,
        )
