default_graph = tf.get_default_graph()

c1 = tf.constant(1.0)

second_graph = tf.Graph()
with second_graph.as_default():
    c2 = tf.constant(101.0)

session = tf.Session() # открываем сессию на графе по-умолчанию
print(c1.eval(session=session))
# print(c2.eval(session=session)) # так нельзя, не тот граф
session.close()

# тоже самое:
with tf.Session() as session:
    print(c1.eval()) # не нужно передавать сессию в метод eval

# используем другой граф:
with tf.Session(graph=second_graph) as session:
    print(c2.eval()) # не нужно передавать сессию в метод eval
