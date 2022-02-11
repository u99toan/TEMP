import tensorflow as tf

if tf.test.is_gpu_available():
    print("Running on GPU")
else:
    print("Running on CPU")