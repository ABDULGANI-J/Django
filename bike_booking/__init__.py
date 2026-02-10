import pymysql

# Patch version for Django compatibility
pymysql.__version__ = "2.2.1"
pymysql.version_info = (2, 2, 1)

pymysql.install_as_MySQLdb()
