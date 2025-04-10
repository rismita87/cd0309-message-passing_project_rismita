from concurrent import futures
import logging

import grpc
import personlist_pb2_grpc
import personlist_pb2
import requests

# PEOPLE = [
#     personlist_pb2.Person(id=1, name="Alice"),
#     personlist_pb2.Person(id=2, name="Bob"),
#     personlist_pb2.Person(id=3, name="Charlie")
# ]


API_URL = "http://udaconnect-api-abhi-personservice:5000/person_api/persons"

class PersonListGetter(personlist_pb2_grpc.PersonServiceServicer):
    def GetAllPersons(self, request, context):
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            context.set_details(f"API request failed: {e}")
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return personlist_pb2.PersonList()
        person_list = personlist_pb2.PersonList()

        for item in data:
            person = personlist_pb2.Person(
                id=item.get('id', 0),
                first_name=item.get('first_name', ''),
                last_name=item.get('last_name', ''),
                company_name=item.get('company_name', '')
            )
            person_list.people.append(person)
        return person_list

def serve():
    port = "50089"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    personlist_pb2_grpc.add_PersonServiceServicer_to_server(PersonListGetter(),server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()