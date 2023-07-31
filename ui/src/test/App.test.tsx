/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-unsafe-call */
import { render, screen } from '@testing-library/react';
import App from '../App';

const setup = () => {
    render(<App />);
};

describe('Component GiftExpertApp UI Testing', () => {
    test('Verify component is rendered', () => {
      setup();
      const headerElement = screen.getByText('Vite + React');
      expect(headerElement).toBeInTheDocument();
    });
});
