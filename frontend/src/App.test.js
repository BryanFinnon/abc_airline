import { render, screen } from '@testing-library/react';
import App from './App';

jest.mock('./AppRouter', () => function MockRouter() {
  return <main>ABC Airline application</main>;
});

test('renders the application router', () => {
  render(<App />);
  expect(screen.getByText('ABC Airline application')).toBeInTheDocument();
});
