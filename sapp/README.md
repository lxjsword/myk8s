1. 加载镜像到minikube虚拟机
minikube image load lxjsword/sapp:v1

2. 挂载宿主机目录到minikube虚拟机
minikube mount /Users/lixiaojian/data/myk8s/sapp/pv:/data/pv &

3. minikube启动端口转发
minikube service sapp-svc
or
minikube tunnel

4. 创建configmap
kubectl create configmap my-config --from-file=./USERNAME
kubectl create configmap config-file --from-file=./config-file
