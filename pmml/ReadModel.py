
# 读取模型
LR = joblib.load(dirs+'/LR.pkl')
 
test = np.array([[3,4,5],[8,7,6]])
print('预测结果:\n', LR.predict(test))