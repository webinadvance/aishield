/**
 * Test 3: Async/Await, Promises, and Generics
 * Tests: async functions, promises, generics, error handling
 */

/**
 * Generic API response wrapper
 * Used for all API responses
 */
interface ApiResponse<T> {
  /** Whether the request was successful */
  success: boolean;
  /** The response data */
  data: T;
  /** Error message if request failed */
  error?: string;
}

/**
 * User data structure
 */
interface UserData {
  /** Unique user identifier */
  userId: number;
  /** User's email address */
  email: string;
  /** User's full name */
  fullName: string;
  /** Last login timestamp */
  lastLogin: Date;
}

/**
 * Generic API client for making requests
 */
class ApiClient<T> {
  /** Base URL for API endpoints */
  private baseUrl: string;

  /**
   * Creates a new API client
   * @param url - The base URL for the API
   */
  constructor(url: string) {
    this.baseUrl = url;
  }

  /**
   * Fetches data from an endpoint
   * @param endpoint - The API endpoint to call
   * @returns Promise with the response data
   */
  public async fetchData(endpoint: string): Promise<ApiResponse<T>> {
    try {
      // Simulate API call
      console.log(`Fetching from: ${this.baseUrl}${endpoint}`);

      // Simulate delay
      await this.delay(500);

      // Simulate successful response
      return {
        success: true,
        data: this.mockData() as T,
      };
    } catch (error) {
      return {
        success: false,
        data: {} as T,
        error: error instanceof Error ? error.message : "Unknown error",
      };
    }
  }

  /**
   * Posts data to an endpoint
   * @param endpoint - The API endpoint
   * @param payload - The data to send
   */
  public async postData(endpoint: string, payload: T): Promise<ApiResponse<T>> {
    try {
      console.log(`Posting to: ${this.baseUrl}${endpoint}`);
      console.log(`Payload:`, payload);

      await this.delay(500);

      return {
        success: true,
        data: payload,
      };
    } catch (error) {
      return {
        success: false,
        data: {} as T,
        error: error instanceof Error ? error.message : "Unknown error",
      };
    }
  }

  /**
   * Delays execution for a specified time
   * @param milliseconds - How long to wait
   */
  private delay(milliseconds: number): Promise<void> {
    return new Promise((resolve) => {
      setTimeout(resolve, milliseconds);
    });
  }

  /**
   * Generates mock data
   */
  private mockData(): T {
    return {} as T;
  }
}

/**
 * User service for managing users
 */
class UserService {
  /** API client for user endpoints */
  private apiClient: ApiClient<UserData>;

  /**
   * Creates a new user service
   */
  constructor() {
    this.apiClient = new ApiClient<UserData>("https://api.example.com");
  }

  /**
   * Retrieves user data by ID
   * @param userId - The user's ID
   */
  public async getUserById(userId: number): Promise<UserData | null> {
    const response = await this.apiClient.fetchData(`/users/${userId}`);

    if (response.success && response.data) {
      return response.data;
    }

    console.error("Failed to fetch user:", response.error);
    return null;
  }

  /**
   * Updates user information
   * @param user - The user data to update
   */
  public async updateUser(user: UserData): Promise<boolean> {
    const response = await this.apiClient.postData("/users/update", user);
    return response.success;
  }

  /**
   * Processes multiple user requests concurrently
   */
  public async processMultipleUsers(userIds: number[]): Promise<(UserData | null)[]> {
    const promises = userIds.map((id) => this.getUserById(id));
    return Promise.all(promises);
  }
}

// Test async operations
async function runAsyncTests() {
  const userService = new UserService();

  console.log("=== Testing Async Operations ===");
  const user = await userService.getUserById(1);
  console.log("User retrieved:", user ? "Success" : "Failed");

  const updateSuccess = await userService.updateUser({
    userId: 1,
    email: "user@example.com",
    fullName: "John Doe",
    lastLogin: new Date(),
  });
  console.log("User updated:", updateSuccess ? "Success" : "Failed");

  console.log("\n=== Testing Concurrent Operations ===");
  const users = await userService.processMultipleUsers([1, 2, 3]);
  console.log(`Processed ${users.length} users`);
}

// Execute tests
runAsyncTests().catch(console.error);
