from cryptography.fernet import Fernet # decode keys
import os



class Secrets:
    """Secrets allows you to specify a platform and db to return uid and pwd"""
    def __init__(self, platform):
        self.platform = platform


    def get_key(self):
        try:
            if self.platform == 'mssql': # reference to AIW SQL Server
                key = os.getenv('MSSQL_SERVER_ADMIN_KEY') # get my Env Variable for hash key
            elif self.platform =='db2_application': # reference to DB2 vos account:
                key =os.getenv('DB2_APPLICATION_KEY') # get my Env Variable for hash key
            elif self.platform =='db2_acf2': # reference to my personal acf2 access
                key = os.getenv('DB2_ACF2_KEY') # get my Env Variable for hash key
            return key
        except UnboundLocalError:
            print("you did not enter a valid platform")

    def uid_pwd(self):
        if self.platform =='mssql':
            uid = b'gAAAAABbF5kb9ciJRcqUAlQRf1JcNXFqUjysO12-eZAXaC-4MF_MB1DkDmnIab8QR1Rjwd_dawU9ZFjx9GtwLDqOmc52wvSFlA=='
            pwd = b'gAAAAABbF5ksNLEc67ddcCxVmThaI_Zy7D1zAWQrHVeDIOmQiPLQ057OX41opPl9jMIpmK4rXogU1GESMcXUBud5p4xiR35nxg=='
        elif self.platform == 'db2_application':
            uid = b'gAAAAABZQC0FDZg7MkU1mmLg20yxqjSyElehOMS13f9EHuOG72fcvy9pUQW8pnkYicxuDqEGbPWLecDdNMlXUpA4TydINWqDgQ=='
            pwd = b'gAAAAABZQC0dmzYoVZ6rXXOVoJmMzhxBT0ZwDbLCVe1yMN1i9h4oByo2-7ahEyLDH6SPTJ70bb4xFqxtg_2qK-rzstAMRLHTiw=='
        elif self.platform == 'db2_acf2':
            uid = b'gAAAAABa_C9lMpEMfA2nnyzUKvQxSEz38fALl-RcNqreT8lhKy3deRjULqigi7QcCWLa8rgUkxKKhu0iIRyF5fNBWvMurZ70WA=='
            pwd = b'gAAAAABa_C9l0UoydfvwoxXUTKOI3e643RQTCNz71iwJUdeEeWuARYfd3NnjUm1Z0DrRrZkEeAUSyLdBBjiIMkH-x7h1IRZ_ww=='
        return (uid, pwd)

    def db_creds(self):
        db_key = Fernet(self.get_key()) # read in Key
        db_uid = db_key.decrypt(self.uid_pwd()[0]).decode() # decrypt username
        db_pwd = db_key.decrypt(self.uid_pwd()[1]).decode() # decrypt password
        return (db_uid, db_pwd) # return tuple