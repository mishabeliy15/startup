from django import template
register = template.Library()


@register.filter(name='dur_to_str')
def duration_to_str(value):
    res = ''
    minutes = value // 60
    if minutes >= 60:
        res += str(minutes // 60) + " h "
        minutes %= 60
    res += str(minutes) + ' min'
    return res