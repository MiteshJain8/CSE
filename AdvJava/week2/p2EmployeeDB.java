package AdvJava.week2;

import java.sql.*;

public class P2EmployeeDB {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/dbName", USER = "root", PASS = ""; // Update this

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;

        try {
            // Establish the connection
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            stmt = conn.createStatement();

            // Create the employees table if it does not exist
            String createTableSQL = "CREATE TABLE IF NOT EXISTS employees (" +
                    "ID INT PRIMARY KEY, " +
                    "FName VARCHAR(50), " +
                    "LName VARCHAR(50), " +
                    "Project VARCHAR(100), " +
                    "Salary DECIMAL(10, 2))";
            stmt.executeUpdate(createTableSQL);
            System.out.println("Table 'employees' created or already exists.");

            // Insert sample data
            String insertDataSQL = "INSERT INTO employees (ID, FName, LName, Project, Salary) VALUES " +
                    "(1, 'Anika', 'Sharma', 'Web Development', 80000), " +
                    "(2, 'Rahul', 'Patel', 'Devops', 60000), " +
                    "(3, 'Priya', 'Gupta', 'Web Development', 75000), " +
                    "(4, 'Vivek', 'Kumar', 'Web Development', 50000), " +
                    "(5, 'Neha', 'Singh', 'Software Engineer', 45000), " +
                    "(6, 'Amit', 'Mishra', 'Web Development', 90000), " +
                    "(7, 'Meera', 'Nair', 'Data Analysis', 40000), " +
                    "(8, 'Rohan', 'Raj', 'Web Development', 70000)";
            stmt.executeUpdate(insertDataSQL);
            System.out.println("Sample data inserted into 'employees' table.");

            // i. Display details of all the employees
            String queryAllEmployees = "SELECT * FROM employees";
            ResultSet rsAll = stmt.executeQuery(queryAllEmployees);
            System.out.println("\nAll Employees:");
            System.out.println("ID\tFName\tLName\tProject\tSalary");
            while (rsAll.next()) {
                System.out.println(rsAll.getInt("ID") + "\t" +
                        rsAll.getString("FName") + "\t" +
                        rsAll.getString("LName") + "\t" +
                        rsAll.getString("Project") + "\t" +
                        rsAll.getBigDecimal("Salary"));
            }

            // ii. Display details of all the employees who work for project “Web Development”
            String queryWebDevelopment = "SELECT * FROM employees WHERE Project = 'Web Development'";
            ResultSet rsWebDev = stmt.executeQuery(queryWebDevelopment);
            System.out.println("\nEmployees in 'Web Development':");
            System.out.println("ID\tFName\tLName\tSalary");
            while (rsWebDev.next()) {
                System.out.println(rsWebDev.getInt("ID") + "\t" +
                        rsWebDev.getString("FName") + "\t" +
                        rsWebDev.getString("LName") + "\t" +
                        rsWebDev.getBigDecimal("Salary"));
            }

            // iii. Display the IDs of all those employees who have salary above 75,000 and are in “Web Development”
            String queryHighSalaryWebDev = "SELECT ID FROM employees WHERE Salary > 75000 AND Project = 'Web Development'";
            ResultSet rsHighSalary = stmt.executeQuery(queryHighSalaryWebDev);
            System.out.println("\nEmployees in 'Web Development' with Salary > 75,000:");
            System.out.println("ID");
            while (rsHighSalary.next()) {
                System.out.println(rsHighSalary.getInt("ID"));
            }

            // iv. Display the total number of employees who have salary less than 50,000
            String queryLowSalaryCount = "SELECT COUNT(*) AS total FROM employees WHERE Salary < 50000";
            ResultSet rsTotalLowSalary = stmt.executeQuery(queryLowSalaryCount);
            if (rsTotalLowSalary.next()) {
                System.out.println(
                        "\nTotal number of employees with Salary < 50,000: " + rsTotalLowSalary.getInt("total"));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Close resources
            try {
                if (stmt != null)
                    stmt.close();
                if (conn != null)
                    conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}