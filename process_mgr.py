from process import Process
from util.system_command import shell, write_stderr


class ProcessManager(object):
    """ProcessManager provides the manipulation of all the parent and child process"""

    def __init__(self):
        self.parent_process = []

    def cumulate_rss(self):
        designated_pids = map(lambda p: p.pid, self.parent_process)
        res = {}
        for p in self.get_all_process():
            if p.pid in designated_pids:
                res[p.pid] = res.get(p.pid, 0) + p.rss
            elif p.ppid in designated_pids:
                res[p.ppid] = res.get(p.ppid, 0) + p.rss
        return res

    def get_all_process(self):
        cmd = 'ps ax -o "pid= ppid= rss="'
        data = shell(cmd)
        res = []
        for row_data in data.splitlines():
            proc_detail = map(int, row_data.split())
            proc = Process(*proc_detail)
            yield proc

    def add_process(self, proc):
        self.parent_process.append(proc)

    def get_name(self, pid):
        for pp in self.parent_process:
            if pp.pid == pid:
                return pp.pname if pp.pname else 'None'
