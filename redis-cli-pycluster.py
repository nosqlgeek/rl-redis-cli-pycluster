###############################################################
#
# redis-cli-pycluster
#
# Author: david.maier@redislabs.com
#
###############################################################


##-- Imports
import click
from rediscluster import StrictRedisCluster


##-- Helpers

################################
#
# Connect to the cluster
#
################################
def connect(host, port, passwd):

    startup_nodes = [{"host": host, "port": str(port)}]

    if passwd:
        return StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True, password=passwd)
    else:
        return StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

################################
#
# Do some basic command parsing
#
################################
def parsecmd(command):

    cmdArr = command.split(" ")

    cmd = ""
    key = ""
    args = []

    for i in range(0, len(cmdArr)):

        e = cmdArr[i]

        if i == 0:
            cmd = e.strip()
        elif i == 1:
            key = e.strip()
        else:
            args.append(e.strip());

    return {"cmd": cmd, "key" : key, "args": args}


################################
#
# Execute the command
#
################################
def exec_command(rc, command):

    cstruct = parsecmd(command)
    cmd = cstruct["cmd"];
    key = cstruct["key"];
    args = cstruct["args"];

    if (not key):
        return rc.execute_command(cmd)
    else:
        if len(args) == 0:
            return rc.execute_command(cmd, key)
        else:
            return rc.execute_command(cmd, key, *args)



##-- Main
@click.command()
@click.option("--host", default="127.0.0.1", prompt="Host/Ip", help="Database host name or IP address")
@click.option("--port", default=6379, prompt="Port", help="Database port")
@click.option("--passwd", default="", help="Database password")
@click.argument("command")

def main(host, port, passwd, command):

    rc = connect(host, port, passwd)
    result = exec_command(rc, command);
    print result;



if __name__ == "__main__":
    main()
