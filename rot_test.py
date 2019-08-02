import requests
import base64
import traceback
import shutil
import os
import time
import timeit

host = '152.63.4.80'
port = 5003
route = 'sdk'
# data = {
#     'static_path': str(static_input_path),
#     'file_name': file_name
# }

# file_path = './input/' + file_name

for file_name in os.listdir('./files_rot'):
    # file_name = '2000476171.pdf'
    print(file_name)
    file_path = './files_rot/' + file_name
    file_data = open(file_path, 'rb')
    file_path_out = './files_rot_output/' + file_name

    data = {'file_data': file_data, 'file_name': file_name}
    response = requests.post(f'http://{host}:{port}/{route}', files=data)
    print(type(response))
    sdk_output = response.json()
    print(type(sdk_output))
    print(sdk_output.keys())
    try:
        pdf = base64.b64decode(sdk_output['blob'])
        print('filepath to save', file_path_out)
        start = timeit.default_timer()
        # while(True):
        #     time.sleep(3)
        # try:
        #     os.remove(file_path)
        #     print('succes in removce')
        #     stop = timeit.default_timer()
        #     print('Time taken by abbyy to leave file: ', stop - start)
        # except Exception as e:
        #     print(e)
        #     print('error in remove')
        # time.sleep(3)
        with open(file_path_out, 'wb') as f:
            f.write(pdf)
        # time.sleep(3)
        print('success')
    except:
        traceback.print_exc()
        print('no blob data')

    # unique_id = file_path.stem
    # shutil.copyfile(file_path,  'o_' + file_name)
    # shutil.move(file_path, file_name)

