## SuperDoctor

### What is this?
SuperDoctor is an app aimed to collect all of the information of sub-processes spawned form supervisor.

### Why choose SuperDoctor?
SuperDoctor provides an incredible convenient integration with supervisor.
All you need to do is install SuperDoctor and register a event listener in supervisorctl.

### How to use it?
```
pip install superdoctor
```
To add an event listener in supervisord.conf.
```script=shell
[eventlistener:SuperDoctor]
command=superdoctor
events=PROCESS_STATE,TICK_60
stdout_logfile=/your-log-path/supervisord.log
stderr_logfile=/your-log-path/supervisord-err.log
```
### Contributor
* Yu-Hsuan Lin

### Liscense
MIT