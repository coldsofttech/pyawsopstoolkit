from pyawsopstoolkit import Session
from pyawsopstoolkit.advsearch import IAM

if __name__ == "__main__":
    session = Session(profile_name='WS-00GM-role_DsAudit')
    account = '550550390011'
    role_arn = f'arn:aws:iam::{account}:role/{account}-role_DsAuditReadOnly'
    assume_role_session = session.assume_role(role_arn)
    iam = IAM(assume_role_session)
    roles = iam.search_roles(condition='AND', tag={'test': 'test'})
    for role in roles:
        print(role)
