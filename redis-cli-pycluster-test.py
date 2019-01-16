import os

HOST="redis-18468.c3091.us-east-1-1.ec2.cloud.rlrcp.com"
PORT=18468
PASS="mypass"


def test(command):

    result = True

    cmdStr = "python redis-cli-pycluster.py --host=%s --port=%s --passwd=%s '%s'" % (HOST, PORT, PASS, command)
    rcode = os.system(cmdStr)

    if rcode != 0 : result = False

    return result


## Print the help
print "Printing the help ..."
os.system("python redis-cli-pycluster.py --help")

## Command with key and value
print "Setting a key ..."
test("SET hello world")

## Key-only command
print "Getting a key ..."
test("GET hello")

## Command without arguments
print "Fetching size ..."
test("DBSIZE")

## Commands without key but an extra argument
print "Scanning the database ..."
test("SCAN 0")

#print "Flushing the database async. ..."
#test("'FLUSHDB ASYNC'")




