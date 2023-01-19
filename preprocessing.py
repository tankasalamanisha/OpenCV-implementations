import tensorflow as tf

def decode_image(filename:str, image_type:str, resize_shape, channels:int=0):
    """
    Function to read an image file and preprocess it 
    Args:
        filename (str): _description_
        image_type (_type_): _description_
        resize_shape (_type_): _description_
        channels (int, optional): _description_. Defaults to 0.
    """
    raw_file = tf.io.read_file(f'{filename}.{image_type}')
    image = tf.image.decode_png(raw_file, channels=channels)
    image.set_shape(resize_shape)
    return image
    