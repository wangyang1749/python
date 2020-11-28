from io import BytesIO
import base64
import matplotlib.pyplot as plt


# plt.plot([1,2,3,4])
fig = plt.figure(figsize=(10, 10))

plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel("some numbers")
# plt.savefig('./test2.png')

sio = BytesIO()
fig.savefig(sio, format='png', bbox_inches='tight', pad_inches=0.0)
data = base64.encodebytes(sio.getvalue()).decode()
src = 'data:image/png;base64,' + str(data)
print(src)
plt.show()