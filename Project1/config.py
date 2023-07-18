from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base



SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Kaa40N2oi!#Q@agilisium-innovation-lab.cabfbspytumf.us-west-2.rds.amazonaws.com/Automated_Data_Lake"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
sessionlocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)
Base = declarative_base()

async def get_db():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()


EMR_INSTNACE_POLICY_ARN = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role"

EMR_CLUSTER_POLICY_ARN = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole"
EMR_CLASSIC_RELEASE_LABEL='emr-6.10.0'

KUBERNETES_CLUSTER_VERSION = '1.26'

NODE_GROUP_INSTANCE_CAPACITY = 'SPOT'
NODE_GROUP_EBS_STORAGE_SIZE = 10
NODE_GROUP_AMI_TYPE = 'AL2_x86_64'
RDS_DB_ALLOCATED_STORAGE=100
RDS_ENGINE='postgres'
RDS_ENGINE_VERSION = '15.2'


IAMServices =["elasticmapreduce.amazonaws.com", "ec2.amazonaws.com",
                                "s3.amazonaws.com", "eks.amazonaws.com",
                                "secretsmanager.amazonaws.com", "airflow-env.amazonaws.com",
                                "airflow.amazonaws.com", "rds.amazonaws.com"]

#File contains the actions which are dedicated for different role and AWS Services.
DatabricksAdminActions = [
    "ec2:AssociateIamInstanceProfile",
    "ec2:AttachVolume",
    "ec2:AuthorizeSecurityGroupEgress",
    "ec2:AuthorizeSecurityGroupIngress",
    "ec2:CancelSpotInstanceRequests",
    "ec2:CreateTags",
    "ec2:CreateVolume",
    "ec2:DeleteTags",
    "ec2:DeleteVolume",
    "ec2:Describe*",
    "ec2:DetachVolume",
    "ec2:DisassociateIamInstanceProfile",
    "ec2:ReplaceIamInstanceProfileAssociation",
    "ec2:RequestSpotInstances",
    "ec2:RevokeSecurityGroupEgress",
    "ec2:RevokeSecurityGroupIngress",
    "ec2:RunInstances",
    "ec2:TerminateInstances"
]
userS3 = ["s3:Get*",
          "s3:List*"]

adminS3 =["s3:*"]

DatabricksUserActions = [
    "ec2:Describe*",
    "ec2:RunInstances",
    "ec2:TerminateInstances"
]

EmrClassicAdminAcitons = [
    "elasticmapreduce:AddInstanceFleet",
    "elasticmapreduce:AddInstanceGroups",
    "elasticmapreduce:AddJobFlowSteps",
    "elasticmapreduce:Describe*",
    "elasticmapreduce:GetManagedScalingPolicy",
    "elasticmapreduce:GetAutoTerminationPolicy",
    "elasticmapreduce:List*",
    "elasticmapreduce:ModifyCluster",
    "elasticmapreduce:SetTerminationProtection",
    "elasticmapreduce:RunJobFlow",
    "elasticmapreduce:TerminateJobFlows"
]

EmrClassicUserAcitons = [
    "elasticmapreduce:Describe*",
    "elasticmapreduce:GetBlockPublicAccessConfiguration",
    "elasticmapreduce:GetManagedScalingPolicy",
    "elasticmapreduce:GetAutoTerminationPolicy",
    "elasticmapreduce:List*",
    "elasticmapreduce:RunJobFlow",
    "elasticmapreduce:ViewEventsFromAllClustersInConsole"
]

EmrServerlessAdminActions = [
    "emr-serverless:CreateApplication",
    "emr-serverless:UpdateApplication",
    "emr-serverless:DeleteApplication",
    "emr-serverless:ListApplications",
    "emr-serverless:GetApplication",
    "emr-serverless:StartApplication",
    "emr-serverless:StopApplication",
    "emr-serverless:StartJobRun",
    "emr-serverless:CancelJobRun",
    "emr-serverless:ListJobRuns",
    "emr-serverless:GetJobRun"
]

EmrServerlessUserActions = [
    "emr-serverless:ListApplications",
    "emr-serverless:GetApplication",
    "emr-serverless:StartApplication",
    "emr-serverless:StopApplication",
    "emr-serverless:StartJobRun",
    "emr-serverless:CancelJobRun",
    "emr-serverless:ListJobRuns",
    "emr-serverless:GetJobRun"
]

MWAAUserActions =[
    "airflow:GetEnvironment",
    "airflow:ListEnvironments"
]

MWAAAdminActions = [
    "airflow:CreateEnvironment",
    "airflow:UpdateEnvironment",
    "airflow:DeleteEnvironment",
    "airflow:ListTagsForResource",
    "airflow:CreateWebLoginToken",
    "airflow:CreateCliToken",
    "airflow:PublishMetrics",
    "airflow:GetEnvironment",
    "airflow:ListEnvironments"
]

EKSAdminActions = []

EKSUserActions = []


requirements="""
           --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.1/constraints-3.10.txt"

            apache-airflow-providers-databricks==4.0.0
            """