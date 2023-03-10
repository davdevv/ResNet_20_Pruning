from torch.nn.modules.batchnorm import _BatchNorm
from IPython.display import clear_output
import matplotlib.pyplot as plt
import os



def print_metrics(loss, acc):
    epoch = len(loss['train'])
    clear_output(True)
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    fig.suptitle(f'Epoch #{epoch}')
    ax[0].set_title('loss')
    ax[0].plot(loss['train'], 'r.-', label='train')
    ax[0].plot(loss['test'], 'g.-', label='test')
    ax[0].legend()
    ax[1].set_title('accuracy')
    ax[1].plot(acc['train'], 'r.-', label='train')
    ax[1].plot(acc['test'], 'g.-', label='test')
    ax[1].legend()
    plt.show()


def create_checkoint_dir(root, model_name, dataset_name):
    checkpoint_dir = os.path.join(root, model_name, dataset_name)
    if not os.path.exists(checkpoint_dir):
        os.makedirs(checkpoint_dir)
    return checkpoint_dir
