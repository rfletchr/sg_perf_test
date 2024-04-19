from centos:7
run yum install -y python3 wget unzip
run mkdir /test
workdir /test
run python3 -m venv venv
run /test/venv/bin/pip install --upgrade pip
run wget https://github.com/shotgunsoftware/python-api/archive/refs/heads/master.zip
run unzip master.zip
run /test/venv/bin/pip install /test/python-api-master
copy test.py /test
cmd /test/venv/bin/python /test/test.py