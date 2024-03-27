class Waypoint:
    def __init__(self, location, description):
        # Initialize waypoint with location, description, and links to next and previous waypoints
        self.location = location
        self.description = description
        self.next = None
        self.prev = None

class Route:
    def __init__(self):
        # Initialize the route with no waypoints
        self.head = None

    def add_waypoint(self, location, description):
        # Adding a new waypoint to the end of the route
        new_waypoint = Waypoint(location, description)
        if not self.head:
            # If the route is empty, set the new waypoint as the head
            self.head = new_waypoint
        else:
            # Traverse to the end of the route and append the new waypoint
            current = self.head
            while current.next:
                current = current.next
            current.next = new_waypoint
            new_waypoint.prev = current

    def remove_waypoint(self, location):
        # Remove a waypoint from the route based on its location
        current = self.head
        while current:
            if current.location == location:
                # If the waypoint to remove is found
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
        print("Waypoint not found.")

    def traverse_forward(self):
        # Traverse the route in a forward direction and print each waypoint
        current = self.head
        while current:
            print(f"Location: {current.location}, Description: {current.description}")
            current = current.next

    def traverse_backward(self):
        # Traverse the route in a backward direction and print each waypoint
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(f"Location: {current.location}, Description: {current.description}")
            current = current.prev

# The Demonstration 
def main():
    route = Route()
    # let's add five way points to the route
    route.add_waypoint("A", "Description A")
    route.add_waypoint("B", "Description B")
    route.add_waypoint("C", "Description C")
    route.add_waypoint("D", "Description D")
    route.add_waypoint("E", "Description E")

    # how to remove a waypoint from the route
    route.remove_waypoint("B")

    # how to traverse the route in a forward direction
    print("Traversing in a forward direction:")
    route.traverse_forward()

    # Traverse the route in a backward direction
    print("\nTraversing in a backward direction:")
    route.traverse_backward()

if __name__ == "__main__":
    main()
