# diagram.py
from diagrams import Cluster, Diagram
from diagrams.azure.general import Resourcegroups
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.network import Subnets

with Diagram("Diagram of script.ps1","diagram"):
    with Cluster("alpha-resource-groups"):
        with Cluster("alpha-vnet"):
            VirtualNetworks("10.0.0.0/16")
            with Cluster("alpha-subnet"):
                Subnets("10.0.0.0/24")
