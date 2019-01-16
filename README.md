# Very basic cluster capable command line tool for Redis (OSS Cluster)

This command line tool is not interactive, but it allows to pass a command as an argument.


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


### SET hello world

* i.e. `python redis-cli-pycluster.py --host=myhost --port=12345  'SET hello world'`

Output:

```
True
```

### GET hello

Output:

```
world
```

### DBSIZE

Output:

```
{'3.81.97.87:18468': 1L, '3.81.32.34:18468': 0L}
```

### SCAN 0

Output:

```
{'3.81.97.87:18468': (0L, [u'hello']), '3.81.32.34:18468': (0L, [])}
```
