from Destination import Destination

class DestinationsController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def set_destinations(self, end):
        self.view.destination_list.delete(0, end)
        self.view.country_list.delete(0, end)
        destinations = self.model.destinations.destinations
        for d in destinations:
            self.view.destination_list.insert(end, d.name)
            self.view.country_list.insert(end, d.country)
    def filter_destinations(self, country, end):
        self.view.destination_list.delete(0, end)
        self.view.country_list.delete(0, end)
        filtered_destinations = self.model.destinations.get_filtered_destinations(country)
        for d in filtered_destinations:
            self.view.destination_list.insert(end, d.name)
            self.view.country_list.insert(end, d.country)
    def add_destination(self, name, country, version):
        self.model.destinations.add_destination(Destination(name, country), version)
    def remove_destination(self, name, country):
        self.model.destinations.remove_destination(name, country)
