import tensorflow as tf
from sklearn.preprocessing import scale
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("news_train.csv",header=0,encoding='gb18030')
ds = df.values
x = ds[:,2:]#特征数据
y = ds[:,1]#标签数据

train_num=500
valid_num=100
test_num = len(x)-train_num-valid_num

x_train = x[:train_num]
y_train = y[:train_num]

x_valid = x[train_num:train_num+valid_num]
y_valid = y[train_num:train_num+valid_num]

x_test = x[train_num+valid_num:train_num+valid_num+test_num]
y_test = y[train_num+valid_num:train_num+valid_num+test_num]

x_train=x_train.astype('float32')
x_valid = x_valid.astype('float32')
x_test = x_test.astype('float32')

x_train = tf.cast(scale(x_train),dtype=tf.float32)
x_valid = tf.cast(scale(x_valid),dtype=tf.float32)
x_test = tf.cast(scale(x_test),dtype=tf.float32)

def modle(x,w,b):
    return tf.matmul(x,w)+b

W = tf.Variable(tf.random.normal([20,1],mean=0.0,stddev=1.0,dtype=tf.float32))
B = tf.Variable(tf.zeros(1),dtype=tf.float32)

train_epochs = 50#迭代次数
learning_rate = 0.01#学习率
batch_size = 10#批样本数(超参)

def loss(x,y,w,b):
    error = modle(x,w,b)-y#计算模型预测值和标签
    sqr_err = tf.square(error)#方差
    return tf.reduce_mean(sqr_err)#均方差

def grad(x,y,w,b):
    with tf.GradientTape() as tape:
        loss_ = loss(x,y,w,b)
    return tape.gradient(loss_,[w,b])#梯度向量


#梯度下降优化器
optimizer=tf.keras.optimizers.SGD(learning_rate)#创建优化器


#迭代训练

loss_train_list=[]
loss_valid_list=[]
total_step = int(train_num/batch_size)#迭代轮次

for epoch in range(train_epochs):
    for step in range(total_step):
        xs = x_train[step*batch_size:(step+1)*batch_size,:]
        ys = y_train[step*batch_size:(step+1)*batch_size]

        grads = grad(xs,ys,W,B)#计算梯度
        optimizer.apply_gradients(zip(grads,[W,B]))#调整变量w和b
    loss_train = loss(x_train,y_train,W,B).numpy()
    loss_valid = loss(x_valid,y_valid,W,B).numpy()
    loss_train_list.append(loss_train)
    loss_valid_list.append(loss_valid)

w = W.numpy()
b = B.numpy()
np.save("weight.npy",w)
np.save("intercept.npy",b)
    #print("epoch={:3d},train_loss={:.4f},valid_loss={:.4f}".format(epoch+1,loss_train,loss_valid))
# plt.xlabel("Epoch")
# plt.ylabel("loss")
# plt.plot(loss_train_list,'blue',label='train_loss')
# plt.plot(loss_valid_list,'red',label='valid_loss')
# plt.legend(loc=1)
# plt.show()