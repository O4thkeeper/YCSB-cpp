
nohup \
  /home/hfeng/code/YCSB/cmake-build-debug-node27/ycsb \
  -load -run -db rocksdb -P /home/hfeng/code/YCSB/workloads/workloada \
  -P /home/hfeng/code/YCSB/rocksdb/rocksdb.properties -s -statistics \
  -p threadcount=5 \
  >ycsb_rocksdb 2>&1 &

nohup \
  sudo -E \
  /home/hfeng/code/YCSB/cmake-build-debug-node27/ycsb \
  -load -run -db titandb -P /home/hfeng/code/YCSB/workloads/workloada \
  -P /home/hfeng/code/YCSB/titandb/titandb.properties -s \
  >ycsb_titan 2>&1 &

nohup \
  /home/hfeng/code/YCSB/cmake-build-debug-node27/ycsb \
  -load -run -db titandb -P /home/hfeng/code/YCSB/workloads/workloada \
  -P /home/hfeng/code/YCSB/titandb/titandb.properties -s -statistics \
  -p threadcount=5 \
  >ycsb_titan 2>&1 &

nohup \
  python3 /home/hfeng/code/YCSB/titandb/cpu_util.py 257317 \
  >/dev/null 2>&1 &

nohup \
  python3 /home/hfeng/code/YCSB/titandb/size_util.py 257317 \
  >/dev/null 2>&1 &

sar -f /var/log/sysstat/sa31 -dp --dev=dev0-0 -s 00:00:00 -e 00:42:59

nohup \
  sudo -E \
  python3 /home/hfeng/code/YCSB/titandb/size_util.py 6591 \
  >/dev/null 2>&1 &

nohup \
  sudo -E \
  python3 /home/hfeng/code/YCSB/titandb/cpu_util.py 6591 \
  >/dev/null 2>&1 &

nohup \
  env XRT_INI_PATH=/home/hfeng/code/titan/hardware/kernel/xrt.ini \
  sudo -E \
  /home/hfeng/code/YCSB/cmake-build-debug-node27/ycsb \
  -load -run -db titandb -P /home/hfeng/code/YCSB/workloads/workloada \
  -P /home/hfeng/code/YCSB/titandb/titandb.properties -s \
  >ycsb_titan 2>&1 &
