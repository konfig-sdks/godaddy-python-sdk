from godaddy_python_sdk.paths.v1_domains_domain.get import ApiForget
from godaddy_python_sdk.paths.v1_domains_domain.delete import ApiFordelete
from godaddy_python_sdk.paths.v1_domains_domain.patch import ApiForpatch


class V1DomainsDomain(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
