from models import create_table
from sqlalchemy import create_engine


def main():
    engine = create_engine("mysql+pymysql://root:root@192.168.33.20/testdb?charset=utf8mb4", echo=True)
    create_table(engine)


if __name__ == "__main__":
    main()
