from typing import Awaitable, Callable, Dict, List, Literal, Optional, Union

from autogen_core.models import ModelCapabilities
from typing_extensions import Required, TypedDict


class ResponseFormat(TypedDict):
    type: Literal["text", "json_object"]


class CreateArguments(TypedDict, total=False):
    frequency_penalty: Optional[float]
    logit_bias: Optional[Dict[str, int]]
    max_tokens: Optional[int]
    n: Optional[int]
    presence_penalty: Optional[float]
    response_format: ResponseFormat
    seed: Optional[int]
    stop: Union[Optional[str], List[str]]
    temperature: Optional[float]
    top_p: Optional[float]
    user: str


AsyncAzureADTokenProvider = Callable[[], Union[str, Awaitable[str]]]


class BaseOpenAIClientConfiguration(CreateArguments, total=False):
    model: str
    api_key: str
    timeout: Union[float, None]
    max_retries: int
    model_capabilities: ModelCapabilities
    """What functionality the model supports, determined by default from model name but is overriden if value passed."""


# See OpenAI docs for explanation of these parameters
class OpenAIClientConfiguration(BaseOpenAIClientConfiguration, total=False):
    organization: str
    base_url: str


class AzureOpenAIClientConfiguration(BaseOpenAIClientConfiguration, total=False):
    # Azure specific
    azure_endpoint: Required[str]
    azure_deployment: str
    api_version: Required[str]
    azure_ad_token: str
    azure_ad_token_provider: AsyncAzureADTokenProvider


__all__ = ["AzureOpenAIClientConfiguration", "OpenAIClientConfiguration"]
