import utils.s3_manager as ut
import sys, os
from datetime import datetime

if __name__ == "__main__":

    if sys.argv[1] == 'PROCESS1':
        pass

    my_param = sys.argv[1]
    my_bucket = os.environ["BUCKET_NAME"]

    now = datetime.now()
    str_date = now.strftime("%Y%m%d_%H%M%S")
    file_name = f"demo_test_{str_date}_{my_param}.txt"

    f = open(file_name, "w")
    f.write("nuevo archivo")
    f.write(str_date)
    f.close()

    key_file = "datalake/tempo-data/" + file_name

    ut.load_to_s3(my_bucket, key_file, file_name)

    print(f"upload file in: {my_bucket}/{key_file}")

    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"remove file : {file_name}")


