// File: frontend/src/index.js

import React from 'react';
import { createRoot } from 'react-dom/client';   // <-- notez le nouvel import
import './index.css';
import App from './App';

const container = document.getElementById('root');
const root = createRoot(container);               // <-- on crée le root
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
