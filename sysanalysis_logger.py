import logger

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format-=FORMAT, level=logging.WARNING)
logger = logging.getLogger(__name__)