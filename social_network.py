class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} does not exist")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} does not exist")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")

# Test your code here
alex = Person("Alex")
jordan = Person("Jordan")
print(alex.friends) 
alex.add_friend(jordan)
print(alex.friends[0].name)

network = SocialNetwork()

people = ["Sam", "Alex", "Jordan", "Taylor", "Joe", "Jane","Chris"] # 7 people
for name in people:
    network.add_person(name)

# Edge Case 1: Duplicate names
sam_before = network.people["Sam"]
network.add_person("Sam") 
print("People count:", len(network.people))  # 7
print()

network.add_friendship("Sam", "Alex")
network.add_friendship("Sam", "Jordan")
network.add_friendship("Alex", "Taylor")
network.add_friendship("Jordan", "Joe")
network.add_friendship("Taylor", "Jane")
network.add_friendship("Joe", "Jane")
network.add_friendship("Jane", "Chris")
network.add_friendship("Alex", "Chris")
network.add_friendship("Sam", "Taylor")

# Edge Case 2: Non-existent person
network.add_friendship("Sam", "Zoe")
network.add_friendship("Zoe", "Sam")  
network.add_friendship("Zoe", "Liam") 

print()
network.print_network()
print()

# Printing network after additions
network.add_person("Bunker")
network.add_friendship("Bunker", "Sam")
network.add_friendship("Bunker", "Alex")
network.print_network()


"""
A graph is the right choice for a social network because a social network is really just a bunch of people connected to each other.
Each person is a node and each friendship is an edge that connects two people. Friendships go both ways, so when I add Sam and Alex as friends,
Sam goes on Alexs list and Alex goes on Sams list.

A list would not work as well because it only keeps people in order. It has no way to show who is friends with who, 
so I would have to search the whole thing to find connections. A tree is closer, but every node in a tree only has 
one parent and you can’t have loops. In my network Sam, Alex, and Taylor are all friends with each other.


I used an adjacency list, where a dictionary points each name to a Person and each Person has a list of friends. 
Finding someone by name is really fast because a dictionary can jump straight to the key. 
Adding a friend is pretty quick too, but my add_friend method checks if the friend is already in the list,
and that check has to go through the whole list. For someone with thousands of friends that would get slow, 
so a set would be a better choice. Printing the network has to go through every person and every friend, 
so it takes longer the bigger the network gets. An adjacency matrix would make checking a friendship faster, 
but it would waste a lot of space storing empty spots for people who aren’t friends.
"""