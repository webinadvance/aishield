/**
 * Test 1: Basic TypeScript Functions and Variables
 * Tests: Function declarations, variables, type annotations, basic comments
 */

// User authentication service
const userDatabase: Map<string, string> = new Map();

/**
 * Registers a new user in the system
 * @param username - The user's login name
 * @param password - The user's secret password
 * @returns boolean indicating success
 */
function registerUser(username: string, password: string): boolean {
  if (userDatabase.has(username)) {
    return false;
  }

  userDatabase.set(username, password);
  return true;
}

/**
 * Validates user credentials
 * @param username - The username to check
 * @param password - The password to verify
 */
function validateCredentials(username: string, password: string): boolean {
  const storedPassword = userDatabase.get(username);
  return storedPassword === password;
}

// Test execution
const isRegistered = registerUser("alice", "secretPassword123");
const isValid = validateCredentials("alice", "secretPassword123");

console.log("Registration successful:", isRegistered);
console.log("Credentials valid:", isValid);
