# 1st sample output
python3.10 app.py --period=1h --tz=Europe/Athens --t1=20210714T204603Z --t2=20210715T123456Z; echo $?

# 2nd sample output
# python3.10 app.py --period=1d --tz=Europe/Athens --t1=20211010T204603Z --t2=20211115T123456Z; echo $?

# 3rd sample output
# python3.10 app.py --period=1mo --tz=Europe/Athens --t1=20210214T204603Z --t2=20211115T123456Z; echo $?

# 4th sample output
# python3.10 app.py --period=1y --tz=Europe/Athens --t1=20180214T204603Z --t2=20211115T123456Z; echo $?


# Example of wrong arguments.
# python3.10 app.py --period=1h --tz=Europess/Athens --t1=20210714T204603Z --t2=20210715T123456Z; echo $?