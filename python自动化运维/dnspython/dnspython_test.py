# -*- coding:utf-8 -*-

import dns.resolver

domain = input('dns:')

a = dns.resolver.query(domain, 'A')
for i in a.response.answer:
    for j in i.items:
        print(j.address)