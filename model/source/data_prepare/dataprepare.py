import sys, os
import datetime as dt
import logging
import psycopg2


class DataPrepare:

    # Setup logging
    log = logging.getLogger(__name__)
    log.setLevel(level=logging.INFO)
    logging.basicConfig(level=logging.INFO)

    # script file name
    script_data_orders = 'scripts/script_prepare.sql'

    @staticmethod
    def log_file_env():
        # origin folder
        local_folder = os.path.dirname(os.path.abspath(__file__))
        # LOG Files
        log_file_app = 'log_app.log'
        local_log_dir = os.path.join(local_folder, 'Log')
        return os.path.join(local_log_dir, log_file_app)

    def __init__(self, host, port, database, user, password, log_file=""):
        self.rs_conn = psycopg2.connect(host=host,
                                        port=port,
                                        dbname=database,
                                        user=user,
                                        password=password)

        if log_file == "":
            log_file = self.log_file_env()
        fh = logging.FileHandler(log_file, mode='w')
        self.log.addHandler(fh)

    def execute_script(self, script_file, params):
        """
        Execute script file
        :param script_file:
        :param params:
        :return:
        """
        self.log.info('execute_script: Start... ')
        self.log.info(f'Script file: {script_file}, params:{params}')
        cursor = self.rs_conn.cursor()

        sql_file = open(script_file, 'r')
        sql_file = sql_file.read()

        for key in params.keys():
            sql_file = sql_file.replace(key, params[key])

        start_time = dt.datetime.now()
        self.log.info(f'Execute: Start at {start_time.isoformat()}')

        try:
            cursor.execute(sql_file)
        except Exception as error:
            sys.exit('execute_script: ' + repr(error))

        cursor.close()
        end_time = dt.datetime.now()
        self.log.info(f'execute_script: End at {end_time.isoformat()}')

    def do_something(self):
        """
        TO DO : do something script
        :return:
        """
        self.log.info('do something: Start... ')
        pass
