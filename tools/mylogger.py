from logging import Logger,FileHandler,StreamHandler,Formatter
import logging
import time,os
from logging.handlers import RotatingFileHandler

__logs_dir = os.path.join(os.path.dirname(__file__),'../logs')
if not os.path.exists(__logs_dir):
    os.mkdir(__logs_dir)

__log_file_name = time.strftime('%Y_%m_%d')+'.log'
__log_file = os.path.join(__logs_dir,__log_file_name)

# 实例化类
log = Logger(name='fanmao')
# log.setLevel(logging.DEBUG)

# 定义日志格式
ft = Formatter('%(asctime)s-[%(name)s]-[%(levelname)s] %(message)s')


# 1-1. 定义输出流管理器
st = StreamHandler()
st.setLevel(logging.DEBUG)
st.setFormatter(ft)
# 1-2. 输出流管理器加载到log日志
log.addHandler(st)

# 2-1 定义文件流管理器
sf = FileHandler(filename=__log_file,encoding='utf8')
sf.setLevel(logging.DEBUG)
sf.setFormatter(ft)

# 2-2 文件记录管理器添加到log中
log.addHandler(sf)

# 3-1 添加文件大小配置
rtf = RotatingFileHandler(filename='log.txt',maxBytes=10*1024,backupCount=10)
rtf.setLevel(logging.DEBUG)
rtf.setFormatter(ft)
log.addHandler(rtf)

