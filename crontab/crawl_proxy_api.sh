#!/usr/bin/env bash
cd /home/apps/proxy_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_dump_to_jd.log"
echo $path_to_log
scrapy mc_crawl_proxy_api -s LOG_FILE=$path_to_log &
