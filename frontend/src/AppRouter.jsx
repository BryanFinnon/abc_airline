// File: frontend/src/AppRouter.jsx

import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

import ListFlights    from './pages/ListFlights';
import BookingForm    from './pages/BookingForm';
import PaymentPage    from './pages/PaymentPage';
import UserBookings   from './pages/UserBookings';
import AdminDashboard from './pages/AdminDashboard';

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        {/* redirige l'accueil */}
        <Route path="/" element={<Navigate to="/flights" replace />} />

        {/* tes routes principales */}
        <Route path="/flights"                element={<ListFlights />} />
        <Route path="/book/:flightId"         element={<BookingForm />} />
        <Route path="/payment/:bookingId"     element={<PaymentPage />} />
        <Route path="/bookings"               element={<UserBookings />} />
        <Route path="/admin"                  element={<AdminDashboard />} />

        {/* fallback : toute autre URL */}
        <Route
          path="*"
          element={
            <div style={{ padding: 20, color: 'red' }}>
              ❌ Aucune route ne correspond à « {window.location.pathname} »
            </div>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
