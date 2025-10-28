/**
 * Test 4: React with TypeScript
 * Tests: React components, hooks, props, state, JSX
 */

import React, { useState, useEffect, useCallback } from "react";

/**
 * Props for the Button component
 */
interface ButtonProps {
  /** The button's click handler */
  onClick: () => void;
  /** Whether the button is disabled */
  disabled?: boolean;
  /** CSS class name */
  className?: string;
  /** Button text content */
  children: React.ReactNode;
}

/**
 * Reusable button component
 * @param props - The button properties
 */
const CustomButton: React.FC<ButtonProps> = ({ onClick, disabled = false, className = "", children }) => {
  return (
    <button onClick={onClick} disabled={disabled} className={`btn ${className}`}>
      {children}
    </button>
  );
};

/**
 * Props for the Counter component
 */
interface CounterProps {
  /** Initial counter value */
  initialValue?: number;
  /** Callback when counter changes */
  onCounterChange?: (value: number) => void;
}

/**
 * Counter component that tracks clicks
 */
const Counter: React.FC<CounterProps> = ({ initialValue = 0, onCounterChange }) => {
  const [count, setCount] = useState<number>(initialValue);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  /**
   * Handles incrementing the counter
   */
  const handleIncrement = useCallback(() => {
    setCount((prevCount) => {
      const newValue = prevCount + 1;
      onCounterChange?.(newValue);
      return newValue;
    });
  }, [onCounterChange]);

  /**
   * Handles decrementing the counter
   */
  const handleDecrement = useCallback(() => {
    setCount((prevCount) => {
      const newValue = prevCount - 1;
      onCounterChange?.(newValue);
      return newValue;
    });
  }, [onCounterChange]);

  /**
   * Resets the counter to initial value
   */
  const handleReset = useCallback(() => {
    setCount(initialValue);
    onCounterChange?.(initialValue);
  }, [initialValue, onCounterChange]);

  /**
   * Simulates an async operation
   */
  const handleAsync = useCallback(async () => {
    setIsLoading(true);
    try {
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 1000));
      setCount((prevCount) => prevCount + 10);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    console.log(`Counter value changed to: ${count}`);
  }, [count]);

  return (
    <div className="counter-container">
      <h2>Counter App</h2>
      <div className="counter-display">
        <p>Current Count: {count}</p>
      </div>

      <div className="counter-controls">
        <CustomButton onClick={handleDecrement} disabled={isLoading}>
          Decrement
        </CustomButton>

        <CustomButton onClick={handleReset} disabled={isLoading} className="reset-btn">
          Reset
        </CustomButton>

        <CustomButton onClick={handleIncrement} disabled={isLoading}>
          Increment
        </CustomButton>

        <CustomButton onClick={handleAsync} disabled={isLoading}>
          {isLoading ? "Loading..." : "Add 10"}
        </CustomButton>
      </div>
    </div>
  );
};

/**
 * Props for the App component
 */
interface AppProps {
  /** Application title */
  title?: string;
}

/**
 * Main application component
 */
const App: React.FC<AppProps> = ({ title = "TypeScript React App" }) => {
  const [totalClicks, setTotalClicks] = useState<number>(0);

  /**
   * Handles counter changes
   */
  const handleCounterChange = useCallback((value: number) => {
    setTotalClicks((prevTotal) => prevTotal + 1);
  }, []);

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>{title}</h1>
        <p className="subtitle">Testing TypeScript and React integration</p>
      </header>

      <main className="app-main">
        <Counter initialValue={0} onCounterChange={handleCounterChange} />

        <section className="stats">
          <h3>Statistics</h3>
          <p>Total Interactions: {totalClicks}</p>
        </section>
      </main>

      <footer className="app-footer">
        <p>&copy; 2024 TypeScript React Test Suite</p>
      </footer>
    </div>
  );
};

/**
 * Default export of the App component
 */
export default App;
