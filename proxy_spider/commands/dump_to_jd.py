# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from scrapy.commands import ScrapyCommand
from proxy_spider.proxy.proxy import DumpProxyItemsValidToProxyItemsJd


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return "valid proxy_items_valid to proxy_items_jd"

    def run(self, args, opts):
        try:
            dump_to_jd = DumpProxyItemsValidToProxyItemsJd()
            dump_to_jd.start_threadpool()
        except Exception, e:
            print e.message