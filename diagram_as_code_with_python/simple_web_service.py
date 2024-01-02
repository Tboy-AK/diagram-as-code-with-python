from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


def main():
    """
    Creates a diagram of a web service with an ELB, EC2, and RDS database.
    """
    # Create the diagram.
    # Diagram("Web Service", show=False)
    # Create the nodes.
    # ELB("lb") >> EC2("web") >> RDS("userdb")
    # Display the diagram.
    # Diagram("Web Service", show=False).save("web_service.png")
    # Create the diagram.
    # Diagram("Web Service", show=False)
    # Create the nodes.
    # ELB("lb") >> EC2("web") >> RDS("userdb")
    # Display the diagram.
    # Diagram("Web Service", show=False).save("web_service.png")
    # Create the diagram.
    # Diagram("Web Service", show=False)
    # Create the nodes.
    # ELB("lb") >> EC2("web") >> RDS("userdb")
    # Display the diagram.
    with Diagram("Web Service", show=False):
        ELB("lb") >> EC2("web") >> RDS("userdb")
