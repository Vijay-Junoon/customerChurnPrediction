from sqlalchemy import create_engine

database_url = (
    "postgresql+psycopg2://"
    "postgres:postgres@"
    "localhost:5432/"
    "customer_churn_db"
)

try:
    engine = create_engine(database_url)

    with engine.connect() as conn:
        print("Connected successfully!")

except Exception as e:
    print(e)