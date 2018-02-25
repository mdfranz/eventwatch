import string

def sanitize(s):
    """Remove special characters that muck with S3 paths"""
    tbl=string.maketrans(":/","-_") # remove : and / from agent and arn
    return str(s).translate(tbl)
    
def create_object_name(f,t):
    if f.has_key(t[1]) and f.has_key(t[0]):
        return sanitize(f[t[0]]) + "/" + sanitize(f[t[1]])
    else:
        return "none"