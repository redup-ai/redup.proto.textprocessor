from typing import List, Tuple, Iterable, Dict
from google.protobuf.json_format import MessageToDict
from redup_servicekit.grpc.client import BasicAsyncClient

from .redup.textprocessor.v1.textprocessor_pb2 import (
    ProcessTextRequest
)
from .textprocessor_pb2_grpc import TextProcessorStub


class Client(BasicAsyncClient):

    def __init__(self, host: str, *argc, **argv):
        super(Client, self).__init__(host, TextProcessorStub, *argc, **argv)

    async def process_text(
        self,
        request_id: str,
        text: str,
        timeout: int=None,
        metadata: Tuple[Tuple[str, str]] = (),
    ) -> Dict:
        return MessageToDict(
            await self.send(
                ProcessTextRequest(
                    request_id=request_id,
                    text=text
                ),
                "ProcessText",
                timeout=timeout,
                metadata=metadata,
            ),
            preserving_proto_field_name=True,
            use_integers_for_enums=False,
            always_print_fields_with_no_presence=True,
        )