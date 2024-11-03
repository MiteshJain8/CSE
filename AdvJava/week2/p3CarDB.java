package AdvJava.week2;

import java.sql.*;

public class P3CarDB {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/dbName", USER = "root", PASS = ""; // Update this

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;

        try {
            // Establish the connection
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            stmt = conn.createStatement();

            // Create the cars table if it does not exist
            String createTableSQL = "CREATE TABLE IF NOT EXISTS cars (" +
                    "Model VARCHAR(50) PRIMARY KEY, " +
                    "Company VARCHAR(50), " +
                    "Price DECIMAL(10, 2), " +
                    "Year INT)";
            stmt.executeUpdate(createTableSQL);
            System.out.println("Table 'cars' created or already exists.");

            // Insert sample data
            String insertDataSQL = "INSERT INTO cars (Model, Company, Price, Year) VALUES " +
                    "('ABC', 'Ford', 150000, 2010), " +
                    "('BCD', 'Mahindra', 120000, 2015), " +
                    "('CDE', 'Kia', 150000, 2018), " +
                    "('DEF', 'Tata', 200000, 2020)";
            stmt.executeUpdate(insertDataSQL);
            System.out.println("Sample data inserted into 'cars' table.");

            // i. Display details of all the Cars from the table
            String queryAllCars = "SELECT * FROM cars";
            ResultSet rsAll = stmt.executeQuery(queryAllCars);
            System.out.println("\nAll Cars:");
            printResultSet(rsAll);

            // ii. Insert a new row into the table and display all the details
            String insertNewCar = "INSERT INTO cars (Model, Company, Price, Year) VALUES " +
                    "('EFG', 'Hyundai', 130000, 2021)";
            stmt.executeUpdate(insertNewCar);
            System.out.println("\nNew car inserted:");
            ResultSet rsNewCar = stmt.executeQuery(queryAllCars);
            printResultSet(rsNewCar);

            // iii. Delete a row from the table where the Model="ABC" and Year=2010
            String deleteCar = "DELETE FROM cars WHERE Model='ABC' AND Year=2010";
            stmt.executeUpdate(deleteCar);
            System.out.println("\nCar with Model 'ABC' and Year '2010' deleted.");

            // Display all cars after deletion
            ResultSet rsAfterDelete = stmt.executeQuery(queryAllCars);
            System.out.println("\nAll Cars after deletion:");
            printResultSet(rsAfterDelete);

            // iv. Update the price of a row from 150000 to 125000
            String updatePrice = "UPDATE cars SET Price = 125000 WHERE Model='CDE'";
            stmt.executeUpdate(updatePrice);
            System.out.println("\nPrice updated for Model 'CDE'.");

            // Display all cars after the update
            ResultSet rsAfterUpdate = stmt.executeQuery(queryAllCars);
            System.out.println("\nAll Cars after updating the price:");
            printResultSet(rsAfterUpdate);

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

    private static void printResultSet(ResultSet rs) throws SQLException {
        System.out.println("Model\tCompany\tPrice\t\tYear");
        while (rs.next()) {
            System.out.println(rs.getString("Model") + "\t" +
                    rs.getString("Company") + "\t" +
                    rs.getBigDecimal("Price") + "\t" +
                    rs.getInt("Year"));
        }
    }
}
