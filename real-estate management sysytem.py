class RealEstateManagementSystem:
    def __init__(self):
        self.properties = {}
        self.next_id = 1

    def add_property(self):
        print("\n--- Add Property ---")
        title = input("Enter property title: ")
        location = input("Enter location: ")
        area = input("Enter area (sq ft): ")
        price = input("Enter price: ")
        owner = input("Enter owner name: ")

        self.properties[self.next_id] = {
            "title": title,
            "location": location,
            "area": area,
            "price": price,
            "owner": owner
        }
        print(f"Property added with ID: {self.next_id}")
        self.next_id += 1

    def view_properties(self):
        print("\n--- All Properties ---")
        if not self.properties:
            print("No properties found.")
            return
        for prop_id, details in self.properties.items():
            print(f"ID: {prop_id}")
            for key, value in details.items():
                print(f"  {key.capitalize()}: {value}")
            print("-" * 30)

    def update_property(self):
        print("\n--- Update Property ---")
        try:
            prop_id = int(input("Enter property ID to update: "))
            if prop_id not in self.properties:
                print("Property not found.")
                return
            print("Leave blank to keep current value.")
            title = input(f"Enter new title (current: {self.properties[prop_id]['title']}): ")
            location = input(f"Enter new location (current: {self.properties[prop_id]['location']}): ")
            area = input(f"Enter new area (current: {self.properties[prop_id]['area']}): ")
            price = input(f"Enter new price (current: {self.properties[prop_id]['price']}): ")
            owner = input(f"Enter new owner (current: {self.properties[prop_id]['owner']}): ")

            if title:
                self.properties[prop_id]['title'] = title
            if location:
                self.properties[prop_id]['location'] = location
            if area:
                self.properties[prop_id]['area'] = area
            if price:
                self.properties[prop_id]['price'] = price
            if owner:
                self.properties[prop_id]['owner'] = owner
            print("Property updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid property ID.")

    def delete_property(self):
        print("\n--- Delete Property ---")
        try:
            prop_id = int(input("Enter property ID to delete: "))
            if prop_id in self.properties:
                del self.properties[prop_id]
                print("Property deleted successfully.")
            else:
                print("Property not found.")
        except ValueError:
            print("Invalid input. Please enter a valid property ID.")

    def run(self):
        while True:
            print("\n--- Real Estate Management System ---")
            print("1. Add Property")
            print("2. View Properties")
            print("3. Update Property")
            print("4. Delete Property")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_property()
            elif choice == '2':
                self.view_properties()
            elif choice == '3':
                self.update_property()
            elif choice == '4':
                self.delete_property()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the system
if __name__ == "__main__":
    system = RealEstateManagementSystem()
    system.run()
