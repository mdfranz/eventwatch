import json
from alertdb import AlertDB
from cleanup import *
from events import *

def lambda_handler(event, context):
    debug=True
    # This configures what are the tuples we track
    tuples = ( 
                 ("username","accesskey"), ("username","ip"), ("username","name"), ("username","region"), 
                 ("accesskey","agent"),("accesskey","ip"),
                 ("arn","ip"), ("arn","agent"), ("arn","region"),
                 ("region","name"), ("region","arn"), ("region","username")
             )
              
    alert_db = AlertDB("mdfranz-cloudtrail-hash")
    event_str = json.dumps(event)
    fields = parse_events(event)
    if debug:
        print event_str

    tmp = open('/tmp/myevent.json',"w")
    tmp.write(event_str)
    tmp.close()

    # Extract Region

    for t in tuples:
        o = create_object_name(fields,t)
        print "Checking:", o

        if not alert_db.get(o):
            print "NEW:",t,o 
            alert_db.put(o,open('/tmp/myevent.json'))

    return fields





