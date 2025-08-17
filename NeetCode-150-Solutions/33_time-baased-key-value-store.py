"""
Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:

TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key with the
value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key if
    set was previously called on it and the most recent timestamp for that key
    prev_timestamp is less than or equal to the given timestamp (prev_timestamp
    <= timestamp). If there are no values, it returns "".
    
Note: For all calls to set, the timestamps are in strictly increasing order.
"""


class TimeMap:
    """
    The idea is implementing a hashmap where the values are arrays
    made up by tuples formed by (value, timestamp) ordered by timestamp.
    This is done such that the set() function can operate in O(1) as
    a new item will have a timestamp surely higher than any previous
    set() call.
    At the same time, the get() function can be implemented such that
    to obtain log(m) time complex. using a simple binary search over 
    the elements in the coresponding value array.
    """

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        values = []
        res = ""

        if key in self.time_map:
            values = self.time_map[key]
        else:
            return ""

        # binary search
        l, r = 0, len(values) - 1

        while l <= r:
            m = l + (r - l) // 2
            val, t = values[m]

            if t <= timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1

        return res
