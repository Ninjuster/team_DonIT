import logging
from logging.handlers import RotatingFileHandler
from settings import bot, TG_OWNER_ID


CONSOLE_FMT = '{asctime} [{levelname:^8}] ({filename}:{funcName}:{lineno}): {message}'
FILE_FMT = '{asctime} [{levelname:^8}] ({filename}:{funcName}:{lineno}): {message}'

CONSOLE_FORMATS = {
    logging.INFO: f"\33[37m{CONSOLE_FMT}\33[0m",
    logging.WARNING: f"\33[33m{CONSOLE_FMT}\33[0m",
    logging.ERROR: f"\33[31m{CONSOLE_FMT}\33[0m",
    logging.CRITICAL: f"\33[1m\33[31m{CONSOLE_FMT}\33[0m"
}


class CustomFormatter(logging.Formatter):
    def __init__(self, formats):
        super().__init__()
        self.formats = formats

    def format(self, record):
        log_fmt = self.formats.get(record.levelno, CONSOLE_FMT)
        formatter = logging.Formatter(log_fmt, style="{")
        return formatter.format(record)


stream_handler = logging.StreamHandler()
stream_handler.setFormatter(CustomFormatter(CONSOLE_FORMATS))

file_handler = RotatingFileHandler(filename='log/logs.log', encoding='UTF-8', maxBytes=100000, backupCount=5)
file_formatter = logging.Formatter(FILE_FMT, style="{")
file_handler.setFormatter(file_formatter)

error_handler = RotatingFileHandler(filename='log/critical_error.log', encoding='UTF-8', maxBytes=100000, backupCount=5)
error_handler.setFormatter(file_formatter)
error_handler.setLevel(logging.ERROR)

logging.basicConfig(
    level=logging.INFO,
    handlers=[stream_handler, file_handler, error_handler]
)

log = logging.getLogger(__name__)


async def logging_tg(message):
    try:
        chat_id = TG_OWNER_ID
        await bot.send_message(chat_id, text=message)
    except:
        log.error(' ', exc_info=True)
