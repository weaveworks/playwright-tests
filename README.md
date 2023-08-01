# Playwright Tests

### How to run:
make sure that you are in the correct path:
/PlaywrightProjects/test_weave_gitops_enterprise
then

run the login credentials first then the files by this format below to get the test report for example:

`export URL="https://demo-01.wge.dev.weave.works/"`

`export USER_NAME=""`  -------> you can get it from 1password.com

`export PASSWORD=""`  --------> you can get it from 1password.com

`export PYTHONPATH=./`

`pytest -s -v --template=html1/index.html --report=test-results/report.html`