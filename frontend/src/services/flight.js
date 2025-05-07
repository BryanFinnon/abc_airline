import api from './api';

export const getFlights = () => api.get('/flights/');
export const createBooking = data => api.post('/bookings/', data);
// …
