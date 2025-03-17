# Problem with mutable default parameters in Python functions
def add_clients(name, client_list=None):
    if client_list is None:
        client_list = []
    client_list.append(name)
    return client_list


client1 = add_clients('John')
add_clients('Doe', client1)
add_clients('Tho', client1)
client1.append('Toe')

client2 = add_clients('Moe')
add_clients('Foe', client2)

client3 = add_clients('Joe')
add_clients('Zoe', client3)

print(client1)
print(client2)
print(client3)
