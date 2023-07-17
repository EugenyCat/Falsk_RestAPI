import json
from datetime import date

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return str(o)

        return super().encode(self.default(o))