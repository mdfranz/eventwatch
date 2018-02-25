import boto3

class AlertDB:
    def __init__(self,name,region="us-east-1"):
        # Validate bucket exists in the proper region
        self.s3c = boto3.client('s3')
        self.s3r = boto3.resource('s3')
        self.bucket = self.s3r.Bucket(name)

    def get(self,path):
        """Checks if a given key is present"""
        o = self.s3r.Object(self.bucket.name,path)
        try:
            o.load()
        except Exception as e:
            return False
        return True

    def put(self,path,f):
        o = self.s3r.Object(self.bucket.name,path)
        o.upload_fileobj(f)