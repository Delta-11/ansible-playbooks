# Updated script to use Docker's API
import json
import docker

def get_container_hosts():
    client = docker.from_env()
    containers = client.containers.list()  # Get running containers
    return [container.name for container in containers]

def main():
    hosts = get_container_hosts()

    inventory = {
        "all": {
            "hosts": hosts
        },
        "_meta": {
            "hostvars": {}
        }
    }

    print(json.dumps(inventory))

if __name__ == "__main__":
    main()