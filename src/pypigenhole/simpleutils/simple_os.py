import subprocess
import sys
import time
import threading


# timeout is None: no timeout
def run_exe(exe: str, timeout=None, check_timeout_interval=1):
    try:
        # need to reroute stderr in proc to stdout, otherwise won't get msg
        # do not set shell=True, since we can't kill it for timeout
        proc = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                universal_newlines=True)

        if timeout:
            thread = threading.Thread(target=proc_monitor, args=(proc, timeout, check_timeout_interval))
            thread.start()
            thread.join(timeout)

        (stdout, stderr) = proc.communicate()
        reply = ''
        if stdout:
            reply += stdout
        if stderr:
            reply += stderr
        # this code truncates the output, don't know why.
        # reply = ''
        # while proc.poll() is None:
        #     if proc.returncode is not None:  # terminated by monitor
        #         return proc.returncode
        #
        #     line = proc.stdout.readline()
        #     if line:
        #         if stream_out:
        #             stream_out.write(line)  # stream_out needs to have these 2 methods
        #             stream_out.flush()
        #
        #         reply += line
        #
        # proc.stdout.close()
        return proc.returncode, reply
    except FileNotFoundError:
        return -1, sys.exc_info()[1]


def proc_monitor(proc, timeout, check_timeout_interval):
    now = time.time()
    while time.time() - now < timeout:
        time.sleep(check_timeout_interval)

    if proc.returncode is None:
        proc.terminate()


# class LogWriter:  # convert logger to writer
#     def __init__(self, ext_logger, level):
#         self._logger = ext_logger
#         self._level = level
#
#     def write(self, message):
#         for line in message.splitlines():
#             self._logger.log(self._level, line.rstrip())
#
#     def flush(self):
#         for h in self._logger.handlers:
#             h.flush()


def run_proc(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    reply = stdout.decode('utf-8') + stderr.decode('utf-8')
    return proc.returncode, reply
