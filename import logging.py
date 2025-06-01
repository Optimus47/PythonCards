import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
logging.info("Программа запущена")
logging.warning("Предупреждение!")
logging.error("Произошла ошибка")

