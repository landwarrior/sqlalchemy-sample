# sqlalchemy-sample
SQLAlchemyのサンプルコード

テーブル作成する際の default と server_default の挙動の違いを調べたかった

SQLAlchemy のバージョンをそれぞれ試したところ、どっちも以下の SQL が発行されるらしい

```sql
CREATE TABLE users (
        user_id INTEGER NOT NULL AUTO_INCREMENT,
        user_name VARCHAR(32) NOT NULL,
        user_kana VARCHAR(32) NOT NULL DEFAULT '',
        PRIMARY KEY (user_id)
)
```
