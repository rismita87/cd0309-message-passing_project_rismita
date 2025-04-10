import grpc
import personlist_pb2
import personlist_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:30021') as channel:
        stub = personlist_pb2_grpc.PersonServiceStub(channel)
        response = stub.GetAllPersons(personlist_pb2.EmptyRequest())
        print("Received persons:")
        for person in response.people:
            print(f"{person.id} {person.first_name} {person.last_name} {person.company_name}")

if __name__ == '__main__':
    run()