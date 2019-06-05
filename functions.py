import bpy
import fnmatch
import re

def is_from(object, regex=''):

    if regex == '':
        regex = bpy.context.scene.attr_regex

    return re.search(regex, object.name)


def change_max_drawtype(draw_type='SOLID', others=False, regex=''):
    for object in [o for o in bpy.data.objects if o.type=='MESH']:
        if others:
            if not is_from(object, regex=regex):
                object.draw_type = draw_type
        else:
            if is_from(object, regex=regex):
                object.draw_type = draw_type


def showhide(hide=True, others=False, regex=''):
    for object in [o for o in bpy.data.objects if o.type=='MESH']:
        if others:
            if not is_from(object, regex=regex):
                object.hide = hide
        else:
            if is_from(object, regex=regex):
                object.hide = hide


if __name__ == '__main__':
    showhide(hide=True, others=True, regex=['props|chars'])
