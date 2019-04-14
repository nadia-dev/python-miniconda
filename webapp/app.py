from flask import Flask
from flask import request
from pathlib import Path
from string import Template

app = Flask(__name__)
logs = 'logs.txt'

'''
Calls:
1. source -> read, activity, average (read), value (read)
2. source -> calculated, activity, average (updated), value (read), most_recent (value read before), fuel (calculated)
3. source -> granted, activity, fuel (granted)
'''

@app.route('/log')
def log():

    filename = Path(logs)
    filename.touch(exist_ok=True)  # will create file, if it exists will do nothing
    file = open(logs, 'a')

    source = request.args.get('source') # source: read, calculated, granted
    activity = request.args.get('activity')
    average = request.args.get('average')
    value = request.args.get('value')
    fuel = request.args.get('fuel')
    most_recent = request.args.get('mostRecentReading')
    date = request.args.get('date')

    template = Template("Source: $a, Activity: $b, Average: $c, Value: %d, Most Recent: %e, Fuel: %f, datetime: %g")
    info = template.safe_substitute(a=source, b=activity, c=average, d=value, e=most_recent, f=fuel, g=date)
    info += "\n"
    info += '-------------------\n'

    file.write(info)
    file.close()

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
