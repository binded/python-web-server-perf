# python-web-server-perf

[![Build Status](https://travis-ci.org/binded/python-web-server-perf.svg?branch=master)](https://travis-ci.org/binded/python-web-server-perf)

Benchmark for threaded, single-process Python web servers.

## Example results (Macbook Pro Mid 2015)

```
sanic
---
Running 15s test @ http://localhost:8080/health
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    23.09ms   10.19ms 132.47ms   82.14%
    Req/Sec     1.34k   269.10     2.27k    81.60%
  240216 requests in 15.03s, 27.72MB read
  Socket errors: connect 0, read 307, write 0, timeout 0
Requests/sec:  15980.75
Transfer/sec:      1.84MB
Running 15s test @ http://localhost:8080/upload
  12 threads and 36 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.09ms    1.57ms  36.08ms   84.55%
    Req/Sec   747.21     95.57     1.20k    77.50%
  134075 requests in 15.03s, 15.47MB read
Requests/sec:   8918.90
Transfer/sec:      1.03MB

japronto
---
Accepting connections on http://0.0.0.0:8080
Running 15s test @ http://localhost:8080/health
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.44ms    1.29ms  14.64ms   69.21%
    Req/Sec     6.92k   793.30    11.58k    84.66%
  1247606 requests in 15.10s, 96.37MB read
  Socket errors: connect 0, read 326, write 0, timeout 0
Requests/sec:  82606.67
Transfer/sec:      6.38MB
Running 15s test @ http://localhost:8080/upload
  12 threads and 36 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.72ms    1.04ms  34.10ms   95.51%
    Req/Sec     1.81k   281.93     5.35k    90.36%
  325415 requests in 15.10s, 25.14MB read
Requests/sec:  21545.76
Transfer/sec:      1.66MB
Termination request received

werkzeug
---
Running 15s test @ http://localhost:8080/health
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    82.66ms   13.77ms 119.98ms   92.66%
    Req/Sec   124.54     58.77   320.00     66.85%
  15795 requests in 15.10s, 2.33MB read
  Socket errors: connect 0, read 1082, write 5, timeout 0
Requests/sec:   1046.12
Transfer/sec:    158.35KB
Running 15s test @ http://localhost:8080/upload
  12 threads and 36 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    58.52ms   39.23ms 135.40ms   64.81%
    Req/Sec    32.79     15.18    75.00     64.58%
  162 requests in 15.09s, 24.52KB read
Requests/sec:     10.74
Transfer/sec:      1.63KB
```

## Usage

```bash
./bench
```

## Install

Install the [wrk](https://github.com/wg/wrk) benchmarking tool.

With pyenv:

```bash
pyenv virtualenv 3.6.2 python-web-server-perf
pyenv local python-web-server-perf
pip install -r requirements.txt
```
