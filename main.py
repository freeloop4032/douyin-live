import logging

import dy

if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    url = 'https://live.douyin.com/442096814877'
    dy.parseLiveRoomUrl(url)
