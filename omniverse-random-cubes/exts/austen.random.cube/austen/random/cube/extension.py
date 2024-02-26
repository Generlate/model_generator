import omni.ext
import omni.ui as ui
import omni.kit.commands
import random


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[austen.random.cube] some_public_function was called with x: ", x)
    return x**x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class AustenRandomCubeExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self):
        print("[austen.random.cube] austen random cube startup")

        self._window = ui.Window("Make Random Cube", width=300, height=300)
        with self._window.frame:
            with ui.VStack():

                def generate_random_algorithm_cube():

                    omni.kit.commands.execute(
                        "CreateMeshPrimWithDefaultXform", prim_type="Cube"
                    )

                    omni.kit.commands.execute(
                        "TransformMultiPrimsSRTCpp",
                        count=1,
                        paths=["/World/Cube"],
                        new_translations=[0.0, 0.0, 0.0],
                        new_rotation_eulers=[0.0, 0.0, 0.0],
                        new_rotation_orders=[0, 1, 2],
                        new_scales=[
                            (random.uniform(0.05, 3)),
                            (random.uniform(0.05, 3)),
                            (random.uniform(0.05, 3)),
                        ],
                        old_translations=[0.0, 0.0, 0.0],
                        old_rotation_eulers=[0.0, 0.0, 0.0],
                        old_rotation_orders=[0, 1, 2],
                        old_scales=[1.0, 1.0, 1.0],
                        usd_context_name="",
                        time_code=0.0,
                    )

                def delete():
                    omni.kit.commands.execute(
                        "DeletePrims",
                        paths=[
                            "/World/Cube",
                            "/World/Cube_01",
                            "/World/Cube_02",
                            "/World/Cube_03",
                            "/World/Cube_04",
                            "/World/Cube_05",
                            "/World/Cube_06",
                            "/World/Cube_07",
                            "/World/Cube_08",
                            "/World/Cube_09",
                            "/World/Cube_10",
                        ],
                        destructive=False,
                    )

                with ui.HStack():
                    with ui.VStack():
                        ui.Button(
                            "Add a random algorithm cube",
                            clicked_fn=generate_random_algorithm_cube,
                        )
                    ui.Button("Delete", clicked_fn=delete, width=110)

    def on_shutdown(self):
        print("[austen.random.cube] austen random cube shutdown")
