from __future__ import print_function

try:
    import statsd
except ImportError:
    print("Skipping the statsd tests.")
    statsd = None

if statsd is not None:
    pass

try:
    import redis
except ImportError:
    print("Skipping redis tests.")
    redis = None

if redis is not None:
    pass
