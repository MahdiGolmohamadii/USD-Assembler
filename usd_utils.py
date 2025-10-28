from pxr import Usd, UsdGeom, Tf, Sdf

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

def create_new_file(name):
    stage = Usd.Stage.CreateNew(name)
    return stage
    

def copy_prim(current_stage, prim_path, target_stage):
    curr_layer = current_stage.GetRootLayer()
    target_layer = target_stage.GetRootLayer()

    src_path = Sdf.Path(prim_path)
    dst_path = Sdf.Path("/World" + prim_path)

    if Sdf.CopySpec(srcLayer=curr_layer,
                srcPath=src_path,
                dstLayer=target_layer,
                dstPath=dst_path):
        print(f"Successfully copied prim {prim_path} to {target_layer}.")
    else:
        print("Something went wrong!")
        return
    
    target_stage.GetRootLayer().save()


def refrence_to_destination(curr_stage, prim_path, dst_stage, dst_parent='/copied'):
    
    src_path = curr_stage.GetRootLayer().realPath

    if not dst_stage.GetPrimAtPath(dst_parent):
        dst_stage.DefinePrim(dst_parent, "Xform")

    prim_name = prim_path.split('/')[-1]
    dst_path = f"{dst_parent}/{prim_name}"

    new_prim = dst_stage.DefinePrim(dst_path, "Xform")

    new_prim.GetReferences().AddReference(src_path, prim_path)
    dst_stage.GetRootLayer().Save()