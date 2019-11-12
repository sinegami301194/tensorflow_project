import tensorflow as tf
default_graph = tf.get_default_graph()
c1 = tf.constant(1.0)
second_graph = tf.Graph()
with second_graph.as_default(): 
     # в этом блоке мы работаем во втором графе 
     c2 = tf.constant(101.0)
print(c2.graph is second_graph, c1.graph is second_graph) # True, False
print(c2.graph is default_graph, c1.graph is default_graph) # False, True
