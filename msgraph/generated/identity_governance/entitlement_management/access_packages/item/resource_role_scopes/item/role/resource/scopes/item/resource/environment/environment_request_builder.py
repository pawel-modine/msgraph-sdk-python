from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .............models.access_package_resource_environment import AccessPackageResourceEnvironment
    from .............models.o_data_errors.o_data_error import ODataError

class EnvironmentRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the environment property of the microsoft.graph.accessPackageResource entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EnvironmentRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}/resourceRoleScopes/{accessPackageResourceRoleScope%2Did}/role/resource/scopes/{accessPackageResourceScope%2Did}/resource/environment{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[EnvironmentRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessPackageResourceEnvironment]:
        """
        Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageResourceEnvironment]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .............models.access_package_resource_environment import AccessPackageResourceEnvironment

        return await self.request_adapter.send_async(request_info, AccessPackageResourceEnvironment, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[EnvironmentRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    @dataclass
    class EnvironmentRequestBuilderGetQueryParameters():
        """
        Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EnvironmentRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[EnvironmentRequestBuilder.EnvironmentRequestBuilderGetQueryParameters] = None

    
