class Recreator3D:
    def __init__(self, model="MK5Kit", printer="Ender3"):
        self.model = model
        self.printer = printer
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def list_components(self):
        print("Components for the Recreator 3D - {} - {}:".format(self.model, self.printer))
        for index, component in enumerate(self.components, start=1):
            print("{}. {}".format(index, component))

# Instantiate Recreator3D
recreator = Recreator3D()

# Add components
recreator.add_component("PET Filament Maker")
recreator.add_component("Plastic Pultrusion Unit")

# List components
recreator.list_components()
