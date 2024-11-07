from waitress import serve
import app  # 确保这里导入你的 Flask 应用

if __name__ == '__main__':
    serve(app.app, host='0.0.0.0', port=5001)
