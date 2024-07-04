import pandas as pd
from sqlalchemy import create_engine
from config.source_config import SOURCE_DB_CONFIG
from config.target_config import TARGET_DB_CONFIG


def get_connection_string(config):
    return f"{config['dialect']}://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"


def migrate_data():
    source_conn_str = get_connection_string(SOURCE_DB_CONFIG)
    target_conn_str = get_connection_string(TARGET_DB_CONFIG)

    source_engine = create_engine(source_conn_str)
    target_engine = create_engine(target_conn_str)

    with source_engine.connect() as source_conn, target_engine.connect() as target_conn:
        query = open('sql/migration_queries.sql', 'r').read()
        df = pd.read_sql(query, source_conn)

        df.to_sql('Users', target_conn, if_exists='append', index=False)
        print(f"{len(df)} rows migrated successfully.")


if __name__ == '__main__':
    migrate_data()
