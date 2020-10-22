# !/usr/bin/python3
# From https://github.com/sftcd/tek_transparency/
# --------------------------------------
import binascii
import TemporaryExposureKeyExport_pb2
import array

def count_keys_in_file (file_path):
    f = open(file_path, "rb")
    tek_key_export = TemporaryExposureKeyExport_pb2.TemporaryExposureKeyExport()
    header = f.read(16)
    # print("header:" + str(header))
    try:
        tek_key_export.ParseFromString(f.read())
    except:
        return -1
    f.close()
    print("file timestamps: start " + str(tek_key_export.start_timestamp) + ", end " + str(tek_key_export.end_timestamp))
    print("batch_num: " + str(tek_key_export.batch_num) + ", batch_size: " + str(tek_key_export.batch_size))
    print("region: " + str(tek_key_export.region))
    print("signature info:")
    print(str(tek_key_export.signature_infos))
    count = 0
    count_array = array.array('l',[0,1,2,3,4,5,6,7,8])
    for key in tek_key_export.keys:
        print(str(binascii.hexlify(key.key_data)) +
              str(key.rolling_start_interval_number) + ", period:" + str(key.rolling_period) +
              str(key.transmission_risk_level) + " Transmission Risk level:" + str(key.transmission_risk_level))
        if key.transmission_risk_level in {1,2,3,4,5,6,7,8}:
            count+=1
            count_array[key.transmission_risk_level] = count_array[key.transmission_risk_level] +1
    print("key:"+str(binascii.hexlify(key.key_data)))
    print("start interval: "+str(key.rolling_start_interval_number)+", period:"+str(key.rolling_period))
    print("transmission risk level: "+str(key.transmission_risk_level))
    return count_array

#0: Unused
# 1: Confirmed test - Low transmission risk level
# 2: Confirmed test - Standard transmission risk level
# 3: Confirmed test - High transmission risk level
# 4: Confirmed clinical diagnosis
# 5: Self report
# 6: Negative case
# 7: Recursive case
# 8: Unused/custom