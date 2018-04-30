from model import *


config = {}

config['model_tag'] = 'rms_first_model'

# Model info
config['num_layers'] = 4
config['hidden_units'] = 128
config['embed_size'] = 128
config['lr'] = 1e-4
config['batch_size'] = 128
config['mini_batch'] = True

config['check_iter'] = 200
config['total_iter'] = 10000
config['save_iter'] = 2000
config['save_dir'] = 'checkpoints/'

config['ld_l2'] = 0.004


def main():
    config['train_x'] = np.load('/st1/rjw0205/cs408/data_set/data51000.npy')
    config['train_y'] = np.load('/st1/rjw0205/cs408/data_set/ydata50100.npy')
    config['val_x'] = np.load('/st1/rjw0205/cs408/data_set/val_x.npy')
    config['val_y'] = np.load('/st1/rjw0205/cs408/data_set/val_y.npy')
    config['eval_x'] = np.load('/st1/rjw0205/cs408/data_set/eval_x.npy')
    config['eval_y'] = np.load('/st1/rjw0205/cs408/data_set/eval_y.npy')
    config['num_features'] = config['train_x'].shape[1] * config['train_x'].shape[2]  # 140 * 15 = 2100
    config['num_champions'] = config['train_x'].shape[1]  # 140

    config['train_x'] = config['train_x'].reshape((-1, config['num_features']))
    config['train_y'] = config['train_y'].reshape((-1, config['num_champions']))

    config['val_x'] = config['val_x'].reshape((-1, config['num_features']))
    config['val_y'] = config['val_y'].reshape((-1, config['num_champions']))

    config['eval_x'] = config['eval_x'].reshape((-1, config['num_features']))
    config['eval_y'] = config['eval_y'].reshape((-1, config['num_champions']))

    # GPU Option
    gpu_options = tf.GPUOptions(allow_growth=True)
    sess = tf.InteractiveSession(config=tf.ConfigProto(gpu_options=gpu_options))
    config['sess'] = sess

    config['sess'] = tf.InteractiveSession()

    with tf.Session() as sess:
        model = MODEL(config)
        model.build_model()
        model.run()


if __name__ == '__main__':
    main()
