/**
 * Test 2: Classes, Interfaces, and OOP Concepts
 * Tests: Class declarations, inheritance, interfaces, access modifiers
 */

// Define the shape of a product
interface Product {
  /** Product unique identifier */
  id: number;
  /** Product name displayed to users */
  name: string;
  /** Current product price */
  price: number;
  /** Number of items in stock */
  quantity: number;
}

/**
 * Base class for store operations
 * Handles common store functionality
 */
abstract class Store {
  /** Name of the store */
  protected storeName: string;

  constructor(name: string) {
    this.storeName = name;
  }

  /**
   * Gets the store name
   */
  public getStoreName(): string {
    return this.storeName;
  }

  /**
   * Abstract method to be implemented by subclasses
   */
  abstract processOrder(productId: number, quantity: number): void;
}

/**
 * Electronics store implementation
 * Specializes in selling electronics
 */
export class ElectronicsStore extends Store {
  /** Collection of available products */
  private products: Product[] = [];

  /**
   * Adds a product to the store
   */
  public addProduct(product: Product): void {
    this.products.push(product);
  }

  /**
   * Retrieves a product by ID
   */
  public getProduct(productId: number): Product | undefined {
    return this.products.find((p) => p.id === productId);
  }

  /**
   * Processes an order for a product
   */
  public processOrder(productId: number, quantity: number): void {
    const product = this.getProduct(productId);

    if (!product) {
      console.log("Product not found");
      return;
    }

    if (product.quantity < quantity) {
      console.log("Insufficient stock");
      return;
    }

    // Reduce inventory
    product.quantity -= quantity;
    const totalPrice = product.price * quantity;

    console.log(`Order processed: ${quantity} x ${product.name} = $${totalPrice}`);
  }

  /**
   * Gets current inventory value
   */
  private calculateInventoryValue(): number {
    return this.products.reduce((total, product) => {
      return total + product.price * product.quantity;
    }, 0);
  }

  /**
   * Reports store status
   */
  public reportStatus(): void {
    console.log(`Store: ${this.storeName}`);
    console.log(`Products: ${this.products.length}`);
    console.log(`Inventory Value: $${this.calculateInventoryValue()}`);
  }
}

// Test the store
const store = new ElectronicsStore("TechMart");

store.addProduct({ id: 1, name: "Laptop", price: 999.99, quantity: 5 });
store.addProduct({ id: 2, name: "Mouse", price: 29.99, quantity: 50 });
store.addProduct({ id: 3, name: "Keyboard", price: 79.99, quantity: 30 });

store.reportStatus();
store.processOrder(1, 2);
store.processOrder(2, 10);
store.reportStatus();
