#-*- coding: utf-8 -*-

import psutil
from pprint import pprint
import  datetime
class SysInfoMonitor(object):
    # change bytes to GB
    def bytes_to_gb(self,data,key=""):
            return round(data/(1024**3),2)

    '''
    ###########################################
    svmem(percent, num, count,status,times)
    ###########################################

    '''
    def cpuinfo(self):
        data = dict(
        percent_avg = psutil.cpu_percent(interval=0, percpu=False),
        percent_per = psutil.cpu_percent(interval=0, percpu=True),
        num_p =psutil.cpu_count(logical=False),
        num_l= psutil.cpu_count(logical=True)
        )
        return data


    '''
    ###########################################
    svmem(total, available, percent, used, free
    ###########################################

    '''
    def meminfo(self):
        meminfo = psutil.virtual_memory()
        data = dict(
            total = self.bytes_to_gb(meminfo.total),
            used = self.bytes_to_gb(meminfo.used),
            free = self.bytes_to_gb(meminfo.free),
            percent = meminfo.percent
        )
        return data
    '''
    ################################################
    swap info (total, used, free, percent, sin, sout)
    ################################################

    '''
    def swapinfo(self):
        swapinfo = psutil.swap_memory()
        data = dict(
            total=self.bytes_to_gb(swapinfo.total),
            used=self.bytes_to_gb(swapinfo.used),
            free=self.bytes_to_gb(swapinfo.free),
            percent=swapinfo.percent
        )
        return data
    '''
    ################################################
    swap info (sdiskpart)
    ################################################

    '''
    def diskinfo(self):
        diskinfo = psutil.disk_partitions()
        list = [
            dict(
                device=v.device,
                mountpoint=v.mountpoint,
                fstype=v.fstype,
                opts=v.opts,
                used = psutil.disk_usage(v.mountpoint)
            )
            for v in diskinfo
        ]
        return diskinfo
    '''
    ################################################
    swap info (family,address,netmask,broadcast,ptp)
    ################################################
    '''
    def netinfo(self):
        addrs = psutil.net_if_addrs()
        addrs_info = {
            k: [
                dict(
                    family=val.family.name,
                    address=val.address,
                    netmask=val.netmask,
                    broadcast=val.broadcast
                )
                for val in v if val.family.name == "AF_INET"
            ]
            for k, v in addrs.items()
        }
        io = psutil.net_io_counters(pernic=True)
        data = [
            dict(
                name=k,
                bytes_sent=v.bytes_sent,
                bytes_recv=v.bytes_recv,
                packets_sent=v.packets_sent,
                packets_recv=v.packets_recv,
                **addrs_info
            )
            for k, v in io.items()
        ]

        return addrs_info

    # convert timestamps to characters
    def td(self, tm):
        dt = datetime.datetime.fromtimestamp(tm)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def dt(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def lastest_start_time(self):
        return self.td(psutil.boot_time())

    def logined_users(self):
        users = psutil.users()
        data = [
            dict(
                name=v.name,
                terminal=v.terminal,
                host=v.host,
                started=self.td(v.started),
                pid=v.pid
            )
            for v in users
        ]
        return data



if __name__ =="__main__":
    m = SysInfoMonitor()
    pprint(m.netinfo())