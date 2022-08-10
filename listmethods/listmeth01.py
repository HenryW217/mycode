#!/usr/bin/env python3

proto = [
        "ssh",
        'http',
        'https'
        ]
protoa = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
proto.append('dns')
protoa.append('dns')
print(proto)
proto2 = [ 22, 80, 443, 53 ]
proto.extend(proto2)
print(f"proto is {proto}")
protoa.append(proto2)
print(f'protoa is {protoa}')

