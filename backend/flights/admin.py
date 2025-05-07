from django.contrib import admin
from .models.route import Route
from .models.flight import Flight
from .models.travel_class import TravelClass
from .models.price import Price
from .models.passenger import Passenger
from .models.booking import Booking
from .models.pickup_drop_service import PickupDropService
from .models.meal_option import MealOption
from .models.meal_selection import MealSelection
from .models.payment import Payment
from .models.luggage import Luggage
from .models.review import Review
from .models.employee_action import EmployeeAction

admin.site.register(Route)
admin.site.register(Flight)
admin.site.register(TravelClass)
admin.site.register(Price)
admin.site.register(Passenger)
admin.site.register(Booking)
admin.site.register(PickupDropService)
admin.site.register(MealOption)
admin.site.register(MealSelection)
admin.site.register(Payment)
admin.site.register(Luggage)
admin.site.register(Review)
admin.site.register(EmployeeAction)
