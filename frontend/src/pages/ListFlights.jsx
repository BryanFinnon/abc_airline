// File: frontend/src/pages/ListFlights.jsx

import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getFlights } from '../services/flights';

export default function ListFlights() {
  const [flights, setFlights] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    getFlights()
      .then(res => setFlights(res.data))
      .catch(err => console.error('Failed to fetch flights:', err));
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">List of available flights</h1>
      {flights.length === 0 ? (
        <p>No flights available at the moment.</p>
      ) : (
        <ul className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {flights.map(flight => (
            <li key={flight.id} className="border rounded-lg p-4 shadow-sm">
              <h2 className="text-xl font-semibold">
                {flight.route.departure} → {flight.route.arrival}
              </h2>
              <p>Date : {flight.date}</p>
              <p>
                Departure : {flight.departure_time} – Arrival : {flight.arrival_time}
              </p>
              <button
                className="mt-2 px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700"
                onClick={() => navigate(`/book/${flight.id}`)}
              >
                Book
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
