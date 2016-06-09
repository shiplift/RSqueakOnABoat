import re

API_PORT = 8082
QUEUE_PORT = 8083
CONTROL_PORT = 8084
BENCHMARK_MACHINES = [
    "http://fb12ce8ws06:%s" % QUEUE_PORT,
    "http://timfelgentreff.no-ip.org:%s" % QUEUE_PORT
]
JOB_TABLE = "jobs"
COMMITID = "commitid"
BRANCH = "branch"
VM = "vm"
FLAG = "done"
DBFILE = "benchmarks.db"
CODESPEED_URL = 'http://speed.squeak.org/'
BINARY_URL = "https://www.hpi.uni-potsdam.de/hirschfeld/artefacts/rsqueak/commits/{}"
BINARY_BASENAME = "rsqueak-x86-linux-jit-{}"

ITERATIONS = 100

OUTPUT_RE = re.compile(r"([a-zA-Z0-9]+) total: iterations=%s runtime: ([0-9\.]+)ms \+/\-([0-9\.]+)" % ITERATIONS)

BENCHMARKS = []

from benchmarks import BENCHMARKS
from config import *