from io import BytesIO
import base64
import matplotlib.pyplot as plt
from flask import Flask, request, Response
# https://blog.csdn.net/qq965194745/article/details/80034291?utm_source=blogxgwz3
app = Flask(__name__)
html = '''
    <html>
        <body>
            <img src="data:image/png;base64,{}" />
        </body>
    <html>
'''

def getPlot():
    # plt.plot([1,2,3,4])
    fig = plt.figure(figsize=(10, 10))

    plt.plot([1,2,3,4],[1,4,9,16])
    plt.ylabel("some numbers")
    # plt.savefig('./test2.png')

    sio = BytesIO()
    fig.savefig(sio, format='png', bbox_inches='tight', pad_inches=0.0)
    data = base64.encodebytes(sio.getvalue()).decode()
    # src = 'data:image/png;base64,' + str(data)
    src = str(data)
    
    return html.format(src)
    # plt.show()


@app.route("/render")
def render():
    try:
        print(getPlot())
        return getPlot()
    except Exception as ex:
        print(ex)
        return Response(status=500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9988, debug=True)

