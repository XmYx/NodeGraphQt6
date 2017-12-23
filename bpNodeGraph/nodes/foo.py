from bpNodeGraph.interfaces import Node


class FooNode(Node):
    """
    A node class with 2 inputs and 2 outputs.
    """
    NODE_TYPE = 'FooNode'

    def __init__(self):
        super(FooNode, self).__init__()
        self.set_name('Foo')

        # create node inputs
        self.add_input('foo')
        self.add_input('bar')

        # create node outputs
        self.add_output('apples')
        self.add_output('bananas')