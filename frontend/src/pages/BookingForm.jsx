// File: frontend/src/pages/BookingForm.jsx
import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  getFlight,
  getPrices,
  getMealOptions,
  createPassenger,
  createBooking,
  createMealSelection,
  createPickupDrop
} from '../services/flights';

export default function BookingForm() {
  const { flightId } = useParams();
  const navigate = useNavigate();

  const [flight, setFlight] = useState(null);
  const [prices, setPrices] = useState([]);
  const [mealOptions, setMealOptions] = useState([]);
  const [selectedClass, setSelectedClass] = useState('');
  const [passenger, setPassenger] = useState({
    first_name: '',
    last_name: '',
    email: '',
    passport_number: '',
    phone: ''
  });
  const [meals, setMeals] = useState([]);  // array of selected meal IDs
  const [pickup, setPickup] = useState(false);
  const [dropoff, setDropoff] = useState(false);
  const [pickupAddress, setPickupAddress] = useState('');
  const [dropAddress, setDropAddress] = useState('');
  const [total, setTotal] = useState(0);
  const [error, setError] = useState(null);

  useEffect(() => {
    getFlight(flightId)
      .then(res => setFlight(res.data))
      .catch(err => console.error('Erreur getFlight:', err));
    getPrices(flightId)
      .then(res => setPrices(res.data))
      .catch(err => console.error('Erreur getPrices:', err));
    getMealOptions()
      .then(res => setMealOptions(res.data))
      .catch(err => console.error('Erreur getMealOptions:', err));
  }, [flightId]);

  useEffect(() => {
    let sum = 0;
    if (selectedClass) {
      const priceObj = prices.find(p => p.travel_class.id === Number(selectedClass));
      if (priceObj) sum += parseFloat(priceObj.amount);
    }
    meals.forEach(id => {
      const opt = mealOptions.find(o => o.id === id);
      if (opt) sum += parseFloat(opt.price);
    });
    if (pickup) sum += 20;
    if (dropoff) sum += 20;
    setTotal(sum);
  }, [selectedClass, meals, pickup, dropoff, prices, mealOptions]);

  const toggleMeal = id => {
    setMeals(prev =>
      prev.includes(id) ? prev.filter(m => m !== id) : [...prev, id]
    );
    setError(null);
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setError(null);
    if (!selectedClass) {
      setError('Please select a class.');
      return;
    }
    if (pickup && !pickupAddress.toLowerCase().includes(flight.route.departure.toLowerCase())) {
      setError(`Pick-up only since ${flight.route.departure}.`);
      return;
    }
    if (dropoff && !dropAddress.toLowerCase().includes(flight.route.arrival.toLowerCase())) {
      setError(`Drop-off only at ${flight.route.arrival}.`);
      return;
    }
    try {
      const { data: p } = await createPassenger(passenger);
      const { data: b } = await createBooking({
        passenger_id: p.id,
        flight_id: flightId,
        travel_class_id: Number(selectedClass),
        total_price: total
      });
      await Promise.all(
        meals.map(id => createMealSelection({ booking_id: b.id, meal_option_id: id, quantity: 1 }))
      );
      if (pickup) {
        await createPickupDrop({ booking_id: b.id, service_type: 'PICKUP', address: pickupAddress, cost: 20 });
      }
      if (dropoff) {
        await createPickupDrop({ booking_id: b.id, service_type: 'DROPOFF', address: dropAddress, cost: 20 });
      }
      navigate(`/payment/${b.id}`);
    } catch (err) {
      console.error(err);
      setError('Erreur lors de la réservation.');
    }
  };

  if (!flight) return <p>Loading the flight...</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-2">Book now : {flight.route.departure} → {flight.route.arrival}</h1>
      <p className="mb-4">Date :{flight.date} | {flight.departure_time} - {flight.arrival_time}</p>
      {error && <div className="text-red-600 mb-4">{error}</div>}
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block font-semibold">Class :</label>
          <select
            value={selectedClass}
            onChange={e => { setSelectedClass(e.target.value); setError(null); }}
            className="border rounded p-2 w-full"
          >
            <option value="" disabled>Select a class</option>
            {prices.map(p => (
              <option key={p.id} value={p.travel_class.id}>
                {p.travel_class.name} (£{p.amount})
              </option>
            ))}
          </select>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input required placeholder="First name" className="border rounded p-2" value={passenger.first_name} onChange={e => setPassenger({ ...passenger, first_name: e.target.value })} />
          <input required placeholder="Last name" className="border rounded p-2" value={passenger.last_name} onChange={e => setPassenger({ ...passenger, last_name: e.target.value })} />
          <input required type="Email" placeholder="Email" className="border rounded p-2" value={passenger.email} onChange={e => setPassenger({ ...passenger, email: e.target.value })} />
          <input required placeholder="Passeport" className="border rounded p-2" value={passenger.passport_number} onChange={e => setPassenger({ ...passenger, passport_number: e.target.value })} />
          <input required placeholder="Phone number" className="border rounded p-2" value={passenger.phone} onChange={e => setPassenger({ ...passenger, phone: e.target.value })} />
        </div>
        <details className="border rounded p-2">
          <summary className="cursor-pointer font-semibold">Meals & drinks</summary>
          <div className="mt-2 space-y-1">
            {mealOptions.map(opt => (
              <label key={opt.id} className="flex items-center">
                <input type="checkbox" className="mr-2" checked={meals.includes(opt.id)} onChange={() => toggleMeal(opt.id)} />
                {opt.name} (£{opt.price})
              </label>
            ))}
          </div>
        </details>
        <div className="space-y-2">
          <div className="flex items-center">
            <input type="checkbox" id="pickup" checked={pickup} onChange={e => { setPickup(e.target.checked); setError(null); }} />
            <label htmlFor="pickup" className="ml-2">Pickup</label>
          </div>
          {pickup && <input required placeholder="Pickup address" className="border rounded p-2 w-full" value={pickupAddress} onChange={e => setPickupAddress(e.target.value)} />}
          <div className="flex items-center">
            <input type="checkbox" id="dropoff" checked={dropoff} onChange={e => { setDropoff(e.target.checked); setError(null); }} />
            <label htmlFor="dropoff" className="ml-2">Drop-off</label>
          </div>
          {dropoff && <input required placeholder="Drop-off address" className="border rounded p-2 w-full" value={dropAddress} onChange={e => setDropAddress(e.target.value)} />}
        </div>
        <div className="flex items-center justify-between">
          <span className="font-bold">Total : £{total.toFixed(2)}</span>
          <button 
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Next → Payment
          </button>

        </div>
      </form>
    </div>
  );
}

// Helper function outside component
function toggleMeal(id) {
  // This function should be defined inside component, binding setMeals
}
