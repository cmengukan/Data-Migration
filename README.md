# Data Migration Project

This project demonstrates how to migrate data between two databases using Python and SQL.

## Setup

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Configure source and target databases in `config/source_config.py` and `config/target_config.py`.

3. Create target tables:

    ```bash
    psql -U target_user -d target_database -f sql/create_tables.sql
    ```

4. Run the migration script:

    ```bash
    python migrate_data.py
    ```

