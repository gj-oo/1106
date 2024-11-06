# 使用官方 Python 作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . /app

# 安装依赖
RUN pip install -r requirements.txt

# 暴露端口
EXPOSE 8000


# 运行 uWSGI
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# -------------------------本地终端命令执行如下-------------------------
# 构建 Docker 镜像
# docker build -t django_api:v1.0 .

# 运行 Docker 容器
# docker run -p 8000:8000 --name django_api django_api:v1.0

