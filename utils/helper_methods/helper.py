from subprocess import run


def install_policies():
    process = run(f"kubectl apply -f /utils/data/policies.yaml")
    exit_code = process.returncode
    assert exit_code == 0, "Failed to install policies to the cluster"


def install_violated_app():
    process = run(f"kubectl apply -f /utils/data/violated_app.yaml")
    exit_code = process.returncode
    assert exit_code == 0, "Failed to install violated App to the cluster"