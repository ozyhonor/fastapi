from bson import ObjectId
from mongoengine import Document, EmbeddedDocument

def to_json(obj):
    if isinstance(obj, list):
        return [to_json(i) for i in obj]
    if isinstance(obj, dict):
        return {k: to_json(v) for k, v in obj.items()}
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, (Document, EmbeddedDocument)):
        obj_dict = obj.to_mongo().to_dict()
        if '_id' in obj_dict:
            obj_dict['id'] = str(obj_dict.pop('_id'))
        return {k: to_json(v) for k, v in obj_dict.items()}
    return obj
