from pxr import Usd, UsdGeom, Tf

class WrongFileFormatError(Exception):
    pass
# MAKE A NEW STAGE AND PRIMS
# stage = Usd.Stage.CreateNew('HelloWorld.usda')
# xformPrim = UsdGeom.Xform.Define(stage, '/hello')
# spherePrim = UsdGeom.Sphere.Define(stage, '/hello/world')
# stage.GetRootLayer().Save()


# stage = Usd.Stage.Open('HelloWorld.usda')
# xform = stage.GetPrimAtPath('/hello')
# sphere = stage.GetPrimAtPath('/hello/world')

# sphere_extentAttr = sphere.GetAttribute('extent')

# sphere_radius = sphere.GetAttribute('radius')
# sphere_radius.Set(2)
# sphere_extentAttr.Set(sphere_extentAttr.Get() * 2)

# stage.GetRootLayer().Save()

# print(xform.GetPropertyNames())
# print(sphere.GetPropertyNames())
# print(sphere_extentAttr.Get())
# print(stage.GetRootLayer().ExportToString())


def open_file(file : str):
    try:
        stage = Usd.Stage.Open(file)
    except Tf.ErrorException as e:
        print(f"Error: {e}")
        raise WrongFileFormatError

    return stage
