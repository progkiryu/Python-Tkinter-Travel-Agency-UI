class AgencyController():
    def __init__(self, model, view):
        self.agency = model
        self.agency_view = view
    def check_administrator(self, username, password) -> bool:
        if self.agency.admins.has_administrator(username, password) == True:
            self.agency.loggedInUser = self.agency.admins.get_administrator(username, password)
            self.agency_view.username = self.agency.loggedInUser.name
            return self.agency.admins.has_administrator(username, password)
        return False
        