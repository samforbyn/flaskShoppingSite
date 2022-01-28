"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, 
                first_name, 
                last_name, 
                email, 
                password):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password


    def __repr__(self):
        """"Convenience method to show custy info in console"""
        return f"Customer: {self.first_name} {self.last_name} Email: {self.email} Password: {self.password}"

    
def read_customers(filepath):
    """ Read customer info and populate dict
    
    Dict will be {email: Customer(...),
                    email: Customer(...)}
    """
    customers_data = {}

    with open(filepath) as f:
        for line in f:
            (first_name,
            last_name,
            email,
            password) = line.strip().split("|")

        customers_data[email] = Customer(first_name,
                                         last_name,
                                         email,
                                         password
                                        )