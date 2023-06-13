args = {"headers":"application/json", "redirects": False, "stream":100}
allow_redirects = args.pop("allow_redirects", True)
print(args)
print(allow_redirects)
print(args.get("stream"))

from collections import OrderedDict

adaptor = OrderedDict()
print(adaptor)
for (key,value) in adaptor.items():
    print(key)
    print(value)