bert-base-serving-start \
    -model_dir /root/code/python/bert/output \
    -bert_model_dir /root/code/python/bert/chinese \
    -model_pb_dir /root/code/python/bert/output \
    -mode CLASS \
    -max_seq_len 128 \
    -http_port 8091 \
    -port 5575 \
    -port_out 5576 \
    -device_map 1 
