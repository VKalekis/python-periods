### Python periodic event calculator

```app.py```: Calculates periodic events with a specific period between two timestamps (start_timestamp, end_timestamp) in UTC.

The shift in time is performed in local time.

Each periodic event corresponds to the start of the period (in local time).
For example, a periodic event with a period of 1month has matching timestamps in the form of YYYYMM01:000000.

Run app:
- by running the python ```app.py``` script.
 
    ``` 
    python3.10 app.py 
        --period=period 
        --tz=timezone 
        --t1=start_timestamp
        --t2=end_timestamp
    ```

- by running the ```run.sh``` bash script which contains the sample commands from the assignment pdf.

- by using the docker image found [here](https://hub.docker.com/repository/docker/vkalekis/python-periods/).


### Unit tests 
In ```unittests.py``` using the sample outputs from the assignment pdf and a wrong input senario.