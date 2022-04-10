"""this is restaurant.py"""
#-----------------------------------------------------------------------
# restaurant.py
#-----------------------------------------------------------------------
# Rowstring[0] -> restaurantid
# rowstring[1] -> name
class restaurant:
    """class Restaurant"""

    # Note: Rowstring is a list of inputs that needs to go into a restaurant
    def __init__(self, rowstring):
        # --- The following will be modified to work for restaurants
        self._restaurantid = rowstring[0]
        self._name = rowstring[1]
        self._openclose = rowstring[2]
        self._tag = rowstring[3]
        self._address = rowstring[4]
        self._stars = rowstring[5]
        self._cuisine = rowstring[6]
        self._type = rowstring[7]
        self._price = rowstring[8]

        # self._dept = rowstring[1]
        # self._course_num = rowstring[2]
        # self._area = rowstring[3]
        # self._title = rowstring[4]
        # self._details = details


    # def __str__(self):
    # # --- The following will be modified to work for restaurants
    #     string_form = str(self._name) + ' '
    #     # string_form += str(self._dept) + ' '
    #     # string_form += str(self._course_num) + ' '
    #     # string_form += str(self._area) + ' '
    #     # string_form += str(self._title)
    #     return string_form

    # Make sure to have name
    def get_name(self):
        """course ID"""
        return self._name

    def get_restaurantid(self):
        """restaurant ID"""
        return self._restaurantid

    def get_tag(self):
        """restaurant ID"""
        return self._tag

    def get_openclose(self):
        """restaurant ID"""
        return self._openclose

    def get_address(self):
        """restaurant ID"""
        return self._address

    def get_stars(self):
        """restaurant ID"""
        return self._stars

    def get_address(self):
        """restaurant ID"""
        return self._address

    def get_stars(self):
        """restaurant ID"""
        return self._stars

    def get_cuisine(self):
        """restaurant ID"""
        return self._cuisine

    def get_type(self):
        """restaurant ID"""
        return self._type

    def get_price(self):
        """restaurant ID"""
        return self._price



    # def get_title(self):
    #     """title"""
    #     return self._title

    # Example of get functions
    # def get_courseid(self):
    #     """course ID"""
    #     return self._courseid
    # def get_dept(self):
    #     """department"""
    #     return self._dept
    # def get_coursenum(self):
    #     """course number"""
    #     return self._course_num
    # def get_area(self):
    #     """area"""
    #     return self._area
    # def get_title(self):
    #     """title"""
    #     return self._title
