from svmutil import *

y, x = svm_read_problem('train.txt')
yt, xt = svm_read_problem('test.txt')
m = svm_train(y, x ,'-c 1 -t 2 -g 0.5')
svm_predict(yt,xt,m)

print(m)
