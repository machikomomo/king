import os

import simplejson

from flask import Flask, render_template, request

# 类似于springboot application 主类 应用程序，监听所有的网络请求
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# 把别人上传的图片保存在这个路径，如下
app.config['UPLOAD_FOLDER'] = '/tmp/'
# 反正就这么写，如下，启动一个web
bootstrap = Bootstrap(app)


def gen_file_name(filename):
    i = 1
    # 在上方的app config中配置了一个上传目录，用户上传的图片都存到这个目录下
    # join表示路径拼接（tmp+文件名），如果这个路径已经存在了 就去给它编号加一，使他不要重名
    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        # 通过split可以取到文件名以及扩展，类似233.txt txt就是扩展名 扩展名不能修改，去把文件名修改一下
        name, extension = os.path.splitext(filename)
        filename = '%s_%s%s' % (name, str(i), extension)
        i += 1
    return filename


@app.route("/upload", methods=['POST'])
def upload():
    # 我们通常需要接收前端发送过来的文件,flask中以下方这样的方式获取文件对象，然后赋值给变量files，python会自动去识别这个变量名的类型
    files = request.files['file']
    if files:
        # 处理文件名，generate file name生成文件名——将用户传入的文件名接收以后，在本机另给一个文件名
        filename = gen_file_name(files.name)

        #save file to disk
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        files.save(uploaded_file_path)


        #return json for js call back 对于用户上传文件，我，服务器，要予以反馈
        return simplejson.dumps({
            # 返回一个json格式的响应
            # json格式有点像key value的格式
            # 定义一个files的数组
            "files":[{
                "name":"识别结果 : "
            }]
        })



# methods 在网络请求中有很多方法 协议类型 有一些约定 get请求就是用户向服务器拿一个东西，post是用户提交一个东西给服务器(服务器接收一个用户的提交）
# route类似于requemapping
# def index方法名 下面是render template 表示渲染网页
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # 用本机ip启动这个网络服务器
    app.run(host='0.0.0.0')
