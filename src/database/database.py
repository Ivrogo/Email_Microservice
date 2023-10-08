import sqlite3


class database:
    def create_tables():
        # Inicializa la base de datos o la crea si no existe con SQLite
        db_conn = sqlite3.connect("notifications.db")
        db_cursor = db_conn.cursor()

        # Ejecutamos el archivo SQL para crear las tablas
        with open("create_tables.sql", "r") as sql_file:
            sql_script = sql_file.read()
            db_cursor.executescript(sql_script)

    def save_notification(notification_data):
        # Inicializa la base de datos o la crea si no existe con SQLite
        db_conn = sqlite3.connect("notifications.db")
        db_cursor = db_conn.cursor()

        notification_type = notification_data.get("type")

        if notification_type == "email":
            db_conn.cursor.execute(
                """
                              INSERT INTO emails_sent (recipient, subject, message) 
                              VALUES (?, ?, ?)
                              """,
                (
                    notification_data["recipient"],
                    notification_data["subject"],
                    notification_data["message"],
                ),
            )
        elif notification_type == "template":
            db_conn.cursor.execute(
                """
                              INSERT INTO email_templates (name, message) 
                              VALUES (?, ?)
                              """,
                (notification_data["name"], notification_data["message"]),
            )
        elif notification_type == "connection":
            db_conn.cursor.execute(
                """
                              INSERT INTO connections (user, password) 
                              VALUES (?, ?)
                              """,
                (notification_data["username"], notification_data["password"]),
            )

        db_conn.commit()
        db_conn.close()
