import sys
from wxcloudrun import create_app

app = create_app()

# 启动Flask Web服务
if __name__ == '__main__':
    if len(sys.argv) > 2:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        host = '0.0.0.0'
        port = 5000  # 默认端口号，可以根据需要调整

    app.run(host=host, port=port)
