class Process(object):
    """Process class contains the parameter of a process"""

    def __init__(self, pid, ppid=0, rss=0, vsz=0, pname=None):
        self.pid = pid
        self.ppid = ppid
        self.rss = rss
        self.vsz = vsz
        self.pname = pname

    def __str__(self):
        return str(self.__dict__)
