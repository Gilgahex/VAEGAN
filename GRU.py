import tensorflow as tf

cell = tf.nn.rnn_cell.GRUCell(CELLSIZE)
mcell - tf.nn.rnn_cell.MultiRNNCell([cell]*NLAYERS, state_is_tuple=False)
Hr, H = tf.nn.dynamic_rnn(mcell, X ,initial_state = Hin)

