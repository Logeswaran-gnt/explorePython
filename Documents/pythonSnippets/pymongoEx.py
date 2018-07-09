'''from pymongo import Connection
# connection = Connection()
connection = Connection('localhost', 27017)
db = connection.student
collection = db.student
print dir(collection)
db.student.insert_many({'name':'Kaviarasan'},{'name':'anumon'})
for user in collection.find():
    print user'''

from pymongo import MongoClient
connect = MongoClient('localhost',27017)
db = connect.student
coll = db.student
coll.insert_many([{'name':'anumon'},{'name':'sudheer'}])
# coll.update_many({$set})
print dir(coll)
cursor = coll.find()#.limit(2)
for i in cursor:
    print i
print coll.count()
'''
'aggregate', 'aggregate_raw_batches', 'bulk_write', 'codec_options', 
'count', 'count_documents', 'create_index', 'create_indexes', 'database', 
'delete_many', 'delete_one', 'distinct', 'drop', 'drop_index', 'drop_indexes', 
'ensure_index', 'estimated_document_count', 'find', 'find_and_modify', 'find_one', 
'find_one_and_delete', 'find_one_and_replace', 'find_one_and_update', 'find_raw_batches', 
'full_name', 'group', 'index_information', 'initialize_ordered_bulk_op', 'initialize_unordered_bulk_op',
 'inline_map_reduce', 'insert', 'insert_many', 'insert_one', 'list_indexes', 'map_reduce', 
 'name', 'next', 'options', 'parallel_scan', 'read_concern', 'read_preference', 'reindex', 
 'remove', 'rename', 'replace_one', 'save', 'update', 'update_many', 'update_one', 'watch', 
 'with_options', 'write_concern'

'''
'''
DeviceManagement:
(non)persistent caching
python oops
django -> Django REST framework
mixing
views
mongodb
api gateway -> redirecting api to the associated container

Watchdog:
thread join,multithread/processing
rabitmq+celery
threadpool vs processpool
Docker,container

Celery-> Rule engine(notification-event package)- distributed manner
python reflexion(same in java/c++)
notification engine how can create?
hash map
'''