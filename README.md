# lt2json

Convert log file to text or json format.

## Installation

```bash
git clone https://github.com/mohammadnovel/lt2json
```

Then install

```bash
cd lt2json
python setup.py install
```

## Usage

### Convert to text format

Convert log file to text (default)

```bash
lt2json /var/log/nginx/access.log -o $HOME/nginx-access.txt
```

Convert multiple log files to text with destination directory

```bash
lt2json /var/log/nginx/access.log /var/log/nginx/error.log -d $HOME/lt2json/
```

If destination directory is not provided, the scripts will use `current directory` + `lt2json_output`

### Convert to json format

Convert log file to json

```bash
lt2json /var/log/nginx/access.log -t json -o $HOME/nginx-access.json
```

Convert multiple log files to text with destination directory

```bash
lt2json /var/log/nginx/access.log /var/log/nginx/error.log -t json -d $HOME/lt2json/
```

Convert log file to json with regex (advanced)

```bash
lt2json /var/log/nginx/access.log -t json -o $HOME/nginx-access.json -e '^(?P<remote_addr>.*?) - (?P<remote_user>.*?) \[(?P<time_local>.*)?\] \"(?P<request>.*?)\" (?P<status>\d+) (?P<body_bytes_sent>\d+) \"(?P<http_referer>.*?)\" \"(?P<http_user_agent>.*?)\" \"(?P<http_x_forwarder_for>.*?)\"$'
```

### For further documentation you can run

```bash
lt2json -h
```