
# create the cluster
kind create cluster --name hw --config config/kind.config.yaml --wait 5m

# create config map for html file 
kubectl create configmap index.html --from-file html/index.html

# apply the manifest file 
kubectl apply -f manifests/hello_world_hw.yaml

# delete the cluster
# kind delete cluster --name hw