import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getBooking, createPayment } from '../services/flights';

export default function PaymentPage() {
  const { bookingId } = useParams();
  const navigate = useNavigate();
  const [booking, setBooking] = useState(null);
  const [cardNumber, setCardNumber] = useState('');

  useEffect(() => {
    getBooking(bookingId)
      .then(res => setBooking(res.data))
      .catch(err => console.error('Erreur getBooking:', err));
  }, [bookingId]);

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await createPayment({
        booking_id: booking.id,
        card_number: cardNumber,
        amount: booking.total_price
      });
      navigate('/bookings');
    } catch (err) {
      console.error('Erreur de paiement:', err);
    }
  };

  if (!booking) return <p>Chargement de la réservation...</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Paiement</h1>
      <p>Montant à payer : €{booking.total_price.toFixed(2)}</p>
      <form onSubmit={handleSubmit} className="mt-4">
        <div className="mb-4">
          <label className="block font-semibold">Numéro de carte</label>
          <input
            type="text"
            required
            className="border rounded p-2 w-full"
            value={cardNumber}
            onChange={e => setCardNumber(e.target.value)}
          />
        </div>
        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Payer
        </button>
      </form>
    </div>
  );
}
