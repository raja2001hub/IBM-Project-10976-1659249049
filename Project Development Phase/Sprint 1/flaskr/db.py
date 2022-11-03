import ibm_db

dsn_hostname = ""
dsn_uid = ""
dsn_pwd = ""

dsn_driver = ""
dsn_database = ""
dsn_database = ""
dsn_port = ""
dsn_protocol = ""

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

print(dsn)