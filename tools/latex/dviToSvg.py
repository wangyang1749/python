import os
import signal
import subprocess

from flask import Flask, request, Response

app = Flask(__name__)

file_id = 0
latex_dir = os.path.join(os.path.expanduser("~"), "latex-server")
if not os.path.exists(latex_dir):
    os.mkdir(latex_dir)


def run_command(s, log_file):
    pro = subprocess.Popen(s, shell=True, preexec_fn=os.setsid)
    try:
        pro.wait(1)  # 最多等待1秒钟
    except Exception as ex:
        print(ex)
        # pro.terminate()
        os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # 杀死一个进程组
        raise ex


def gets(formula):
    global file_id
    file_id += 1
    now = file_id
    tex_file, dvi_file, svg_file, log_file = [
        os.path.join(latex_dir, "{}.{}".format(now, file_type))
        for file_type in "tex dvi svg log".split()
    ]
    open(tex_file, mode="w").write(
        r"""
            \documentclass{minimal}
            \usepackage{amsmath}
            \begin{document}
            $$%s$$
            \end{document}
                """
        % formula
    )
    try:
        run_command(
            "latex  --interaction=nonstopmode --output-directory  {} {}".format(
                latex_dir, tex_file
            ),
            log_file,
        )
        run_command(
            "dvisvgm --no-fonts --no-styles -c2,2 -o {} {}".format(svg_file, dvi_file),
            log_file,
        )
        svg = open(svg_file).read()  # 如果不存在，那就直接抛出异常吧
        return svg
    except Exception as ex:
        raise ex
    finally:
        # 清理文件
        for i in "tex dvi log aux svg".split():
            filename = os.path.join(latex_dir, "{}.{}".format(now, i))
            if os.path.exists(filename):
                os.remove(filename)


@app.route("/render")
def render():
    formula = request.args["formula"]
    try:
        resp = gets(formula)
        return Response(response=resp, headers={"Content-Type": "image/svg+xml"})
    except Exception as ex:
        print(ex)
        return Response(status=500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9988, debug=True)

