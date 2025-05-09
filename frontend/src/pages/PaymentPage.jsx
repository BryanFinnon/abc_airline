import React from 'react';
import { useParams } from 'react-router-dom';

export default function PaymentPage() {
  const { bookingId } = useParams();
  return (
    <div style={{ padding: 20 }}>
      <h1>💳 PaymentPage</h1>
      <p>bookingId = {bookingId}</p>
      <p>Si tu vois ce message, la route fonctionne.</p>
    </div>
  );
}
