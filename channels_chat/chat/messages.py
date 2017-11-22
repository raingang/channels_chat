import json


class Message(dict):

    def __init__(self, text=None, username=None, **kwargs):
        defaults = {'type': 'message'}
        if text:
            defaults['text'] = text
        if username:
            defaults['username'] = username
        defaults.update(kwargs)
        self['text'] = json.dumps(defaults)


class SystemMessage(Message):

    def __init__(self, *args, **kwargs):
        kwargs['type'] = 'system'
        kwargs['username'] = 'System'
        super().__init__(*args, **kwargs)



def message(*args, **kwargs):
    return Message(*args, **kwargs)


def system(*args, **kwargs):
    return SystemMessage(*args, **kwargs)


