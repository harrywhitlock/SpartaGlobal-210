


from google.cloud import storage
import os

'''Apply json key'''
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "upheld-producer-379316-c90f4b755ac9.json"

'''Instantiate a client'''
client = storage.Client()

'''Retrieve a bucket reference'''
bucket = client.get_bucket('my_first_bucket_harry')

'''Upload a file to the bucket'''
blob = bucket.blob('text.txt')
# blob.upload_from_filename('/Users/harrywhitlock/Desktop/Screenshot 2023-03-01 at 14.59.26.png')
blob.upload_from_filename('sometext.txt')

'''Download a file'''
# blob = bucket.get_blob('picture1')
# blob.download_to_filename('picture2')

'''Read a file'''
blob = bucket.get_blob('text')
file_contents = blob.download_as_text()
print(file_contents)