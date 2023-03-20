# 基础镜像
FROM node:14.18.0-alpine3.13 AS build-stage

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . .

# 安装依赖和构建项目
RUN npm install && npm run build

# 创建一个新的Nginx镜像
FROM nginx:1.21.3-alpine

# 将构建好的Vue项目复制到Nginx默认目录下
COPY /app/dist /usr/share/nginx/html

# 将Nginx配置文件复制到容器中
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
# 暴露Nginx的80端口
EXPOSE 80

# 启动Nginx
CMD ["nginx", "-g", "daemon off;"]
