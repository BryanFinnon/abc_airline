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
  const navigate     = useNavigate();

  const [flight, setFlight]           = useState(null);
  const [prices, setPrices]           = useState([]);
  const [mealOptions, setMealOptions] = useState([]);
  const [selectedClass, setSelectedClass] = useState(null);
  const [passenger, setPassenger] = useState({
    first_name: '',
    last_name: '',
    email: '',
    passport_number: '',
    phone: ''
  });
  const [meals, setMeals]         = useState([]);  // { optionId, quantity }
  const [pickup, setPickup]       = useState(false);
  const [dropoff, setDropoff]     = useState(false);
  const [pickupAddress, setPickupAddress] = useState('');
  const [dropAddress, setDropAddress]     = useState('');
  const [total, setTotal]         = useState(0);

  // Fetch flight, prices, meals with error handling and logging
  useEffect(() => {
    getFlight(flightId)
      .then(res => setFlight(res.data))
      .catch(err => console.error('Erreur getFlight:', err));

    getPrices(flightId)
      .then(res => {
        console.log('Prices pour le vol', flightId, res.data);
        setPrices(res.data);
      })
      .catch(err => console.error('Erreur getPrices:', err));

    getMealOptions()
      .then(res => setMealOptions(res.data))
      .catch(err => console.error('Erreur getMealOptions:', err));
  }, [flightId]);

  // Recalculate total whenever selections change
  useEffect(() => {
    let sum = 0;
    if (selectedClass) {
      const priceObj = prices.find(p => p.travel_class.id === selectedClass);
      sum += priceObj ? parseFloat(priceObj.amount) : 0;
    }
    meals.forEach(m => {
      const opt = mealOptions.find(o => o.id === m.optionId);
      if (opt) sum += parseFloat(opt.price) * m.quantity;
    });
    if (pickup) sum += 20;
    if (dropoff) sum += 20;
    setTotal(sum);
  }, [selectedClass, meals, pickup, dropoff, prices, mealOptions]);

  const handleMealChange = (optionId, qty) => {
    setMeals(prev => {
      const other = prev.filter(m => m.optionId !== optionId);
      return [...other, { optionId, quantity: qty }];
    });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const { data: p } = await createPassenger(passenger);
      const bookingData = {
        passenger_id: p.id,
        flight_id: flightId,
        travel_class_id: selectedClass,
        total_price: total
      };
      const { data: b } = await createBooking(bookingData);
      await Promise.all(
        meals.filter(m => m.quantity > 0).map(m =>
          createMealSelection({
            booking_id: b.id,
            meal_option_id: m.optionId,
            quantity: m.quantity
          })
        )
      );
      if (pickup) {
        await createPickupDrop({
          booking_id: b.id,
          service_type: 'PICKUP',
          address: pickupAddress,
          cost: 20
        });
      }
      if (dropoff) {
        await createPickupDrop({
          booking_id: b.id,
          service_type: 'DROPOFF',
          address: dropAddress,
          cost: 20
        });
      }
      navigate(`/payment/${b.id}`);
    } catch (err) {
      console.error('Erreur lors de la réservation:', err);
    }
  };

  if (!flight) return <p>Chargement du vol...</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">
        Réserver : {flight.route.departure} → {flight.route.arrival}
      </h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        {/* Choix de la classe */}
        <div>
          <label className="block font-semibold">Classe :</label>
          <select
            required
            className="border rounded p-2 w-full"
            value={selectedClass || ''}
            onChange={e => setSelectedClass(Number(e.target.value))}
          >
            <option value="" disabled>
              Sélectionnez
            </option>
            {prices.map(p => (
              <option key={p.id} value={p.travel_class.id}>
                {p.travel_class.name} (€{p.amount})
              </option>
            ))}
          </select>
        </div>

        {/* Infos passager */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input
            required
            placeholder="Prénom"
            className="border rounded p-2"
            value={passenger.first_name}
            onChange={e =>
              setPassenger({ ...passenger, first_name: e.target.value })
            }
          />
          <input
            required
            placeholder="Nom"
            className="border rounded p-2"
            value={passenger.last_name}
            onChange={e =>
              setPassenger({ ...passenger, last_name: e.target.value })
            }
          />
          <input
            required
            type="email"
            placeholder="Email"
            className="border rounded p-2"
            value={passenger.email}
            onChange={e =>
              setPassenger({ ...passenger, email: e.target.value })
            }
          />
          <input
            required
            placeholder="Passeport"
            className="border rounded p-2"
            value={passenger.passport_number}
            onChange={e =>
              setPassenger({ ...passenger, passport_number: e.target.value })
            }
          />
          <input
            required
            placeholder="Téléphone"
            className="border rounded p-2"
            value={passenger.phone}
            onChange={e =>
              setPassenger({ ...passenger, phone: e.target.value })
            }
          />
        </div>

        {/* Options repas */}
        <div>
          <label className="block font-semibold mb-2">
            Repas supplémentaires :
          </label>
          {mealOptions.map(opt => (
            <div key={opt.id} className="flex items-center mb-1">
              <span className="mr-2">
                {opt.name} (€{opt.price})
              </span>
              <input
                type="number"
                min="0"
                defaultValue="0"
                className="border rounded p-1 w-16"
                onChange={e => handleMealChange(opt.id, Number(e.target.value))}
              />
            </div>
          ))}
        </div>

        {/* Pickup / Dropoff */}
        <div className="space-y-2">
          <div className="flex items-center">
            <input
              type="checkbox"
              id="pickup"
              checked={pickup}
              onChange={e => setPickup(e.target.checked)}
            />
            <label htmlFor="pickup" className="ml-2">
              Pickup depuis l’adresse
            </label>
          </div>
          {pickup && (
            <input
              required
              placeholder="Adresse de pickup"
              className="border rounded p-2 w-full"
              value={pickupAddress}
              onChange={e => setPickupAddress(e.target.value)}
            />
          )}

          <div className="flex items-center">
            <input
              type="checkbox"
              id="dropoff"
              checked={dropoff}
              onChange={e => setDropoff(e.target.checked)}
            />
            <label htmlFor="dropoff" className="ml-2">
              Dropoff à l’adresse
            </label>
          </div>
          {dropoff && (
            <input
              required
              placeholder="Adresse de dropoff"
              className="border rounded p-2 w-full"
              value={dropAddress}
              onChange={e => setDropAddress(e.target.value)}
            />
          )}
        </div>

        {/* Total & Submit */}
        <div className="flex items-center justify-between">
          <span className="font-bold">Total : €{total.toFixed(2)}</span>
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Confirmer la réservation
          </button>
        </div>
      </form>
    </div>
  );
}
