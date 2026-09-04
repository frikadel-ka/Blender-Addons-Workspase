#type: ignore
#GPL лицензия:
# Copyright (C) 2026 Frikadel_ka

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


'''
Аддон для 

Функционал:
'''


bl_info = {
    "name": "",
    "author": "Frikadel_ka",
    "description": "",
    "blender": (4, 3, 0),
    "version": (0, 0, 1),
    "location": "View3D > Sidebar > Mass Drop",
    "warning": "",
    "doc_url": "https://github.com/frikadel-ka/addon#readme",
    "tracker_url": "https://github.com/frikadel-ka/addon/issues",
    "category": "Object",
}


from bpy.props import StringProperty, FloatProperty, CollectionProperty, IntProperty, PointerProperty, EnumProperty, BoolProperty # type: ignore
from bpy.types import Operator, Panel, PropertyGroup

if "bpy" in locals():
    import importlib
    # Вписываем сюда все ваши файлы, кроме init.py
    #translations=importlib.reload(translations)
    print("--- Аддон обновлен ---")
else:
    #from .mass_drop import translations


import bpy
import bmesh
import math
#translations_dict = translations.translations_dict

# UTILS
def busness_logic():
    return 0

# PROPERTIES
class AddonSettingsPronerties(PropertyGroup):
    first_setting: FloatProperty(
        name="First Setting",
        description="Description the First Setting",
        default=1,
        min=0,
        soft_max=2
    )
    # и тд

# OPERATORS
class MYADDON_OT_operator(Operator):
    bl_idname = "my_addon.operator" # Уникальный id "категория.название"
    bl_label = "Operator" # Имя в интерфейсе
    bl_options = {'REGISTER', 'UNDO'} # Поддержка Ctrl+Z

    def execute(self, context):
        #Получаем доступ к нашим настройкам
        cfg = context.scene.my_addon_settings

        busness_logic()

        self.report.({'INFO'}, f"Info-Panel") # Инфопанель

        return {'FINISHED'}

# UI
class VIEW3D_PT_main_panel(Panel):
    bl_idname = "VIEW3D_PT_main_panel"
    bl_label = "My Addon"
    bl_space_type = 'VIEW3D'
    bl_region_type = 'UI'
    bl_category = 'My Tool' # Название вкладки в N-панели
    def draw(self, context):
        # чек в доках и др файлах ui.py...

# REGISTRATION
classes = (
    AddonSettingsPronerties,
    MYADDON_OT_operator,
    VIEW3D_PT_main_panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.my_wheel_settings = PointerProperty(
            type=properties.WheelSettingsProperties,
            name="Wheel Settings"
        )
    
    #bpy.app.translations.register(__name__, translations_dict)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.my_wheel_settings

    #bpy.app.translations.unregister(__name__)

if __name__ == "__main__":
    register()