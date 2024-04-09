def get_user_schema(request):
    user = request.user
    if user:
        return f'user_{user.id}_schema'
    else:
        return None

class UserSchemaRouter:
    def __init__(self, request=None):
        self.request = request
        
    # def db_for_read(self, model, **hints):
    #     if model._meta.app_label == 'user_car':
    #         user_schema = get_user_schema(self.request)  # Implement this function
    #         return user_schema
    #     return None

    # def db_for_write(self, model, **hints):
    #     return self.db_for_read(model, **hints)

    # def allow_relation(self, obj1, obj2, **hints):
    #     return obj1._state.db == obj2._state.db

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     if db == 'default':
    #         return True
    #     return False


