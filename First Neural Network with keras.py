from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense 


data= loadtxt('pima-indians-diabetes.csv', delimiter=',')

x = data[ :,0:8]
y = data[ :,8]

model = Sequential()
model.add(Dense(12,input_dim=8, activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='softmax'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
model.fit(x,y,epochs=10,batch_size=8, verbose=1)

acc=model.evaluate(x,y)
print("accuracy:",acc*100)







