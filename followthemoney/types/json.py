import json  # yay Python 3
from banal import ensure_list

from followthemoney.types.common import PropertyType


class JsonType(PropertyType):
    name = 'raw'
    group = None
    matchable = False

    def pack(self, obj):
        """Encode a given value to JSON."""
        # TODO: use a JSON encoder that handles more types?
        if obj is not None:
            return json.dumps(obj)

    def unpack(self, obj):
        """Decode a given JSON object."""
        if obj is None:
            return
        try:
            return json.loads(obj)
        except Exception:
            return obj

    def clean(self, obj, **kwargs):
        if not isinstance(obj, str):
            obj = self.pack(obj)
        return obj

    def normalize(self, obj, cleaned=False, **kwargs):
        return [] if obj is None else [obj]

    def join(self, values):
        """Turn multiple values into a JSON array."""
        values = [self.unpack(v) for v in ensure_list(values)]
        return self.pack(values)
