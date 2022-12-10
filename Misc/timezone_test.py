from pytz import common_timezones, all_timezones, timezone
from datetime import datetime

if __name__ == '__main__':
    tz = datetime.now()
    print(timezone("UTC").localize(tz))



