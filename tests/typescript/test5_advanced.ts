/**
 * Test 5: Advanced TypeScript Features
 * Tests: Generics, utility types, conditional types, mapped types, enums, decorators
 */

/**
 * Enumeration for HTTP methods
 */
enum HttpMethod {
  GET = "GET",
  POST = "POST",
  PUT = "PUT",
  DELETE = "DELETE",
  PATCH = "PATCH",
}

/**
 * Enumeration for request status
 */
enum RequestStatus {
  Pending = "PENDING",
  Success = "SUCCESS",
  Error = "ERROR",
  Cancelled = "CANCELLED",
}

/**
 * Generic type for paginated results
 */
type PaginatedResult<T> = {
  /** Array of items in this page */
  items: T[];
  /** Current page number */
  pageNumber: number;
  /** Total number of pages */
  totalPages: number;
  /** Total item count */
  totalItems: number;
};

/**
 * Generic type for API requests
 */
interface ApiRequest<T = any> {
  /** The HTTP method to use */
  method: HttpMethod;
  /** The request URL */
  url: string;
  /** Request body data */
  body?: T;
  /** Request headers */
  headers?: Record<string, string>;
  /** Request timeout in milliseconds */
  timeout?: number;
}

/**
 * Generic type for API responses
 */
interface ApiResponseData<T> {
  /** The response data */
  data: T;
  /** HTTP status code */
  statusCode: number;
  /** Response headers */
  headers: Record<string, string>;
  /** Request status */
  status: RequestStatus;
}

/**
 * Utility type: Readonly version of a type
 */
type ReadonlyApiResponse<T> = Readonly<ApiResponseData<T>>;

/**
 * Utility type: Makes all properties optional
 */
type Partial<T> = {
  [P in keyof T]?: T[P];
};

/**
 * Utility type: Extract keys of a certain type
 */
type KeysOfType<T, U> = {
  [K in keyof T]: T[K] extends U ? K : never;
}[keyof T];

/**
 * Advanced generic constraint
 */
type WithId<T> = T & {
  /** Unique identifier */
  id: string;
};

/**
 * Conditional type example
 */
type IsArray<T> = T extends Array<infer U> ? U : T;

/**
 * User record type
 */
interface User {
  /** User ID */
  id: number;
  /** Username */
  username: string;
  /** User email */
  email: string;
  /** Is user active */
  isActive: boolean;
  /** User creation date */
  createdAt: Date;
}

/**
 * Product record type
 */
interface Product {
  /** Product ID */
  id: number;
  /** Product name */
  name: string;
  /** Product price */
  price: number;
  /** Stock quantity */
  stock: number;
}

/**
 * Generic repository pattern
 */
class Repository<T extends { id: number | string }> {
  /** Stored items */
  private items: T[] = [];
  /** Next ID counter */
  private nextId: number = 1;

  /**
   * Creates a new repository
   */
  constructor() {
    console.log("Repository initialized");
  }

  /**
   * Adds an item to the repository
   * @param item - The item to add
   */
  public create(item: Omit<T, "id">): T {
    const newItem = {
      ...item,
      id: this.nextId++,
    } as T;

    this.items.push(newItem);
    return newItem;
  }

  /**
   * Retrieves an item by ID
   * @param id - The item ID
   */
  public read(id: number | string): T | undefined {
    return this.items.find((item) => item.id === id);
  }

  /**
   * Updates an item
   * @param id - The item ID
   * @param updates - Partial updates to apply
   */
  public update(id: number | string, updates: Partial<T>): T | undefined {
    const index = this.items.findIndex((item) => item.id === id);

    if (index === -1) {
      return undefined;
    }

    this.items[index] = { ...this.items[index], ...updates };
    return this.items[index];
  }

  /**
   * Deletes an item
   * @param id - The item ID
   */
  public delete(id: number | string): boolean {
    const index = this.items.findIndex((item) => item.id === id);

    if (index === -1) {
      return false;
    }

    this.items.splice(index, 1);
    return true;
  }

  /**
   * Retrieves all items
   */
  public getAll(): T[] {
    return [...this.items];
  }

  /**
   * Gets paginated results
   * @param pageNumber - Page number
   * @param pageSize - Items per page
   */
  public getPaginated(pageNumber: number, pageSize: number): PaginatedResult<T> {
    const startIndex = (pageNumber - 1) * pageSize;
    const endIndex = startIndex + pageSize;
    const items = this.items.slice(startIndex, endIndex);
    const totalPages = Math.ceil(this.items.length / pageSize);

    return {
      items,
      pageNumber,
      totalPages,
      totalItems: this.items.length,
    };
  }
}

/**
 * User repository
 */
class UserRepository extends Repository<User> {
  /**
   * Finds users by username
   */
  public findByUsername(username: string): User | undefined {
    return this.getAll().find((user) => user.username === username);
  }

  /**
   * Finds active users
   */
  public findActiveUsers(): User[] {
    return this.getAll().filter((user) => user.isActive);
  }
}

/**
 * Product repository
 */
class ProductRepository extends Repository<Product> {
  /**
   * Finds products in stock
   */
  public findInStock(): Product[] {
    return this.getAll().filter((product) => product.stock > 0);
  }

  /**
   * Finds products within price range
   */
  public findByPriceRange(minPrice: number, maxPrice: number): Product[] {
    return this.getAll().filter((product) => product.price >= minPrice && product.price <= maxPrice);
  }
}

// Test the repositories
const userRepo = new UserRepository();
const productRepo = new ProductRepository();

// Add users
const user1 = userRepo.create({
  username: "alice",
  email: "alice@example.com",
  isActive: true,
  createdAt: new Date(),
});

const user2 = userRepo.create({
  username: "bob",
  email: "bob@example.com",
  isActive: false,
  createdAt: new Date(),
});

console.log("Users created:", userRepo.getAll().length);

// Add products
const product1 = productRepo.create({
  name: "Laptop",
  price: 999.99,
  stock: 10,
});

const product2 = productRepo.create({
  name: "Mouse",
  price: 29.99,
  stock: 100,
});

console.log("Products created:", productRepo.getAll().length);

// Test queries
console.log("Active users:", userRepo.findActiveUsers().length);
console.log("Products in stock:", productRepo.findInStock().length);
console.log("Products under $50:", productRepo.findByPriceRange(0, 50).length);

// Test pagination
const userPage1 = userRepo.getPaginated(1, 10);
console.log(`Users: Page ${userPage1.pageNumber} of ${userPage1.totalPages} (${userPage1.totalItems} total)`);

// Test updates
userRepo.update(user1.id, { isActive: false });
console.log("Updated user1 active status");

// Test deletion
const deleted = productRepo.delete(product2.id);
console.log("Product deleted:", deleted);
console.log("Remaining products:", productRepo.getAll().length);
