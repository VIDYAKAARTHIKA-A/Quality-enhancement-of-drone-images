#imports all fucntions and classes from the mode module
from mode import *
#used for parsing command-line arguments
import argparse

#This line creates an ArgenmentParser object to define and parse command line arguments
parser = argparse.ArgumentParser()

def str2bool(v):
    return v.lower() in ('true')

#path to low resolution images
parser.add_argument("--LR_path", type = str, default = r"D:\IIITDMK summer internship 2024\Task 8- implementation of SRGAN\train_LR_new")

#path to the ground truth
parser.add_argument("--GT_path", type = str, default = r"D:\IIITDMK summer internship 2024\Task 8- implementation of SRGAN\train_HR_new")

#number of residual blocks
parser.add_argument("--res_num", type = int, default = 32)

#number of subprocesses to use for data loading
parser.add_argument("--num_workers", type = int, default = 0)

#number of samples per batch
parser.add_argument("--batch_size", type = int, default = 16)

#coefficient of L2 loss
parser.add_argument("--L2_coeff", type = float, default = 1.0)

#coefficient of adversarial loss
parser.add_argument("--adv_coeff", type = float, default = 1e-3)

#coefficient of total variation loss
parser.add_argument("--tv_loss_coeff", type = float, default = 0.0)

#number of epochs for pre-training
parser.add_argument("--pre_train_epoch", type = int, default = 0)

#number of epochs for fine-tuning
parser.add_argument("--fine_train_epoch", type = int, default =100)

#upscaling factor for super-resolution
parser.add_argument("--scale", type = int, default = 4)

#patch size of training
parser.add_argument("--patch_size", type = int, default = 24)

#layer of VGG network to use for feature loss
parser.add_argument("--feat_layer", type = str, default = 'relu5_4')

#coefficient to rescale VGG feature loss
parser.add_argument("--vgg_rescale_coeff", type = float, default = 0.01)

#boolean indicating whether to fine tune or not
parser.add_argument("--fine_tuning", type = str2bool, default = False)

#boolean to indicate whether data to be loaded in memory or not
parser.add_argument("--in_memory", type = str2bool, default = True)

#path to a pre-trained model
parser.add_argument("--generator_path", type = str)

#mode to run the script in default is train
parser.add_argument("--mode", type = str, default = 'train')

args = parser.parse_args()

if args.mode == 'train':
    train(args)
    
elif args.mode == 'test':
    test(args)
    
elif args.mode == 'test_only':
    test_only(args)
