package AdvJava.week4;

import java.sql.*;

public class P3CustomerDB {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/dbName", USER = "root", PASS = ""; // Update this

    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement pStmt = null;
        Statement stmt = null;

        try {
            // Establish the connection
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            stmt = conn.createStatement();

            // Create the Customer table if it does not exist
            String createTableSQL = "CREATE TABLE IF NOT EXISTS Customer (" +
                    "ID INT PRIMARY KEY, " +
                    "Name VARCHAR(100), " +
                    "Type_of_Customer VARCHAR(50), " +
                    "Amount_Spent INT)";
            stmt.executeUpdate(createTableSQL);
            System.out.println("Table 'Customer' created or already exists.");

            // i. Insert rows using PreparedStatement
            String insertSQL = "INSERT INTO Customer (ID, Name, Type_of_Customer, Amount_Spent) VALUES (?, ?, ?, ?)";
            pStmt = conn.prepareStatement(insertSQL);
            pStmt.setInt(1, 1);
            pStmt.setString(2, "Raj");
            pStmt.setString(3, "Regular");
            pStmt.setInt(4, 1500);
            pStmt.executeUpdate();

            pStmt.setInt(1, 2);
            pStmt.setString(2, "Riya");
            pStmt.setString(3, "Premium");
            pStmt.setInt(4, 2500);
            pStmt.executeUpdate();

            System.out.println("Sample data inserted into 'Customer' table.");

            // ii. Display details of all the Customer table
            String queryAllCustomers = "SELECT * FROM Customer";
            ResultSet rs = stmt.executeQuery(queryAllCustomers);
            System.out.println("ID\tName\tType_of_Customer\tAmount_Spent");
            while (rs.next()) {
                System.out.println(rs.getInt("ID") + "\t" +
                        rs.getString("Name") + "\t" +
                        rs.getString("Type_of_Customer") + "\t\t\t" +
                        rs.getBigDecimal("Amount_Spent"));
            }

            // iii. Demonstrate the details of the database by using DatabaseMetaData
            DatabaseMetaData dbMetaData = conn.getMetaData();
            System.out.println("\nDatabase MetaData:");
            System.out.println("Database Product Name: " + dbMetaData.getDatabaseProductName());
            System.out.println("Database Product Version: " + dbMetaData.getDatabaseProductVersion());
            System.out.println("Driver Name: " + dbMetaData.getDriverName());
            System.out.println("Driver Version: " + dbMetaData.getDriverVersion());

            // iv. Demonstrate the details of the ResultSet by using ResultSetMetaData
            ResultSetMetaData rsMetaData = rs.getMetaData();
            System.out.println("\nResultSet MetaData:");
            int columnCount = rsMetaData.getColumnCount();
            for (int i = 1; i <= columnCount; i++) {
                System.out.println("Column " + i + ": " + rsMetaData.getColumnName(i) + " - " + rsMetaData.getColumnTypeName(i));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Close resources
            try {
                if (stmt != null)
                    stmt.close();
                if (pStmt != null)
                    pStmt.close();
                if (conn != null)
                    conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
