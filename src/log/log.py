import datetime
import json

## Log events into a file

##ToDo:
## actually the file should be placed into a volume
## and there should be a function to construct a more detailed log string
## but we will do a simple text string with date & message

def log(log_message):
    log_time = datetime.datetime.today()
    log_string = f'{log_time} {log_message} \n'
    with open('src/params/config.json') as f:
        config = json.load(f)
    log_file = config["log"]["log_file"] #'src/log/events.log'
    with open(log_file, 'a') as f:
        f.write(log_string)


