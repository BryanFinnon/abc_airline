from rest_framework.routers import DefaultRouter
from .views.route_viewset import RouteViewSet
from .views.flight_viewset import FlightViewSet
from .views.travel_class_viewset import TravelClassViewSet
from .views.price_viewset import PriceViewSet
from .views.passenger_viewset import PassengerViewSet
from .views.booking_viewset import BookingViewSet
from .views.pickup_drop_service_viewset import PickupDropServiceViewSet
from .views.meal_option_viewset import MealOptionViewSet
from .views.meal_selection_viewset import MealSelectionViewSet
from .views.payment_viewset import PaymentViewSet
from .views.luggage_viewset import LuggageViewSet
from .views.review_viewset import ReviewViewSet
from .views.employee_action_viewset import EmployeeActionViewSet
from flights.views.booking_viewset import BookingViewSet


router = DefaultRouter()
router.register(r'routes', RouteViewSet, basename='route')
router.register(r'flights', FlightViewSet, basename='flight')
router.register(r'travel-classes', TravelClassViewSet, basename='travelclass')
router.register(r'prices', PriceViewSet, basename='price')
router.register(r'passengers', PassengerViewSet, basename='passenger')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'pickup-drop-services', PickupDropServiceViewSet, basename='pickupdrop')
router.register(r'meal-options', MealOptionViewSet, basename='mealoption')
router.register(r'meal-selections', MealSelectionViewSet, basename='mealselection')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'luggages', LuggageViewSet, basename='luggage')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'employee-actions', EmployeeActionViewSet, basename='employeeaction')

urlpatterns = router.urls





