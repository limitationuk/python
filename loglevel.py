from os import environ

if(environ.get("LOGLEVEL")):
    print("로깅중")
else:
    print("로깅 안하는중")