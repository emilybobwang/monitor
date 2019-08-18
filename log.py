# -*- coding: utf-8 -*-
import time
import datetime
from app.models.models import Cpu, Mem, Swap
from app.tools.SysInfoMonitor import SysInfoMonitor
from app.tools.orm import ORM


# date time
def dt():
    now = datetime.datetime.now()
    _date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    _date = now.strftime("%Y-%m-%d")
    _time = now.strftime("%H:%M:%S")
    return _date, _time, _date_time


# save log
def save_log():
    m = SysInfoMonitor()
    cpu_info, mem_info, swap_info = m.cpuinfo(), m.meminfo(), m.swapinfo()
    _date, _time, _date_time = dt()
    # 1.create session
    session = ORM.db()
    try:
        # CPU
        cpu = Cpu(
            percent=cpu_info["percent_avg"],
            create_date=_date,
            create_time=_time,
            create_dt=_date_time
        )
        # memory
        mem = Mem(
            percent=mem_info['percent'],
            total=mem_info['total'],
            used=mem_info['used'],
            free=mem_info['free'],
            create_date=_date,
            create_time=_time,
            create_dt=_date_time
        )
        # swap
        swap = Swap(
            percent=swap_info['percent'],
            total=swap_info['total'],
            used=swap_info['used'],
            free=swap_info['free'],
            create_date=_date,
            create_time=_time,
            create_dt=_date_time
        )
        # commit to db
        session.add(cpu)
        session.add(mem)
        session.add(swap)
    except Exception as e:
        #rollback
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()


if __name__ == "__main__":
    while True:
        _date, _time, _date_time = dt()
        print("start time：{}".format(_date_time))
        save_log()
        print("end time：{}".format(_date_time))
        #collect log every 5s
        time.sleep(5)
