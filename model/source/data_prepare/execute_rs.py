import sys, psycopg2
import datetime as dt


class ExecuteRS:

    def __init__(self, host, port, database, user, password):
        self.host = host,
        self.port = port,
        self.database = database,
        self.user = user,
        self.password = password

    def execute_script(self, script_file, params):
        '''
        :param script_file: script filename relative root
        :param params: dictionay of all params needed in script
        :return:
        '''

        rs_conn = psycopg2.connect(host=self.host,
                                   port=self.port,
                                   dbname=self.database,
                                   user=self.user,
                                   password=self.password)

        cursor = rs_conn.cursor()

        sqlfile = open(script_file, 'r')
        sqlfile = sqlfile.read()

        for key in params.keys():
            sqlfile = sqlfile.replace(key, params[key])

        start_time = dt.datetime.now()
        print("Start: ", start_time.isoformat())

        try:
            cursor.execute(sqlfile)
            cursor.execute("COMMIT;")

        except Exception as error:
            sys.exit('execute_script: ' + repr(error))
        finally:
            cursor.close()
            rs_conn.close()

        end_time = dt.datetime.now()
        print("End: ", end_time.isoformat())
