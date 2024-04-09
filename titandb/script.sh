nohup \
  /home/hfeng/code/YCSB/cmake-build-debug-node27/ycsb \
  -load -run -db rocksdb -P /home/hfeng/code/YCSB/workloads/workloada \
  -P /home/hfeng/code/YCSB/rocksdb/rocksdb.properties -s -statistics \
  -p threadcount=16 \
  >ycsb_rocksdb 2>&1 &

nohup \
  /home/hfeng/code/YCSB/cmake-build-debug-node27/ycsb \
  -load -run -db rocksdb -P /home/hfeng/code/YCSB/workloads/workloada \
  -P /home/hfeng/code/YCSB/rocksdb/rocksdb-blob.properties -s -statistics \
  -p threadcount=16 \
  >ycsb_rocksdb-blob 2>&1 &

nohup \
  /home/hfeng/code/YCSB/cmake-build-debug-node27/ycsb \
  -load -run -db titandb -P /home/hfeng/code/YCSB/workloads/workloada \
  -P /home/hfeng/code/YCSB/titandb/titandb.properties -s -statistics \
  -p threadcount=16 \
  >ycsb_titan 2>&1 &

nohup \
  /home/hfeng/code/YCSB/cmake-build-debug-node27/ycsb \
  -load -run -db titandb -P /home/hfeng/code/YCSB/workloads/workloada \
  -P /home/hfeng/code/YCSB/titandb/diffkv.properties -s -statistics \
  -p threadcount=16 \
  >ycsb_diffkv 2>&1 &

nohup \
  python3 /home/hfeng/code/YCSB/titandb/size_util.py 2053497 \
  >/dev/null 2>&1 &

nohup \
  python3 /home/hfeng/code/YCSB/titandb/cpu_util.py 2053497 \
  >/dev/null 2>&1 &


nohup \
  sudo -E \
  /home/hfeng/code/YCSB/cmake-build-debug-node27/ycsb \
  -load -run -db titandb -P /home/hfeng/code/YCSB/workloads/workloada \
  -P /home/hfeng/code/YCSB/titandb/aegonkv.properties -s -statistics \
  -p threadcount=16 \
  >ycsb_aegonkv 2>&1 &

nohup \
  sudo -E \
  python3 /home/hfeng/code/YCSB/titandb/size_util.py 1190842 \
  >/dev/null 2>&1 &

nohup \
  sudo -E \
  python3 /home/hfeng/code/YCSB/titandb/cpu_util.py 1190842 \
  >/dev/null 2>&1 &

sar -f /var/log/sysstat/sa21 -dp --dev=dev0-0 -s 00:00:00 -e 07:00:00

