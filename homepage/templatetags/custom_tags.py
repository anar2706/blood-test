from django import template
import json

register = template.Library()

json_decode_string = ""
json_decode_dict = {}

@register.filter(name='contains')
def contains(string, val):
    return val in string

@register.filter(name='seq_counter')
def seq_counter(seq):
    return len(seq)

@register.filter(name='count_persistent_messages')
def count_persistent_messages(messages):
    # print(dir(messages))
    return len(tuple(filter(lambda x: "persistent" in x.tags, messages)))

@register.filter(name='json_decode')
def json_decode(string, keyword):
    global json_decode_string, json_decode_dict

    if json_decode_string == string:
        return json_decode_dict.get(keyword)

    try:
        js = json.loads(str(string))
        json_decode_dict = js
        json_decode_string = string
        return js.get(keyword)
    except:
        return string
