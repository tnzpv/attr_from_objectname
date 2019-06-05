bl_info = {
    "name":        "Attribute from Objects Names",
    "description": "Change hide/max_drawtype from objects names",
    "author":      "TNZPV",
    "version":     (0, 1, 0),
    "blender":     (2, 79, 4),
    "location":    "3D View",
    "warning":     "",
    "category":    "3D View"
}

import bpy

from . import operators
from . import panels


def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.attr_regex = bpy.props.StringProperty(name='attr_regex', default='.*')

def unregister():
    del bpy.types.Scene.attr_regex
    bpy.utils.unregister_module(__name__)
