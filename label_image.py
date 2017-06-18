import tensorflow as tf, sys

# constants
LABELS_FILE = './output_labels.txt'
GRAPH_FILE = './output_graph.pb'

def get_predictions(image_path):
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # parse labels file
    label_lines = [ line.rstrip() for line in tf.gfile.GFile(LABELS_FILE) ]

    # load the trained model from the output graph
    with tf.gfile.FastGFile(GRAPH_FILE, 'rb') as f:
        graph = tf.GraphDef()
        graph.ParseFromString(f.read())
        _ = tf.import_graph_def(graph, name='')

    with tf.Session() as sess:
        # pass the image into the graph as input
        tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(tensor, { 'DecodeJpeg/contents:0': image_data })
        sorted_predictions = predictions[0].argsort()[-len(predictions[0]):][::-1]

        final_predictions = []
        for node in sorted_predictions:
            label = label_lines[node]
            score = predictions[0][node]
            final_predictions.append((label, float(score)))

        return final_predictions

if __name__ == '__main__':
    image_path = sys.argv[1]
    for prediction in get_predictions(image_path):
        print "%s: %.5f" % (prediction[0], prediction[1])
