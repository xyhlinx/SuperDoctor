import sys
import os
import time
from util.system_command import write_stderr, write_stdout
from supervisor import childutils
from process_mgr import ProcessManager
from process import Process


def ev_formatting(raw_data):
    data = raw_data.split()
    return {k: v for k, v in row_formatting(iter(data))}


def row_formatting(iter_data):
    for row_data in iter_data:
        data = row_data.split(':')
        yield data[0], data[1]


def get_timestamp():
    return time.strftime('%Y/%m/%d %H:%M:%S')


def super_doctor():
    rpc_iface = childutils.getRPCInterface(os.environ)
    process_mgr = ProcessManager()

    while 1:
        # transition from ACKNOWLEDGED to READY
        write_stdout('READY\n')

        # read header line and print it to stderr
        line = sys.stdin.readline()
        # write_stderr(line)

        # read event payload and print it to stderr
        headers = dict([x.split(':') for x in line.split()])
        raw_data = sys.stdin.read(int(headers['len']))
        ev = ev_formatting(raw_data)
        # write_stderr(str(ev))

        if 'processname' in ev:
            try:
                pname = ev['processname']
                process_info = rpc_iface.supervisor.getProcessInfo(pname)
                p = Process(pid=process_info['pid'], ppid=process_info['pid'], pname=pname)
                write_stderr(str(p))
                process_mgr.add_process(p)
            except Exception as err:
                write_stderr('a bad ev object process\n')
                write_stderr(str(err))
                write_stderr(str(ev))

        res = process_mgr.cumulate_rss()
        write_stderr(get_timestamp() + '\t' + str(res) + '\n')

        # transition from READY to ACKNOWLEDGED
        write_stdout('RESULT 2\nOK')


if __name__ == '__main__':
    super_doctor()
