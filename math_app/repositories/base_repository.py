from django.db import models

class BaseRepository:
    model: models.Model = None

    @classmethod
    def get_all(cls):
        return cls.model.objects.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.model.objects.get(id=id)

    @classmethod
    def create(cls, **kwargs):
        instance = cls.model(**kwargs)
        instance.save()
        return instance

    @classmethod
    def update(cls, id, **kwargs):
        cls.model.objects.filter(id=id).update(**kwargs)

    @classmethod
    def delete(cls, id):
        cls.model.objects.filter(id=id).delete()