class Config:
    SQLALCHEMY_DATABASE_URI = None
    server_name = "DESKTOP-FEL9AF1"
    database_name = "flask_gpx"
    username = "your_username"
    password = "your_password"

    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server"
