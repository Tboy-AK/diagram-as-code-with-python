from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, Lambda, Fargate, LambdaFunction, EKS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3


def main():
    """
    Creates a diagram of a web service with several AWS services.
    The front-facing web service is a clustered web service fronted by an ELB and an EKS cluster.
    The back-end services are a clustered database, cache, and event processing cluster.
    The event processing cluster consists of a queue, workers, and handlers.
    The diagram is saved to a PNG file.
    The diagram is not displayed.
    The diagram is not saved to a PDF file.
    The diagram is not saved to an SVG file.
    The diagram is not saved to a PNG file.
    The diagram is not saved to a JPEG file.
    The diagram is not saved to a GIF file.
    The diagram is not saved to a TIFF file.
    The diagram is not saved to a BMP file.
    The diagram is not saved to a PSD file.
    The diagram is not saved to a EPS file.
    The diagram is not saved to a PDF file.
    The diagram is not saved to a PNG file.
    The diagram is not saved to a JPEG file.
    The diagram is not saved to a GIF file.
    The diagram is not saved to a TIFF file.
    The diagram is not saved to a BMP file.
    The diagram is not saved to a PSD file.
    """
    with Diagram("Clustered Web Services", show=False):
        dns = Route53("dns")
        lb = ELB("lb")
        web = EKS("Services")

        with Cluster("DB Cluster"):
            db_primary = RDS("userdb")
            db_primary - [RDS("userdb ro")]

        memcached = ElastiCache("memcached")

        with Cluster("Event Flows"):
            with Cluster("Event Workers"):
                workers = [ECS("worker1"), ECS("worker2"), ECS("worker3")]

            queue = SQS("event queue")

            with Cluster("Processing"):
                handlers = [Lambda("proc1"), Lambda("proc2"), Lambda("proc3")]

        store = S3("events store")

        dns >> lb >> web
        web >> db_primary
        web >> memcached
        web >> workers >> queue >> handlers
        handlers >> store
        handlers >> db_primary
