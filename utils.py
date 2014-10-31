import re
import logging
import ConfigParser


logging.basicConfig()
LOGGER = logging.getLogger(__name__)

class Utilities():

    @staticmethod
    def reg_finder(regexp, regstring):
        val = re.findall(regexp, regstring)
        return val[0]


def parse_config(config_file):

    cfg = ConfigParser.SafeConfigParser()
    cfg.optionxform = str  # retains case in keys
    cfg.read(config_file)

    return cfg

if __name__ == "__self__":
    Utilities()