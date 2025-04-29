class Config:
    VERSION = "v1"
    EMAIL_USER = "admin@example.com"                # Your email id
    EMAIL_PASS = ""                                 # Your email password
    EMAIL_HOST = ""                                 # email host
    EMAIL_PORT = 993                                # ssl/non-ssl port
    EMAIL_PROTOCOL = ""                             # protocal : TODO - for future
    EMAIL_FOLDER = "Inbox"                          # Folder you want to read

    DB_TYPE = "mysql"                               # DB type: mysql, sqlite etc
    DB_HOST = "localhost"                           # DB host
    DB_PORT = 3306                                  # DB Port
    DB_NAME = "email_reader"                        # DB Name
    DB_USER = ""                                    # DB Username
    DB_PASS = ""                                    # DB password

    SOURCE_EMAIL = "complaints@example.com"         # source mail id, from whom you want to read mail.
