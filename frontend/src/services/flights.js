import api from './api';

// Existing exports...
export const getRoutes = () => api.get('/routes/');
export const getFlights = () => api.get('/flights/');
export const getFlight = id => api.get(`/flights/${id}/`);
export const getPrices = flightId => api.get('/prices/', { params: { flight: flightId } });
export const getMealOptions = () => api.get('/meal-options/');
export const createPassenger = data => api.post('/passengers/', data);
export const createBooking = data => api.post('/bookings/', data);
export const createMealSelection = data => api.post('/meal-selections/', data);
export const createPickupDrop = data => api.post('/pickup-drop-services/', data);
export const createPayment = data => api.post('/payments/', data);

// New helper to fetch a single booking
export const getBooking = id => api.get(`/bookings/${id}/`);