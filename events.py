def parse_events(event):
    fields = {}
    if event.has_key('region'):
        fields['region'] = event['region']
    if event.has_key('detail'):
        detail = event['detail']
        
        if detail.has_key('userIdentity'):
            if detail['userIdentity'].has_key('userName'):
                fields['username'] = detail['userIdentity']['userName']
            fields['accesskey'] = detail['userIdentity']['accessKeyId']
            fields['arn'] = detail['userIdentity']['arn']

        if detail.has_key('sourceIPAddress'):
            fields['ip'] = detail['sourceIPAddress']
        if detail.has_key('eventSource'):
            fields['source'] = detail['eventSource']
        if detail.has_key('userAgent'):
            fields['agent'] = detail['userAgent']
        if detail.has_key('eventType'):
            fields['type'] = detail['eventType']
        if detail.has_key('eventName'):
            fields['name'] = detail['eventName']
    return fields