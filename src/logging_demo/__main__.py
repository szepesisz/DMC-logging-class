import logging

from logging_demo.subdir.module import hi_from_module

logger = logging.getLogger(__name__)

logging

root_logger = logging.getLogger()

handler = logging.StreamHandler()
formatter = logging.Formatter(
    fmt='%(asctime)s [%(levelname)s] %(name)s.%(funcName)s[%(lineno)s]: %(message)s'
)

handler.setFormatter(formatter)
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)

def calc_sum_of_list(l):
    s = 0
    for n in l:
        s += n
        logger.debug(f'Adding {n}, actual sum: {s}')
    return s


def main():
    logger.info('Hi')
    l = [123, 345, 42, 11]
    s = calc_sum_of_list(l)
    logger.info(f'Sum of {l}: {s}')
    logger.error('Something is bad')
    hi_from_module()


if __name__ == '__main__':
    main()
