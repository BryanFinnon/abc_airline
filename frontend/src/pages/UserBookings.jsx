import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getBookings, cancelBooking } from '../services/flights';

export default function UserBookings() {
  const [bookings, setBookings] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetchBookings();
  }, []);

  const fetchBookings = () => {
    getBookings()
      .then(res => setBookings(res.data))
      .catch(err => console.error('Erreur getBookings:', err));
  };

  const handleCancel = async id => {
    try {
      await cancelBooking(id);
      fetchBookings();
    } catch (err) {
      console.error('Erreur annulation:', err);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Mes Réservations</h1>
      {bookings.length === 0 ? (
        <p>Vous n'avez aucune réservation.</p>
      ) : (
        <ul className="space-y-4">
          {bookings.map(b => (
            <li key={b.id} className="border rounded p-4 shadow-sm">
              <p><strong>Vol :</strong> {b.flight.route.departure} → {b.flight.route.arrival} le {b.flight.date}</p>
              <p><strong>Classe :</strong> {b.travel_class.name}</p>
              <p><strong>Statut :</strong> {b.status}</p>
              <p><strong>Prix total :</strong> €{b.total_price}</p>
              {b.status === 'CONFIRMED' && (
                <button
                  className="mt-2 bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700"
                  onClick={() => handleCancel(b.id)}
                >
                  Annuler
                </button>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
