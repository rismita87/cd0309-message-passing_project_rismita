# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import colour_pb2
import colour_pb2_grpc


class ColourGetter(colour_pb2_grpc.ColourProviderServicer):
    def getColour(self, request, context):

        colour_value = "white"
        print(f"count of contacts, {request.name}!")
        request_number = int(request.name)
        if request_number<2:
            colour_value = "yellow"
        elif request_number>=2 and request_number<=3 :
            colour_value = "blue"
        elif request_number>3 :
            colour_value = "red"
        else:
            colour_value = "white"
        return colour_pb2.ColourReply(message=colour_value)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    colour_pb2_grpc.add_ColourProviderServicer_to_server(ColourGetter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
