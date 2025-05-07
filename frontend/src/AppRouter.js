import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ListFlights from './pages/ListFlights';
import BookingForm from './pages/BookingForm';
// …

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ListFlights />} />
        <Route path="/book/:flightId" element={<BookingForm />} />
        {/* … autres routes … */}
      </Routes>
    </BrowserRouter>
  );
}
