# Playwright Tests

### How to run tests locally:

This is a guide to quickly setup the environment to run and debug tests locally on a kind cluster.

There are some prerequisites before running tests locally. It includes installing required tools and environment configurations.

  ## Tools  & Utilities

It is recommended to install latest and stable version of these tools. All tools must be on path.
| Tool | Purpose | Installation |
|--|--|--|
| Docker | Containers runtime environment | `https://docs.docker.com/get-docker` |
| Kind | Running local Kubernetes cluster | `https://kind.sigs.k8s.io/docs/user/quick-start#installation` |
|Kubectl|Kubernetes command-line tool| `https://kubernetes.io/docs/tasks/tools/install-kubectl-linux` |
| Helm | Package manager for Kubernetes | `https://helm.sh/docs/intro/install` |
| Playwright |  a framework for Web Testing and Automation | `https://playwright.dev/docs/intro#installing-playwright`|
| flux | Command-line interface to bootstrap and interact with Flux | `https://fluxcd.io/docs/installation/#install-the-flux-cli`|
| Playwright chromium browser | a browser binary which playwright needs to operate and run tests | After installing Playwright run `playwright install chromium`<br> you can also check this page for more info. <br> `ghttps://playwright.dev/docs/browsers`
| Pytest | a testing framework that allows users to write test codes using Python programming language.  | `https://docs.pytest.org/en/7.1.x/getting-started.html` |
| pytest-reporter-html1 | A basic HTML report for pytest using Jinja2 template engine.   | `https://pypi.org/project/pytest-reporter-html1/` |

## Environment Setup
1. Clone the repo<br/>
    ```bash
    git clone git@github.com:weaveworks/playwright-tests.git
    ```

2. Open it in any IDE like **PyCharm** or **VS Code**<p>&nbsp;</p>

3. Run **Docker Desktop**<p>&nbsp;</p>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for help check this URL `https://docs.docker.com/desktop/install/ubuntu/#launch-docker-desktop` <p>&nbsp;</p>

4. Delete any existing kind cluster(s).<p>&nbsp;</p> 
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`kind delete clusters --all`<p>&nbsp;</p>

5. Create a new clean kind cluster.<p>&nbsp;</p>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./utils/scripts/mgmt-cluster-setup.sh kind  $(pwd) playwright-mgmt-kind`<p>&nbsp;</p>

6. Setup core and enterprise controllers<p>&nbsp;</p>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./utils/scripts/wego-enterprise.sh setup ./utils/scripts`<p>&nbsp;</p>

7. Install violating-app<p>&nbsp;</p>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`kubectl create secret generic git-provider-credentials -n flux-system --from-literal=username="weave-gitops-bot" --from-literal=password="${{ secrets.WEAVEWORKS_BOT_TOKEN }}"`

     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sed -i 's/BRANCH_NAME/<your_brnach_name>/' ./utils/data/violating-podinfo-kustomization.yaml`

     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`kubectl apply -f  ./utils/data/violating-podinfo-kustomization.yaml`<p>&nbsp;</p>

8. Install policies<p>&nbsp;</p>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`kubectl apply -f  ./utils/data/policies.yaml`<p>&nbsp;</p>

9. Flux reconcile violating app<p>&nbsp;</p>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`flux reconcile kustomization violating-podinfo -n default --with-source || true`
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`kubectl get pods -A`


## Run Tests

`export URL="http://localhost:8000"`

`export USER_NAME=""`  -------> you can get it from [./utils/scripts/resources/cluster-user-auth.yaml](./utils/scripts/resources/cluster-user-auth.yaml)

`export PASSWORD=""`  --------> you can get it from [./utils/scripts/resources/cluster-user-auth.yaml](./utils/scripts/resources/cluster-user-auth.yaml)

`export PYTHONPATH=./`

`pytest -s -v --template=html1/index.html --report=test-results/report.html`