
import tensorflow as tf

from ModelEval import ModelEval
from ModelTrainer import ModelTrainer
from iterators.DumbIterator import DumbIterator
from models.DiffTime import DiffTime

vocab_size = 100000
batch_size = 10000
# num_iterations = 99000
num_iterations = 200
num_iter_per_epoch = 100


dataiter = DumbIterator(batch_size, vocab_size)



with tf.Session() as sess:
    model = DiffTime(vocab_size)
    trainer = ModelTrainer(sess, dataiter, model)
    trainer.train_model(batch_size, num_iterations, num_iter_per_epoch)
    modeleval = ModelEval(sess, model)

