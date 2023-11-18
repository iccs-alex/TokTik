# Alex's TikTok Clone

### I have 4 submodules in my repo:

&nbsp;&nbsp;&nbsp;&nbsp;The frontend repo's relative path is **./frontend/codebase**

&nbsp;&nbsp;&nbsp;&nbsp;The backend repo's relative path is **./backend/codebase**

&nbsp;&nbsp;&nbsp;&nbsp;The repo for the video workers has the relative path **./TokTik_Workers**

&nbsp;&nbsp;&nbsp;&nbsp;The socketIO server repo's relative path is **./socketio**

<br/><br/>

**First**, when you clone the project, make sure to clone the submodules as well.

<br/><br/>

**Then**, you need to have the traefik ingress controller running, the easiest way is to use helm by running the following commands:
  ```
    helm repo add traefik https://traefik.github.io/charts

    helm repo update

    helm install traefik traefik/traefik
  ```

<br/><br/>

**Finally**, get the K8S cluster up and running with the following command:
  ```
    kubectl apply -R -f k8s
  ```

<br/><br/>

**Now**, just open up a browser window and type *'localhost'* as the URL (use *'127.0.0.1'* if there are issues).
