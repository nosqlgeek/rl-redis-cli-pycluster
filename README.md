#  Redis OSS-Cluster Command line Tool

This is a very basic cluster capable command line tool for Redis (OSS Cluster).

## Motivation

Redis is coming with a very sophisticated command line tool, called `redis-cli`. Especially older versions of this tool are using a light-weighted approach for interacting with an OSS Redis Cluster.

1. Establish the connection to one of the endpoints (shards)
2. Execute the command to the shard to which the tool is currently connected
3. If the shard is not responsible for the key which was passed over as an argument, then the client is retrieving a redirect (MOVED) response
4. Follow the redirect response by replacing the current connection with a new one to this shard
5. Execute the command again

There is a challange when a command is executed which doesn't get a key passed. In this case `redis-cli` will just execute the command to the current connection which then causes partial results (i.e. only the size of the shard to which the tool was connected). The tool `redis-cli-pycluster` is using the `redispy-cluster` smart client library which means that it behaves differently:

1. Establish the connection to one of the endpoints
2. Fetch the cluster topology by executing `CLUSTER SLOTS`
3. Establish a connection to each endpoint in the cluster
4. A command which is getting a key passed will be executed against the right endpoint from the very beginning
5. Commands without key arguments will be executed in parallel against every endpoint. The result is grouped by endpoint.


## Limitations

* This command line tool is not (yet) interactive, but it allows to pass a command as an argument
* The tool doesn't return the result in the same format as `redis-cli` does. The response is already parsed and converted into an equivalent Python type/object (i.e. lists, dictonary, boolean, ...). The output is the string representation of this value.


## Usage

```
Usage: redis-cli-pycluster.py [OPTIONS] COMMAND

Options:
  --host TEXT     Database host name or IP address
  --port INTEGER  Database port
  --passwd TEXT   Database password
  --help          Show this message and exit.
```

If the COMMAND argument contains spaces (i.e. SET hello world) then it's required to wrap the command with single quotes.

## Examples


### KV Command

Command:

```
python redis-cli-pycluster.py --host=myhost --port=12345  'SET hello world'
```

Output:

```
True
```

### Key-only Command

Command:

```
python redis-cli-pycluster.py --host=myhost --port=12345 --passwd mypass  'GET hello'
```

Output:

```
world
```

### Key-less Command

Command:

```
python redis-cli-pycluster.py --host=myhost --port=12345 'DBSIZE'
```

Output:

```
{'3.81.97.87:18468': 1L, '3.81.32.34:18468': 0L}
```

### Key-less Command with Argument

Command:

```
python redis-cli-pycluster.py --host=myhost --port=12345 'SCAN 0'
```

Output:

```
{'3.81.97.87:18468': (0L, [u'hello']), '3.81.32.34:18468': (0L, [])}
```

## How to build?

The build box should have Python 2.7 and `pip` installed

The build script is working the following way:

1. Create Python 2.7 VirtualEnv
2. Install all dependencies to this environment
3. Use `PyInstaller` in order to package a standalone version (doesn't need Python installed on the target machnine)
4. Wraps the dist package as a TAR file 

The result is the file `redis-cli-pycluster.tar`.

> PyInstaller is not a cross-platform compiler, which means that you will need to execute the build script at least once on your target platform.
