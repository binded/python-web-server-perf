# python-web-server-perf

[![Build Status](https://travis-ci.org/binded/python-web-server-perf.svg?branch=master)](https://travis-ci.org/binded/python-web-server-perf)

Benchmark for threaded, single-process Python web servers.

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
